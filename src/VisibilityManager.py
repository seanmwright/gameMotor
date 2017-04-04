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
        self.polygon = []
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

    def castRays(self):
        self.rays.clear()
        if self.method == 0:
            for point in self.points:
                line = LineString([(self.eyePosition.x,self.eyePosition.y),(point.x,point.y)])
                self.rays.append(line)
        if self.method == 1:
            for degree in range(0,360):
                rads = radians(degree)
                magnitude = 10000
                x = cos(rads)*magnitude
                y = sin(rads)*magnitude
                self.rays.append(LineString([(self.eyePosition.x,self.eyePosition.y),(x,y)]))
        #self.polygon = DrawPolygon(vertexList)

    def calculatePolygon(self):
        self.polygon.clear()
        for ray in self.rays:
            intersections = []
            for segment in self.segments:
                if ray.intersects(segment):
                    intersections.append((self.eyePosition.distance(ray.intersection(segment)),ray.intersection(segment)))
            self.polygon.append(sorted(intersections)[0][1])

    def addLines(self):
        self.lines.clear()
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

        if True: #TODO debug
            for point in self.polygon:
                line = DrawLine(point.x-5,
                                point.y-5,
                                point.x+5,
                                point.y+5)
                line.changeColor(255,0,0)
                self.lines.append(line)

    def update(self):
        self.castRays()
        self.calculatePolygon()
        self.addLines()

    def draw(self):
        for line in self.lines:
            line.draw()

    def on_mouse_motion(self, x, y):
        self.eyePosition = Point(x, y)

