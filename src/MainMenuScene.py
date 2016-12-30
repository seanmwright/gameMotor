import pyglet

from Scene import Scene

from Menu import Menu

class MainMenuScene(Scene):
    def __init__(self, window, inputManager):
        Scene.__init__(self)
        self.menu = Menu(window)
        self.menu.rootNode.children[2].function = pyglet.app.exit
        inputManager.push_handlers(self.menu)

    def draw(self):
        self.menu.draw()
