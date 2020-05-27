from gtts import gTTS
import os

msg: str
langu = 'en'
name: str
OS: int

msg = input("Write a message:")
name = input("Name of your audio file:")
print("which OS are you use ?\n1.Windows\n2.mac\n3.linux")
OS = input()

obj = gTTS(text=msg, lang=langu, slow=False)
obj.save(name+'.mp4')
if OS == 1:
    os.system("start " + name + ".mp4")
elif OS == 2:
    os.system("open " + name + ".mp4")
elif OS == 3:
    os.system("mpg123 " + name + ".mp4")
