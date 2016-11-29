from Utils import Text
from MenuNode import MenuNode
from MenuItem import MenuItem

class Menu(object):
    def __init__(self,window):
        centerWidth = window.width/2
        y = window.height-40

        self.window = window
        self.titlePostition = (centerWidth,y)
        self.menuPosition = (centerWidth, self.titlePostition[1]-(window.height/3))
        self.menuSpacing = 65
        self.fontSize = 32

        mainMenu = MenuNode("game engine", self.fontSize)
        play = MenuItem("play", self.fontSize)
        quit = MenuItem("quit", self.fontSize)

        options = MenuNode("options", self.fontSize)
        options.list.append(MenuItem("volume", self.fontSize))
        options.list.append(MenuItem("sfx", self.fontSize))
        options.list.append(MenuItem("FoV", self.fontSize))

        self.rootNode = mainMenu
        self.rootNode.list.append(play)
        self.rootNode.list.append(options)
        self.rootNode.list.append(quit)

        self.currentNode = self.rootNode
        self.previousNodes = []

        self.arrangeMenu(self.currentNode)

    def on_menu_confirm(self):
        if isinstance(self.currentNode.list[self.currentNode.focus],MenuNode):
            self.previousNodes.append(self.currentNode)
            self.currentNode = self.currentNode.list[self.currentNode.focus]
            self.arrangeMenu(self.currentNode)
        else:
            self.currentNode.list[self.currentNode.focus].function()
        return True

    def on_menu_back(self):
        if len(self.previousNodes) > 0:
            self.currentNode = self.previousNodes.pop()
            self.arrangeMenu(self.currentNode)
        return True

    def on_menu_down(self):
        self.currentNode.focusNext()
        return True

    def on_menu_up(self):
        self.currentNode.focusPrevious()
        return True

    def arrangeMenu(self, node):
        self.currentNode.label.move(self.titlePostition)
        node.arrangeChildren(self.menuPosition,self.menuSpacing)

    def draw(self):
        # draw node title
        self.currentNode.draw()
        # highlight selection
        for i in range(0,len(self.currentNode.list)):
            if i == self.currentNode.focus:
                self.currentNode.list[i].label.highlight()
            else:
                self.currentNode.list[i].label.unhighlight()
        # draw current node's children
        for childNode in self.currentNode.list:
            childNode.draw()
