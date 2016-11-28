from Utils import Text

class MenuNode(object):
    """docstring for MenuNode"""
    def __init__(self, text, fontSize):
        super(MenuNode, self).__init__()
        self.label = Text(text,fontSize,(0,0))
        self.list = []
        self.focus = 0

    def arrangeChildren(self, position, spacing):
        x = position[0]
        y = position[1]
        for child in self.list:
            child.label.move((x,y))
            y -= spacing

    def focusNext(self):
        self.focus+=1
        if self.focus > len(self.list)-1:
            self.focus = 0

    def focusPrevious(self):
        self.focus-=1
        if self.focus < 0:
            self.focus = len(self.list)-1

    def draw(self):
        self.label.draw()
