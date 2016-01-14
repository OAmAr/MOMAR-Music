from pyglet import media , resource
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *
    
from os import listdir
from random import shuffle

import tkinter.messagebox
import math

class Playlist():

    def __init__(self):
        #start as all songs, can be changed to playlist or shuffle
        self.directory = 'music'
        self.allsongs = listdir(self.directory)
        self.pos = 0
        self.songText = self.allsongs[self.pos]
        self.song = self.loadCurrentSong()
        #self.song = resource.media('testSong.mp3')

    def loadCurrentSong(self):
        self.songText = self.allsongs[self.pos]
        return resource.media("%s/%s" %(self.directory, self.songText)) 
        
    def update(self):
        if self.pos >= len(self.allsongs):
            self.pos = 0
        self.song = self.loadCurrentSong()
        player.queue(self.song)
        player.next_source()
        app.time.configure(to=standPlay.song.duration)
        
    def next(self):
        self.pos = self.pos + 1
        self.update()
            
    def back(self):
        if player.time < 10:
            self.update()
        else:
            self.pos = self.pos - 1
            self.update()

#Music Player Things
standPlay = Playlist()

player = media.Player()

player.queue(standPlay.song)

def toggleState():
    if player.playing:
        player.pause()
        app.playB.config(text="Play")
    else:
        player.play()
        app.playB.config(text="Pause")
        return
        
            

#Window Things

class PlayWindow (Frame):
    """Main Window"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        #need to add current song/last song/file finding etc.
        
    def create_widgets(self):
        """Play, skip, back buttons"""
        #eventually change to images not text
        self.backB = Button(self, text = "Back", command = self.back, width = 5,
                            height = 1)
        self.playB = Button(self, text = "Play", command =  self.play, width= 5,
                            height = 1)
        self.skipB =Button(self, text = "Skip", command =self.skip, width= 5,
                           height = 1)
        
        self.backB.grid(row = 0, sticky= NW)
        self.playB.grid(row = 1, sticky= NW)
        self.skipB.grid(row = 2, sticky= SW, pady= (5, 2))

        """Labels"""
        self.timeLabel = Label(self, text= "00:00")
        self.songLabel = Label(self, text= "Song Title \n Artist")
        
        self.timeLabel.grid(row= 2 , column=2)
        self.songLabel.grid(row= 0 , column=2, sticky= N)

        """Volume"""
        self.vol = Scale(self, from_=100, to=0, orient=VERTICAL,
                    command = self.volchanged, length = 105)
        self.vol.set(50)
        
        self.vol.grid(row = 0, column = 1, rowspan = 3, sticky = NW)

        """Time seeker"""
        self.time = Scale(self, to= standPlay.song.duration, from_ = 0,
                          orient = HORIZONTAL , command = self.timechanged, showvalue = False)
        self.time.grid(row = 1, column = 2, sticky = SW)
        
    def back(self):
        standPlay.back()
        return
    
    def play(self):
        toggleState()
        return
    
    def skip(self):
        standPlay.next()
        return

    def volchanged(self, event):
        player.volume= float(event)/100

    def timechanged(self, event):
        value = int(event)
        minutes = value/60
        seconds = value%60
        timeAsText = "%2.2d:%2.2d" % (minutes, seconds)
        self.timeLabel.configure(text=timeAsText)
        self.songLabel.configure(text=standPlay.songText + "\nArtist")
        
        if abs(value - player.time) > 1:
            player.seek(value)
        
        
    def updateTime(self):
        print("Time:"+str(player.time)+" Duration:"+str(math.floor(standPlay.song.duration)))
        if standPlay.song.duration-1 <= player.time:
            self.after(1, standPlay.next)
        self.time.set(player.time)
        self.after(250,self.updateTime)
    




if __name__ == "__main__":
    root = Tk() 
    root.title("MOMAR")
    root.geometry("200x109")

    app = PlayWindow(root)
    app.updateTime()

    root.mainloop()
    
