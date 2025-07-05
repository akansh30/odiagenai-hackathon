# Odia Literature Summarizer with Voice (GenAI Hackathon)

A Streamlit-based web app that summarizes Odia literature from uploaded PDFs and reads it out loud using Odia Text-to-Speech (TTS).

![Screenshot 2025-07-05 122401](https://github.com/user-attachments/assets/2bd9567d-d7ce-40d3-b475-3e726bee4d3d)

##  Features

-  Upload Odia or English PDFs
-  Summarization:
  - English PDFs → summarized in English → translated to Odia
  - Odia PDFs → summarized directly in Odia
-  Odia TTS playback using SarvamAI
-  Uses FalconsAI for summarization and NLLB model for translation

---

##  Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/akansh30/odiagenai-hackathon.git
cd odiagenai-hackathon
```
### 2. Create virtual environment
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Add API keys
Create a `.env` file in the root directory and add:
```bash
SARVAM_API_KEY=your_sarvamai_api_key
```

## Run the App
```bash
streamlit run app.py
```
The app will launch in your default browser at `http://localhost:8501`

## Demo Video
[Drive Link](https://drive.google.com/file/d/1YNhGfZ5MTNa9ZGrMIt6noKzINipV94b0/view?usp=sharing)

## Project Structure
```bash
.
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── .env                   # Your API keys (not committed)
├── utils/                 # Utility modules
│   ├── pdf_utils.py
│   ├── summarizer.py
│   ├── lang_detect.py
│   ├── translator.py
│   └── tts.py
└── output_odia.wav        # TTS audio output
```
## Acknowledgements
`Sarvam AI` for Odia TTS API
`FalconsAI` for summarization
`Facebook NLLB` for translation

