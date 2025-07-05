from transformers import pipeline

# Load once globally (cached after first run)
translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang="eng_Latn",
    tgt_lang="ory_Orya"
)

def translate_to_odia(text):
    """
    Translates English text to Odia using NLLB model.
    """
    result = translator(text)
    return result[0]['translation_text']


# Test block
if __name__ == "__main__":
    sample = "Odia literature has a long and rich history."
    print("Translated:", translate_to_odia(sample))