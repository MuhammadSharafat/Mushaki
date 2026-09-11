import asyncio
import edge_tts
import os


VOICE = "en-GB-RyanNeural"


async def generate_speech(text):

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save("voice.mp3")


def text_to_speech(text):

    asyncio.run(
        generate_speech(text)
    )

    with open("voice.mp3", "rb") as f:

        audio = f.read()

    os.remove("voice.mp3")

    return audio