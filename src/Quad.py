import pyglet

class Quad(object):
    def __init__(self, position, width, height):
        self.x = position[0]
        self.y = position[1]
        self.x2 = self.x + width
        self.y2 = self.y + height
        self.vertexList = pyglet.graphics.vertex_list(4,
                ('v2f',(self.x, self.y, self.x2, self.y, self.x2, self.y2, self.x, self.y2)),
                ('c3B',(255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255))
                )

    def draw(self):
        self.vertexList.draw(pyglet.gl.GL_QUADS)
