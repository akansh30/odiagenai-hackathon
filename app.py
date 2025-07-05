import streamlit as st
from utils import pdf_utils, lang_detect, summarizer, translator, tts
import tempfile
import os

st.set_page_config(page_title="Odia Literature Summarizer", layout="wide")
st.title("Odia Literature Summarizer with Voice ")

uploaded_file = st.file_uploader(" Upload a PDF (English or Odia)", type="pdf")

if uploaded_file:
    # Save the uploaded file to a temporary path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    with st.spinner(" Extracting text from PDF..."):
        raw_text = pdf_utils.extract_text_from_pdf(pdf_path)

    if not raw_text.strip():
        st.error("No text found in the PDF.")
        os.remove(pdf_path)
        st.stop()
    else:
        with st.spinner(" Detecting language..."):
            lang = lang_detect.detect_language(raw_text)

        st.success(f"Detected Language: **{lang.upper()}**")

        if lang == "en":
            with st.spinner("Summarizing English text..."):
                summary = summarizer.summarize_text(raw_text)
            with st.spinner("Translating summary to Odia..."):
                odia_summary = translator.translate_to_odia(summary)
        elif lang == "or":
            with st.spinner(" Summarizing Odia text..."):
                odia_summary = summarizer.summarize_text(raw_text)
        else:
            st.error(" Unsupported language. Please upload a PDF in English or Odia.")
            os.remove(pdf_path)
            st.stop()

        st.subheader(" Odia Summary:")
        st.write(odia_summary)

        if st.button("Play Odia Audio"):
            with st.spinner("Generating speech using Sarvam TTS..."):
                audio_path = tts.text_to_speech_sarvam(odia_summary)
                st.audio(audio_path, format="audio/wav")

        os.remove(pdf_path)
