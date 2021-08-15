import os
import time
import tkinter
from pygame import mixer

d = os.getcwd()
# print(d)
os.chdir(d + "/sounds")
# print(os.getcwd())
mixer.init()
for i in os.listdir():
    sound = mixer.Sound(i) # add file name / file
    sleep = sound.get_length()
    sound.play()
    time.sleep(sleep)
