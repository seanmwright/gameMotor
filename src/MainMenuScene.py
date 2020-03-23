import pyglet

from Scene import Scene

from Menu import Menu

class MainMenuScene(Scene):
    def __init__(self, window, inputManager, playGame):
        Scene.__init__(self)
        self.menu = Menu(window)
        self.menu.rootNode.children[0].function = playGame
        self.menu.rootNode.children[2].function = pyglet.app.exit

    def enter(self):
        inputManager.push_handlers(self.menu)

    def exit(self):
        inputManager.pop_handlers(self.menu)

    def draw(self):
        self.menu.draw()
