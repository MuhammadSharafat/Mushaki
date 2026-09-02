from playsound import playsound
import eel

# playing assistant sound function

@eel.expose
def playassistantSound():
    music_dir = "D:\\Mushaki\\www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)