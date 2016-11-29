from MenuObject import MenuObject
from Utils import Text

class MenuItem(MenuObject):
    def __init__(self, position, text, fontSize, function=None):
        super(MenuItem, self).__init__(position, text, fontSize)
        self.function = function
        if self.function == None:
            self.function = self.printSelf

    def printSelf(self):
        print(self.label.text)
