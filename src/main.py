#!/usr/bin/env python3

import pyglet
from pyglet.window import key
from pyglet.window import mouse

import pymunk
from pymunk import pyglet_util

from Utils import Text

from InputManager import InputManager
from SceneManager import SceneManager

from ObjectManager import ObjectManager
from GameObject import GameObject

from MainMenuScene import MainMenuScene
from GameScene import GameScene

DEBUG = True
WIDTH = 1920
HEIGHT = 1080
GAMENAME = "gameMotor2D"

# setup resource path
pyglet.resource.path = ['../resources/']
pyglet.resource.reindex()

#TODO configManager
#TODO load config file

# create window
window = pyglet.window.Window(WIDTH,HEIGHT,
        vsync=not DEBUG,
        style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS,
            )
window.set_caption(GAMENAME)

# create physics space
space = pymunk.Space()
space.damping = .6
if DEBUG:
    debugDrawOptions = pyglet_util.DrawOptions()

# start managers
inputManager = InputManager(key,mouse)
sceneManager = SceneManager()
#TODO audioManager
objectManager = ObjectManager()

# create scenes
gameScene = GameScene(objectManager, space, WIDTH, HEIGHT)
mainMenuScene = MainMenuScene(window, inputManager, lambda:sceneManager.changeScene(gameScene))

# switch to main menu scene
sceneManager.changeScene(gameScene)

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
    sceneManager.update(dt)
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
    # return to terminate input event
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
    sceneManager.draw()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/240.0)
    pyglet.app.run()
