#!/usr/bin/python

import pyglet
from pyglet.window import key
from pyglet.window import mouse

import pymunk
from pymunk import pyglet_util

from Utils import Text
from InputManager import InputManager

DEBUG = True
gameName = "gameMotor2D"

# setup resource path
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

#TODO load config file

# create window
window = pyglet.window.Window(800,600,vsync=not DEBUG)
window.set_caption(gameName)

# start managers
inputManager = InputManager(key,mouse)
#TODO configManager
#TODO eventManager
#TODO uiManager
#TODO sceneManager
#TODO audioManager
#TODO objectManager

# debug
if DEBUG:
    print("pyglet version: "+str(pyglet.version))
    print("pymunk version: "+str(pymunk.version))
    print("vsync: "+str(window.vsync))
    timeElap = 0
    timeText = Text( int(timeElap), 32, (window.width/2,50))
    fpsDisplay = pyglet.clock.ClockDisplay()

def update(dt):
    global DEBUG
    global timeElap
    if DEBUG:
        timeElap += dt
        timeText.update(int(timeElap))

def toggleFullscreen():
    if window.fullscreen:
        window.set_fullscreen(False)
    else:
        window.set_fullscreen(True)

@window.event
def on_key_press(symbol, modifiers):
    # toggle fullscreen
    if symbol==key.F11 or (modifiers==4 and symbol==key.ENTER):
        toggleFullscreen()
    inputManager.handleKeys(symbol,modifiers)

@window.event
def on_mouse_press(x,y,button,modifiers):
    inputManager.handleMouse(x,y,button,modifiers)

@window.event
def on_draw():
    global DEBUG
    window.clear()
    #TODO draw
    if DEBUG:
        timeText.draw()
        fpsDisplay.draw()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/240.0)
    pyglet.app.run()
