from Utils import Text
from MenuQuad import MenuQuad

class MenuObject(object):
    def __init__(self, position, text, fontSize):
        self.position = position
        self.text = text
        self.fontSize = fontSize
        self.width = len(text)*(fontSize*.9)
        self.label = Text(text,fontSize,position, (0,0,0,255))
        self.quad = MenuQuad( position, self.width, self.fontSize )

    def move(self, position):
        self.label.move( position )
        self.position = position
        self.quad = MenuQuad( position, self.width, self.fontSize*1.6 )

    def draw(self):
        self.quad.draw()
        self.label.draw()

    def checkBounds(self, x, y):
        if x >= self.position[0]-self.width/2 and x <= self.position[0]+self.width/2:
            if y >= self.position[1]-self.fontSize/2 and y <= self.position[1]+self.fontSize/2:
                return True
        else:
            return False
