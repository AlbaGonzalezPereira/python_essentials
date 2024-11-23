# pip install gTTS desde el cmd
from gtts import gTTS
import os
tts = gTTS('Hola, ¿a que Python es apasionante?', lang='es')
tts.save('hello.mp3') # crea un mp3 de lo que se escribe arriba
os.system('start hello.mp3') # lo ejecuta