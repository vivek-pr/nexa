from utils.recorder import record_audio
from utils.stt import transcribe_audio
from utils.witai import get_intent_from_response


def main():
    audio_filename = "temp_recording.wav"
    print("Please speak your query after pressing Enter.")
    input("Press Enter to start recording...")
    record_audio(audio_filename, duration=10)  # Records for 10 seconds. Adjust as needed.

    print("Transcribing the recorded audio...")
    transcript = transcribe_audio(audio_filename)
    print(f"Transcript: {transcript}")
    intent = get_intent_from_response(transcript)
    print(f"Intent: {intent}")


if __name__ == "__main__":
    main()
