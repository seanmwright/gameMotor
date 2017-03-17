import pyglet

from Scene import Scene

from Quad import Quad
from GameObject import GameObject

class GameScene(Scene):
    def __init__(self, objectManager, space):
        Scene.__init__(self)
        self.objectManager = objectManager
        self.space = space
        self.spriteBatch = pyglet.graphics.Batch()

    def enter(self):
        self.player = GameObject(self.spriteBatch,self.space,500,500)
        self.objectManager.addObject(self.player)

    def update(self, dt):
        self.objectManager.updateObjects(dt)

    def draw(self):
        self.spriteBatch.draw()
