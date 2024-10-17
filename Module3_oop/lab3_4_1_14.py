'''Lab for PCAP 3.4.1.14 @ 2024-10-17'''
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

def main() -> None:
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))

if __name__ == '__main__':
    main()
