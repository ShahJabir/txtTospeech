from gtts import gTTS
import os

msg: str
langu = 'en'
name: str

msg = input("Write a message:")
name = input("Name of your audio file:")

obj = gTTS(text=msg, lang=langu, slow=False)
obj.save(name+'.mp4')
os.system('start '+name+'.mp4')
