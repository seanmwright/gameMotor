from Utils import Text

class MenuItem(object):
    """docstring for MenuItem"""
    def __init__(self, text, fontSize, function=None):
        super(MenuItem, self).__init__()
        self.label = Text(text,fontSize,(0,0))
        self.function = function
        if self.function == None:
            self.function = self.printSelf

    def printSelf(self):
        print(self.label.text)

    def draw(self):
        self.label.draw()
