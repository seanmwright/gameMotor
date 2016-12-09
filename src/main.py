#!/usr/bin/python

import pyglet
from pyglet.window import key
from pyglet.window import mouse

import pymunk
from pymunk import pyglet_util

from Utils import Text
from InputManager import InputManager
from ObjectManager import ObjectManager
from GameObject import GameObject
from Menu import Menu

DEBUG = True
gameName = "gameMotor2D"

# setup resource path
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

#TODO configManager
#TODO load config file

# create window
window = pyglet.window.Window(800,600,
        vsync=not DEBUG,
        style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS,
            )
window.set_caption(gameName)

# create physics space
space = pymunk.Space()
space.damping = .6
if DEBUG:
    debugDrawOptions = pyglet_util.DrawOptions()

# start managers
inputManager = InputManager(key,mouse)
#TODO sceneManager
#TODO audioManager
objectManager = ObjectManager()

spriteBatch = pyglet.graphics.Batch()

#objectManager.addObject(GameObject(spriteBatch,space,window.width/2,400))

menu = Menu(window)
menu.rootNode.children[2].function = pyglet.app.exit
inputManager.push_handlers(menu)

# debug
if DEBUG:
    print("pyglet version: "+str(pyglet.version))
    print("pymunk version: "+str(pymunk.version))
    print("vsync: "+str(window.vsync))
    timeElap = 0
    timeText = Text(int(timeElap), 32, (window.width/2,50), (255, 255, 255, 255))
    fpsDisplay = pyglet.clock.ClockDisplay()

def update(dt):
    global DEBUG
    global timeElap
    space.step(1/60.0)
    objectManager.updateObjects(dt)
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

    # pass input to input manager
    # return to terminate event
    return inputManager.handleKeyboard(symbol, modifiers)

@window.event
def on_mouse_press(x,y,button,modifiers):
    inputManager.handleMouse(x,y,button,modifiers)

@window.event
def on_mouse_motion(x, y, dx, dy):
    inputManager.handleMouse(x, y)

@window.event
def on_draw():
    global DEBUG
    window.clear()
    if DEBUG:
        timeText.draw()
        fpsDisplay.draw()
        space.debug_draw(debugDrawOptions)
    menu.draw()
    spriteBatch.draw()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/240.0)
    pyglet.app.run()
