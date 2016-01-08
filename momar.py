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
        playB= Button(app, text = "Play", command = toggleState)
    else:
        player.play()
        playB= Button(app, text = "Pause", command = toggleState)

#Window Things
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

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
        
    def back(self):
        self.placeholder("gone back.")
        return
    
    def play(self):
        toggleState()
        return
    
    def skip(self):
        self.placeholder("skipped.")
        return
    
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
