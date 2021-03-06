import pyglet
import random

from Scene import Scene

from Quad import Quad
from GameObject import GameObject
from VisibilityManager import VisibilityManager

class GameScene(Scene):
    def __init__(self, objectManager, inputManager, space, width, height):
        Scene.__init__(self)
        self.objectManager = objectManager
        self.inputManager = inputManager
        self.visibilityManager = VisibilityManager()
        self.space = space
        self.spriteBatch = pyglet.graphics.Batch()
        self.width = width
        self.height = height

    def enter(self):
        random.seed()
        for i in range(10):
            startx = random.randint(1,self.width)
            starty = random.randint(1,self.height)
            self.visibilityManager.addSegment( startx, starty, startx+random.randint(-100,100), starty+random.randint(-100,100))

        self.visibilityManager.addWorldBoundaries(self.width, self.height)
        self.visibilityManager.castRays()
        self.visibilityManager.addLines()
        self.inputManager.push_handlers(self.visibilityManager)
        #self.player = GameObject(self.spriteBatch,self.space,500,500)
        #self.objectManager.addObject(self.player)

    def update(self, dt):
        self.visibilityManager.update()
        self.objectManager.updateObjects(dt)

    def draw(self):
        self.objectManager.draw()
        self.visibilityManager.draw()
        self.spriteBatch.draw()
