import pyglet
from pyglet.window import key

window = pyglet.window.Window()
music = pyglet.resource.media('testSong.mp3')
player = pyglet.media.Player()

player.queue(music)

def toggleState():
    if player.playing:
        player.pause()
    else:
        player.play()
        

label = pyglet.text.Label('MOMAR Music',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_key_press(symbol,modifiers):
    if symbol == key.SPACE:
        toggleState()

pyglet.app.run()
