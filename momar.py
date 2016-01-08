import pyglet
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *

#Music Player Things
music = pyglet.resource.media('testSong.mp3')
player = pyglet.media.Player()

player.queue(music)

def toggleState():
    if player.playing:
        player.pause()
    else:
        player.play()

#Window Things
momarInstance = Tk()
momarInstance.geometry("200x75")

#Frame is where things go
app = Frame(momarInstance)
#put frame on window
app.grid()
#Back button
backB= Button(app, text = "Back")
backB.grid()
#Play button
playB= Button(app, text = "Play", command = toggleState)
playB.grid()
#Skip Button
skipB=Button(app, text = "Skip")
skipB.grid()
