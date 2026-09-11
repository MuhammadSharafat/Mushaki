import os
import io

# ==========================================
# FFmpeg Configuration
# ==========================================

FFMPEG_BIN = r"C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.1-full_build-shared\bin"

# Add FFmpeg folder to Python PATH
os.environ["PATH"] = FFMPEG_BIN + os.pathsep + os.environ.get("PATH", "")


# ==========================================
# Imports
# ==========================================

import speech_recognition as sr
from pydub import AudioSegment


# Tell pydub exactly where FFmpeg is
AudioSegment.converter = os.path.join(
    FFMPEG_BIN,
    "ffmpeg.exe"
)


# ==========================================
# Speech To Text
# ==========================================

def speech_to_text(audio_bytes):

    recognizer = sr.Recognizer()

    try:

        print("====================================")
        print("Audio received:", len(audio_bytes), "bytes")
        print("FFmpeg:", AudioSegment.converter)
        print("====================================")


        # ----------------------------------
        # Convert recorded audio
        # ----------------------------------

        audio = AudioSegment.from_file(
            io.BytesIO(audio_bytes)
        )


        print("Audio loaded successfully!")
        print("Sample rate:", audio.frame_rate)
        print("Channels:", audio.channels)
        print("Duration:", len(audio), "ms")


        # ----------------------------------
        # Convert to mono 16kHz
        # ----------------------------------

        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(16000)


        # ----------------------------------
        # Export as WAV
        # ----------------------------------

        wav_buffer = io.BytesIO()

        audio.export(
            wav_buffer,
            format="wav"
        )

        wav_buffer.seek(0)


        print("WAV conversion successful!")


        # ----------------------------------
        # Read WAV with SpeechRecognition
        # ----------------------------------

        with sr.AudioFile(wav_buffer) as source:

            recorded_audio = recognizer.record(source)


        print("Audio read successfully!")
        print("Sending audio to Google Speech Recognition...")


        # ----------------------------------
        # Speech → Text
        # ----------------------------------

        text = recognizer.recognize_google(
            recorded_audio,
            language="en-US"
        )


        print("Recognized text:", text)
        print("====================================")


        return text


    # ======================================
    # Error Handling
    # ======================================

    except sr.UnknownValueError:

        print(
            "ERROR: Google could not understand the audio."
        )

        return ""


    except sr.RequestError as e:

        print(
            "ERROR: Google Speech Recognition failed:",
            e
        )

        return ""


    except Exception as e:

        print(
            "ERROR:",
            type(e).__name__,
            str(e)
        )

        return ""