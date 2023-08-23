import os
from google.cloud import speech_v1p1beta1 as speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/nexa-396804-1911e49b6e89.json"

client = speech.SpeechClient()


def transcribe_audio(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        audio_content = audio_file.read()

    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-IN",
    )

    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript if response.results else "Could not understand the audio"