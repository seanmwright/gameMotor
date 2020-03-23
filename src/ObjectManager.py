import pymunk
from pymunk import Vec2d
class ObjectManager(object):
    def __init__(self):
        self.gameObjects = []

    def addObject(self,gameObject):
        self.gameObjects.append(gameObject)

    def updateObjects(self,dt):
        for obj in self.gameObjects:
            obj.update(dt)

    def draw(self):
        for obj in self.gameObjects:
            obj.draw()

    def movePlayer(self, direction):
        player = self.gameObjects[0]
        player.body.apply_force_at_local_point((0,1000.0*direction),(0,-10.0))

    def turnPlayer(self, direction):
        player = self.gameObjects[0]
        player.body.torque = 10000*direction

