import pyglet
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *
    
import tkinter.messagebox
import time 

#Music Player Things
music = pyglet.resource.media('testSong.mp3')
player = pyglet.media.Player()

player.queue(music)

def toggleState():
    if player.playing:
        player.pause()
    else:
        player.play()
        return

def playcount():
    while player.playing:
        print('playing')
        app.time.set(player.time)
        time.sleep(1.0)
        if player.time == music.duration:
            app.time.set(0)
            #and move to next song
def playwait():
    while not player.playing:
        print(
            'waiting')
    playcount()
            
        
            

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
        self.backB = Button(self, text = "Back", command = self.back)
        self.playB = Button(self, text = "Play", command =  self.play)
        self.skipB =Button(self, text = "Skip", command =self.skip)

        self.backB.grid(row = 0)
        self.playB.grid(row = 1)
        self.skipB.grid(row = 2)


        """Volume"""
        self.vol = Scale(self, from_=100, to=0, orient=VERTICAL,
                    command = self.volchanged)
        self.vol.set(50)
        self.vol.grid(row = 0, column = 1, rowspan = 3, sticky = W)

        """Time Scrub"""
        self.time = Scale(self, to= music.duration, from_ = 0,
                          orient = HORIZONTAL , command = self.timechanged)
        #when song ends this needs to change, use config?

        self.time.grid(row = 0, column = 2, rowspan = 3, sticky = W)
        
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

    def timechanged(self, event):
        if abs(self.time.get() - player.time) > 1:
            player.seek(self.time.get() )
        
    def updateTime(self):
        self.time.set(player.time)
        self.after(1000,self.updateTime)
    

    def placeholder(self, text):
        messagebox.showerror(title = "no code",
                           message = "Oops! There's no code here! "
                             + "This should have %s" %(text),
                           parent = self)




if __name__ == "__main__":
    root = Tk() 
    root.title("MOMAR")
    root.geometry("200x103")

    app = PlayWindow(root)
    app.updateTime()

    root.mainloop()
    
