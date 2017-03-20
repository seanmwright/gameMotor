from sympy import Point2D

from sympy.geometry import Segment
from sympy.geometry import Ray
from sympy.geometry import Line

from Line import Line as DrawLine

class VisibilityManager(object):
    def __init__(self):
        self.points = []
        self.segments = []
        self.rays = []
        self.lines = []
        self.polygon = []
        self.eyePosition = Point2D(512, 334)

    def addSegment(self, x1, y1, x2, y2):
        self.points.append(Point2D(x1,y1))
        self.points.append(Point2D(x2,y2))
        self.segments.append(Segment((x1,y1),(x2,y2)))

    def castRays(self):
        for point in self.points:
            self.rays.append(Ray(self.eyePosition,point))
        for ray in self.rays:
            for segment in self.segments:
                if not Line.is_parallel(ray, segment):
                    if isinstance(ray.intersection(segment),Point2D):
                        self.polygon.append(Point2D(ray.intersection(segment)))

    def addLines(self):
        for ray in self.rays:
                self.lines.append(DrawLine(ray.p1.x,ray.p1.y,ray.p2.x,ray.p2.y))
        for segment in self.segments:
            if isinstance(segment, Segment):
                self.lines.append(DrawLine(segment.p1.x,segment.p1.y,segment.p2.x,segment.p2.y))

    def draw(self):
        for line in self.lines:
            line.draw()
