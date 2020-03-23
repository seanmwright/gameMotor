import pyglet

class Polygon(object):
    def __init__(self, vertexList):
        super(Polygon, self).__init__()
        self.vertexList = pyglet.graphics.vertex_list(  len(vertexList),
                                                        'v2f',
                                                        'c3b')
        self.vertexList.colors = []
        for i in range(0, len(vertexList)):
            for i in range(0,2):
                self.vertexList.colors.append(255)
        self.vertexList.vertices = vertexList

    def draw(self):
        self.vertexList.draw(pyglet.gl.GL_POLYGON)
