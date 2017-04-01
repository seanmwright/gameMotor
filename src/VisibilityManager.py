from math import cos, sin, radians
from shapely.geometry import Point
from shapely.geometry import LineString

from Line import Line as DrawLine
from Polygon import Polygon as DrawPolygon

class VisibilityManager(object):
    def __init__(self):
        self.points = []
        self.segments = []
        self.rays = []
        self.lines = []
        self.polygon = None
        self.eyePosition = Point(512, 334)

    def addSegment(self, x1, y1, x2, y2):
        self.points.append(Point(x1,y1))
        self.points.append(Point(x2,y2))
        self.segments.append(LineString([(x1,y1),(x2,y2)]))

    def addWorldBoundaries(self, width, height):
        self.segments.append(LineString([(1,1),(width,1)]))
        self.segments.append(LineString([(width,1),(width,height)]))
        self.segments.append(LineString([(width,height),(1,height)]))
        self.segments.append(LineString([(1,height),(1,1)]))

    def castRays(self):
        self.rays.clear()
        for degree in range(0,360):
            rads = radians(degree)
            magnitude = 10000
            x = cos(rads)*magnitude
            y = sin(rads)*magnitude
            self.rays.append(LineString([(self.eyePosition.x,self.eyePosition.x),(x,y)]))
        #self.polygon = DrawPolygon(vertexList)

    def addLines(self):
        for segment in self.segments:
            if isinstance(segment, LineString):
                self.lines.append(DrawLine(segment.coords[0][0],
                                            segment.coords[0][1],
                                            segment.coords[1][0],
                                            segment.coords[1][1],))
    '''
        for ray in self.rays:
                self.lines.append(DrawLine(ray.p1.x,ray.p1.y,ray.p2.x,ray.p2.y))
    '''

    def draw(self):
        #self.polygon.draw()
        for line in self.lines:
            line.draw()
