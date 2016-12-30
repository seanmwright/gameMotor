from Scene import Scene

class SceneManager(object):
    """docstring for SceneManager"""
    def __init__(self):
        super(SceneManager, self).__init__()
        self.scenes = []


    def changeScene(self, newScene):
        """TODO: Docstring for changeScene.

        :newScene: the new scene to switch to
        """
        if len(self.scenes) > 0:
            self.scenes[-1].exit()
        self.scenes.append(newScene)
        self.scenes[-1].enter()

    def update(self, dt):
        """TODO: Docstring for update.

        :dt: TODO
        """
        self.scenes[-1].update(dt)
        #space.step(1/60.0)

    def draw(self):
        """TODO: Docstring for draw.
        """
        self.scenes[-1].draw()
        #spriteBatch.draw()
        pass
