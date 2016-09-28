class ObjectManager(object):
    def __init__(self):
        self.gameObjects = []

    def addObject(self,gameObject):
        self.gameObjects.append(gameObject)
    
    def updateObjects(self,dt):
        for obj in self.gameObjects:
            obj.update(dt)
