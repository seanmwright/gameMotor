import pyglet
from pyglet.window import key
from pyglet.window import mouse

class InputManager(pyglet.event.EventDispatcher):
    def __init__(self, key, mouse):
        self.key = key
        self.mouse = mouse

    def handleKeyboard(self, symbol, modifiers):
        if symbol==key.UP or symbol==key.K:
            self.dispatch_event('on_menu_up')
            return True
        if symbol==key.DOWN or symbol==key.J:
            self.dispatch_event('on_menu_down')
            return True
        if symbol==key.ENTER:
            self.dispatch_event('on_menu_confirm')
            return True
        if symbol==key.ESCAPE:
            self.dispatch_event('on_menu_back')
            return True

    def handleMouse(self, x, y, button=None, modifiers=None):
        if button == None:
            self.dispatch_event('on_mouse_motion', x, y)
        else:
            self.dispatch_event('on_mouse_press', x, y, button)

InputManager.register_event_type('on_menu_up')
InputManager.register_event_type('on_menu_down')
InputManager.register_event_type('on_menu_confirm')
InputManager.register_event_type('on_menu_back')
InputManager.register_event_type('on_mouse_press')
InputManager.register_event_type('on_mouse_motion')

'''
    # movement
    if symbol==key.W:
        objectManager.movePlayer(1)
    if symbol==key.S:
        objectManager.movePlayer(-1)
    if symbol==key.A:
        objectManager.turnPlayer(1)
    if symbol==key.D:
        objectManager.turnPlayer(-1)
'''

