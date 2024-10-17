'''Lab for PCAP 3.4.1.15 @ 2024-10-17'''
from math import hypot, fabs

class Point:
    def __init__(self, x:float=0.0, y:float=0.0) -> None:
        self.__x = x
        self.__y = y
    def getx(self) -> float:
        return self.__x
    def gety(self) -> float:
        return self.__y
    def distance_from_xy(self, x:float, y:float) -> float:
        xdiff = fabs(x - self.__x)
        ydiff = fabs(y - self.__y)
        return hypot(xdiff, ydiff)
    def distance_from_point(self, point) -> float:
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, vertice1:Point, vertice2:Point, vertice3:Point) -> None:
        self.__vertices = [vertice1, vertice2, vertice3]
    def perimeter(self) -> float:
        _pts = self.__vertices
        _len = len(self.__vertices)
        # The brackets are needed in {(i+1)%_len} since % is computed before +
        return sum([_pts[i].distance_from_point(_pts[(i+1)%_len]) for i in range(_len)])

def main() -> None:
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())

if __name__ == '__main__':
    main()
