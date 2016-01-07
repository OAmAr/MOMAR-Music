#!/usr/bin/python

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *

import winsound
import tkSnack

#AUDIO PLAYER
def playPause():
    song = open("testSong.mp3").read()
    winsound.PlaySound(song, winsound.SND_MEMORY)

momarInstance = Tk()
momarInstance.title("MOMAR Music")
momarInstance.geometry("200x75")

#Frame is where things go
app = Frame(momarInstance)
#put frame on window
app.grid()
#Back button
backB= Button(app, text = "Back")
backB.grid()
#Play button
playB= Button(app, text = "Play", command = playPause)
playB.grid()
#Skip Button
skipB=Button(app, text = "Skip")
skipB.grid()




momarInstance.mainloop()

