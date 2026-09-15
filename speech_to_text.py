import io
import speech_recognition as sr
from pydub import AudioSegment

def speech_to_text(audio_bytes):
    recognizer = sr.Recognizer()

    try:
        print("====================================")
        print("Audio received:", len(audio_bytes), "bytes")
        print("====================================")

        # Load incoming audio bytes into pydub AudioSegment
        audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
        
        # Convert audio to 16kHz Mono WAV format for SpeechRecognition compatibility
        audio = audio.set_channels(1).set_frame_rate(16000)

        # Save converted audio into an in-memory WAV buffer
        wav_buffer = io.BytesIO()
        audio.export(wav_buffer, format="wav")
        wav_buffer.seek(0)

        # Read the WAV audio using SpeechRecognition
        with sr.AudioFile(wav_buffer) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recorded_audio = recognizer.record(source)

        print("Audio read successfully!")
        print("Sending audio to Google Speech Recognition...")

        # Convert speech to text ("en-US" for English, "bn-BD" for Bangla)
        text = recognizer.recognize_google(
            recorded_audio,
            language="en-US"
        )

        print("Recognized text:", text)
        print("====================================")

        return text

    except sr.UnknownValueError:
        print("ERROR: Google Speech Recognition could not understand the audio.")
        return ""

    except sr.RequestError as e:
        print("ERROR: Could not request results from Google Speech Recognition service:", e)
        return ""

    except Exception as e:
        print("ERROR:", type(e).__name__, str(e))
        return ""