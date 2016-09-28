import pyglet
import pymunk

class GameObject(object):
    def __init__(self,spriteBatch,x,y):
        self.sprite = self.addSprite(spriteBatch, x, y)

    def addSprite(self,spriteBatch,x,y):
        image=pyglet.image.load('../resources/penta.png')
        return pyglet.sprite.Sprite(image,x=x,y=y,batch=spriteBatch)
