import Exceptions as exc
e = 1e-9

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "x = {0:.5f}, y = {1:.5f}".format(self.x, self.y)

#p = Point(1,1)
#print(p.__str__())

#class Line:
#    def __init__(self, p1, p2):
#        self.p1 = p1
#        self.p2 = p2

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Intersect:
    def __init__(self, line1 , line2):
        """ конструктор
            line1 = a1x + b1y = c1
            line1 = a2x + b2y = c2
        """
        self.line1 = line1
        self.line2 = line2
        self.det = self._main_det(self.line1, self.line2)

    def _det2x2(self, a11, a12, a21, a22):
        """возвращает определить матрицы 2x2
            |a11 a12|
            |a21 a22|  
        """
        return (1.0)*a11*a22-a21*a12

    def _main_det(self, line1, line2):
        """ возвращает главный определить матрицы
            |a1 b1|
            |a2 b2|  
        """
        res = self._det2x2(line1.a, line1.b, line2.a, line2.b)
        return self._det2x2(line1.a, line1.b, line2.a, line2.b)

    def _intersect_point(self, line1,line2):
        """ возвращает точку пересечения прямых
            x = det x / det 
            y = det y / det
            det x = | c1 b1|
                    | c2 b2|

            det y = | a1 c1|
                    | a2 c2|
        """
        px = self._det2x2(line1.c, line1.b, line2.c, line2.b) / self.det
        py = self._det2x2(line1.a, line1.c, line2.a, line2.c) / self.det
        return Point(px, py)

    def is_parallel(self, line1,line2):
        """ Возвращает True, если прямые параллельны(при чем они могут лежать на одной прямой)
            В этом случаи либо точек пересечений бесконечное множество, либо точек пересечения не существует(система несовместна)
        """
        if abs(self.det) < e:
            return True
        return False

    def is_equivalent(self, line1,line2):
        """ возвращает True, если прямые совпадают(лежат на одной прямой)
        то есть коэффициенты прямых пропорциональны
            a1/a2==b1/b2==c1/c2
            a1*b2-a2*b1==0
            a1*c2-a2*c1==0
            b1*c2-b2*c1==0
            |a1 b1|   |a1 c1|   |b1 c1|
            |a2 b2|   |a2 c2|   |b2 c2|
        """
        if abs(self.det) > e:
           return False
        if abs(self._det2x2(line1.a, line1.c, line2.a, line2.c)) > e:
           return False
        if abs(self._det2x2(line1.b, line1.c, line2.b, line2.c)) > e:
           return False
        return True

    def find_cross(self):
        if self.is_parallel(self.line1, self.line2):
            if self.is_equivalent(self.line1, self.line2):
                raise exc.StraightIsEqualError()
            else:
                raise exc.StraightIsParallelError()       
        return self._intersect_point(self.line1, self.line2)

