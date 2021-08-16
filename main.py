import os
import time
import tkinter as tk
from pygame import mixer
    # sound.play()
    # time.sleep(sleep)


def FileN(folder):
        d = os.getcwd()
        os.chdir(d + "/" + folder)
        mixer.init()
        for i in os.listdir():
            print(i)
            sound = mixer.Sound(i) # add file name / file
            yield sound


class song1():
    def __init__(self):
        self.nsong = FileN(input("what folder? "))
        self.ne()

    def ne(self):
        self.sound.stop()
        self.sound = next(self.nsong)

def main():
    con = True
    root = tk.Tk()
    # nSong = FileN(input("what folder? "))
    # song = next(nSong)
    
    song = song1()
    play = tk.Button(root, text="play", command=lambda:song.sound.play())
    pause = tk.Button(root, text="pause", command=lambda:song.sound.stop())
    skip = tk.Button(root, text="skip", command=lambda:song.ne())
    play.grid(row=0, sticky=tk.EW)
    pause.grid(row=1, sticky=tk.EW)
    skip.grid(row=2, sticky=tk.EW)
    while con:
        # print(song.song)
        root.update_idletasks()
        root.update()

if __name__ == "__main__":
    main()