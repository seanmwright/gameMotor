import pyglet

class Line(object):
    def __init__(self, x1, y1, x2, y2):
        super(Line, self).__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.vertexList = pyglet.graphics.vertex_list(2,
                ('v2f',(self.x1, self.y1, self.x2, self.y2,)),
                ('c3B',(255, 255, 255, 255, 255, 255,))
                )

    def changeColor(self, r, g, b):
        self.vertexList.colors = (r, g, b, r, g, b)

    def draw(self):
        self.vertexList.draw(pyglet.gl.GL_LINES)
