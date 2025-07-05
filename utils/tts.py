import os
from dotenv import load_dotenv
from sarvamai import SarvamAI
from sarvamai.play import save

# Load the .env variables
load_dotenv()

def text_to_speech_sarvam(text, lang="od-IN", model="bulbul:v2", speaker="anushka"):
    api_key = os.getenv("SARVAM_API_KEY")
    if not api_key:
        raise ValueError("SARVAM_API_KEY not found in environment variables.")

    client = SarvamAI(api_subscription_key=api_key)
    audio = client.text_to_speech.convert(
        target_language_code=lang,
        text=text,
        model=model,
        speaker=speaker
    )
    output_path = "output_odia.wav"
    save(audio, output_path)
    return output_path