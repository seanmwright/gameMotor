import pyglet
import pymunk
import math

class GameObject(object):
    def __init__(self,spriteBatch,space,x,y):
        self.sprite = self.addSprite(spriteBatch, x, y)
        self.physics = self.addPhyiscal(space,x,y)

    def addLine(self, length, angle):
        pass

    def addSprite(self,spriteBatch,x,y):
        image=pyglet.image.load('../resources/penta.png')
        image.anchor_x = int(image.width/2)
        image.anchor_y = int(image.height/2)
        return pyglet.sprite.Sprite(image,batch=spriteBatch)

    def addPhyiscal(self,space,x,y):
        self.mass = 1
        self.radius = 50
        self.moment = pymunk.moment_for_circle(self.mass,0,self.radius)
        self.body = pymunk.Body(self.mass,self.moment)
        self.body.position = x,y
        self.shape = pymunk.Circle(self.body,self.radius)
        space.add(self.body,self.shape)

    def update(self,dt):
        self.sprite.position = self.body.position
        self.sprite.rotation = math.degrees(-self.body.angle)

    def draw(self):
        pass
