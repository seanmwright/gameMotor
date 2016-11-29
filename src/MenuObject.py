from Utils import Text

class MenuObject(object):
    def __init__(self, position, text, fontSize):
        self.position = position
        self.text = text
        self.fontSize = fontSize
        self.width = len(text)*(fontSize)
        self.label = Text(text,fontSize,position)

    def move(self, position):
        self.label.move( position )
        self.position = position

    def draw(self):
        self.label.draw()

    def checkBounds(self, x, y):
        if x >= self.position[0]-self.width/2 and x <= self.position[0]+self.width/2:
            if y >= self.position[1]-self.fontSize/2 and y <= self.position[1]+self.fontSize/2:
                return True
        else:
            return False
