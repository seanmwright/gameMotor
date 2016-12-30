import pyglet

from Scene import Scene

from GameObject import GameObject

class GameScene(Scene):
    def __init__(self, objectManager, space):
        """TODO: to be defined1. """
        Scene.__init__(self)
        self.objectManager = objectManager
        self.space = space
        self.spriteBatch = pyglet.graphics.Batch()


    def enter(self):
        """TODO: Docstring for enter.
        :returns: TODO

        """
        self.player = GameObject(self.spriteBatch,self.space,50,50)
        self.objectManager.addObject(self.player)

    def update(self, dt):
        """TODO: Docstring for update.

        :dt: TODO
        :returns: TODO

        """
        self.objectManager.updateObjects(dt)

    def draw(self):
        """TODO: Docstring for draw.
        :returns: TODO

        """
        self.spriteBatch.draw()
