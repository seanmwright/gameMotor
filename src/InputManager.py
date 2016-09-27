class InputManager(object):
    def __init__(self, key, mouse):
        self.key = key
        self.mouse = mouse

    def handleKeys(self,symbol,modifiers):
        pass
        #TODO send event based on key bindings

    def handleMouse(self,x,y,button,modifiers):
        pass
