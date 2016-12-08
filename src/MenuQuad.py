import pyglet
from Quad import Quad

class MenuQuad(Quad):
    def __init__(self, position, width, height, color=(255,255,255)):
        self.x = position[0]-width/2
        self.y = position[1]-5-(height/2)
        self.x2 = self.x + width
        self.y2 = self.y + height

        self.vertexList = pyglet.graphics.vertex_list(4,
                ('v2f',(self.x, self.y, self.x2, self.y, self.x2, self.y2, self.x, self.y2)),
                ('c3B',(255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255))
                )

        self.width = width
        self.height = height
        self.color = color
