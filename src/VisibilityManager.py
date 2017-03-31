from sympy import Point2D, pi
from mpmath import radians

from sympy.geometry import Segment
from sympy.geometry import Ray
from sympy.geometry import Line

from Line import Line as DrawLine
from Polygon import Polygon as DrawPolygon

class VisibilityManager(object):
    def __init__(self):
        self.points = []
        self.segments = []
        self.rays = []
        self.lines = []
        self.polygon = []
        self.eyePosition = Point2D(512, 334, evalute=False)

    def addSegment(self, x1, y1, x2, y2):
        self.points.append(Point2D(x1,y1))
        self.points.append(Point2D(x2,y2))
        self.segments.append(Segment((x1,y1),(x2,y2)))

    def addWorldBoundaries(self, width, height):
        self.segments.append(Segment((1,1),(width,1)))
        self.segments.append(Segment((width,1),(width,height)))
        self.segments.append(Segment((width,height),(1,height)))
        self.segments.append(Segment((1,height),(1,1)))

    def castRays(self):
        vertexList = []
        walls = []
        for degree in range(0,360):
            ray = Ray(self.eyePosition,angle=radians(degree), evalute=False)
            for segment in self.segments:
                intersection = ray.intersection(segment)
                if len(intersection) > 0:
                    print(str(intersection[0]))
        #self.polygon = DrawPolygon(vertexList)

    def addLines(self):
        for ray in self.rays:
                self.lines.append(DrawLine(ray.p1.x,ray.p1.y,ray.p2.x,ray.p2.y))
        for segment in self.segments:
            if isinstance(segment, Segment):
                self.lines.append(DrawLine(segment.p1.x,segment.p1.y,segment.p2.x,segment.p2.y))

    def draw(self):
        #self.polygon.draw()
        for line in self.lines:
            line.draw()
