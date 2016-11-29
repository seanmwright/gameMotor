from MenuObject import MenuObject
from Utils import Text

class MenuNode(MenuObject):
    """docstring for MenuNode"""
    def __init__(self, position, text, fontSize):
        super(MenuNode, self).__init__(position, text, fontSize)
        self.children = []

    def arrangeChildren(self, position, spacing):
        x = position[0]
        y = position[1]
        for child in self.children:
            child.move((x,y))
            y -= spacing
