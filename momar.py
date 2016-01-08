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
import tkinter.messagebox
def toggleState():
    if player.playing:
        player.pause()
    else:
        player.play()

#Window Things

class Player (Frame):
    """Main Window"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        #need to add current song/last song/file finding etc.
        
    def create_widgets(self):
        """Play, skip, back buttons"""
        #eventually change to images not text
        self.backB = Button(self, text = "Back", command = self.back)
        self.playB = Button(self, text = "Play", command =  self.play)
        self.skipB =Button(self, text = "Skip", command =self.skip)

        self.backB.grid()
        self.playB.grid()
        self.skipB.grid()

        """Volume"""
        self.vol = Scale(self, from_=100, to=0, orient=VERTICAL,
                    command = self.volchanged)
        self.vol.grid()
        
    def back(self):
        self.placeholder("gone back.")
        return
    
    def play(self):
        toggleState()
        return
    
    def skip(self):
        self.placeholder("skipped.")
        return

    def volchanged(self, event):
        player.volume= float( self.vol.get())/100
        print (player.volume)
        
    
    def placeholder(self, text):
        messagebox.showerror(title = "no code",
                           message = "Oops! There's no code here! "
                             + "This should have %s" %(text),
                           parent = self)



if __name__ == "__main__":
    root = Tk() 
    root.title("MOMAR")
    root.geometry("200x80")
    
    app = Player(root)

    root.mainloop()
