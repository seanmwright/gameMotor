from math import cos, sin, radians
from shapely.geometry import Point
from shapely.geometry import LineString

from Line import Line as DrawLine
from Polygon import Polygon as DrawPolygon

class VisibilityManager(object):
    def __init__(self):
        self.method = 0
        self.points = []
        self.segments = []
        self.rays = []
        self.lines = []
        self.polygon = None
        self.eyePosition = Point(950, 500)

    def addSegment(self, x1, y1, x2, y2):
        self.points.append(Point(x1,y1))
        self.points.append(Point(x2,y2))
        self.segments.append(LineString([(x1,y1),(x2,y2)]))

    def addWorldBoundaries(self, width, height):
        self.addSegment(1,1,width,1)
        self.addSegment(width,1,width,height)
        self.addSegment(width,height,1,height)
        self.addSegment(1,height,1,1)

    def castRays(self, eyePosition=Point(950,5)):
        self.eyePosition = eyePosition
        self.rays.clear()
        if self.method == 0:
            for point in self.points:
                line = LineString([(self.eyePosition.x,self.eyePosition.x),(point.x,point.y)])
                self.rays.append(line)
        if self.method == 1:
            for degree in range(0,360):
                rads = radians(degree)
                magnitude = 10000
                x = cos(rads)*magnitude
                y = sin(rads)*magnitude
                self.rays.append(LineString([(self.eyePosition.x,self.eyePosition.x),(x,y)]))
        #self.polygon = DrawPolygon(vertexList)

    def addLines(self):
        if True: #TODO debug
            for ray in self.rays:
                self.lines.append(DrawLine(ray.coords[0][0],
                                            ray.coords[0][1],
                                            ray.coords[1][0],
                                            ray.coords[1][1],))
        for segment in self.segments:
            self.lines.append(DrawLine(segment.coords[0][0],
                                        segment.coords[0][1],
                                        segment.coords[1][0],
                                        segment.coords[1][1],))

    def draw(self):
        #self.polygon.draw()
        for line in self.lines:
            line.draw()
