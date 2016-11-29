from pyglet.window import mouse

from Utils import Text
from MenuNode import MenuNode
from MenuItem import MenuItem

class Menu(object):
    def __init__(self,window):
        # positioning
        centerWidth = window.width/2
        y = window.height-40
        self.window = window
        self.titlePostition = (centerWidth,y)
        self.menuPosition = (centerWidth, self.titlePostition[1]-(window.height/3))
        self.fontSize = 32
        self.menuSpacing = (float(self.fontSize)*1.33)**1.1

        # build menu hierarchy
        mainMenu = MenuNode(self.titlePostition, "game engine", self.fontSize)
        play = MenuItem(self.menuPosition, "play", self.fontSize)
        quit = MenuItem(self.menuPosition, "quit", self.fontSize)

        options = MenuNode(self.menuPosition, "options", self.fontSize)
        options.children.append(MenuItem(self.menuPosition, "volume", self.fontSize))
        options.children.append(MenuItem(self.menuPosition, "sfx", self.fontSize))
        options.children.append(MenuItem(self.menuPosition, "FoV", self.fontSize))

        self.rootNode = mainMenu
        self.rootNode.children.append(play)
        self.rootNode.children.append(options)
        self.rootNode.children.append(quit)

        # setup the node stack
        self.currentNode = self.rootNode
        self.previousNodes = []

        # layout children
        self.arrangeMenu(self.currentNode)

        # setup initial menu object focus
        self.focusFirstChild()

        # keyboard focus until mouse movement
        self.keyboardHighlight = True

    def on_menu_confirm(self):
        if self.focus != None and isinstance(self.focus,MenuNode):
            self.previousNodes.append(self.currentNode)
            self.currentNode = self.focus
            self.focusFirstChild()
            self.arrangeMenu(self.currentNode)
            self.currentNode.label.unhighlight()
        else:
            self.focus.function()
        return True

    def on_menu_back(self):
        self.currentNode.label.unhighlight()
        for child in self.currentNode.children:
            child.label.unhighlight()
        if len(self.previousNodes) > 0:
            self.currentNode = self.previousNodes.pop()
            self.focusFirstChild()
            self.arrangeMenu(self.currentNode)
        return True

    def on_menu_down(self):
        self.keyboardHighlight = True
        focusIndex = self.getFocusIndex()
        if focusIndex < len(self.currentNode.children)-1:
            self.focus = self.currentNode.children[focusIndex+1]
        else:
            self.focus = self.currentNode.children[0]
        return True

    def on_menu_up(self):
        self.keyboardHighlight = True
        focusIndex = self.getFocusIndex()
        length = len(self.currentNode.children)
        if focusIndex > 0:
            self.focus = self.currentNode.children[focusIndex-1]
        else:
            self.focus = self.currentNode.children[length-1]
        return True

    def on_mouse_press(self, x, y, button):
        if self.focus.checkBounds(x, y) and button == mouse.LEFT:
            self.on_menu_confirm()

    def on_mouse_motion(self, x, y):
        self.keyboardHighlight = False
        for child in self.currentNode.children:
            if child.checkBounds(x, y):
                child.label.highlight()
                self.focus = child
            else:
                child.label.unhighlight()

    def arrangeMenu(self, node):
        self.currentNode.move(self.titlePostition)
        node.arrangeChildren(self.menuPosition,self.menuSpacing)

    def draw(self):
        # draw node title
        self.currentNode.draw()
        # draw current node's children
        for childNode in self.currentNode.children:
            if self.keyboardHighlight:
                if childNode == self.focus:
                    childNode.label.highlight()
                else:
                    childNode.label.unhighlight()
            childNode.draw()

    def getFocusIndex(self):
        if self.focus != None:
            return self.currentNode.children.index(self.focus)

    def focusFirstChild(self):
        self.focus = self.currentNode.children[0]

