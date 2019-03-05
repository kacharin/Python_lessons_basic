# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

"""

import math

class Triangle:
    def __init__(self, a, b, c):
        # Метод считает длинну стороны по координатам точек
        def side(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2
                             + (point1[1] - point2[1]) ** 2)
        self.a = a
        self.b = b
        self.c = c
        # Считаем длину всех сторон
        self.ab = side(self.a, self.b)
        self.bc = side(self.b, self.c)
        self.ca = side(self.c, self.a)
    # Считаем площадь треугольника по формуле Герона, 
    # которая взята тут https://clck.ru/EUCMh
    def area(self):
        semiperim = self.perimeter() / 2
        return math.sqrt(semiperim
                         * (semiperim - self.ab)
                         * (semiperim - self.bc)
                         * (semiperim - self.ca))
    # Считаем периметр
    def perimeter(self):
        return self.ab + self.bc + self.ca
    # Считаем высоту
    def hTriangle(self):
        return self.area() / (self.ab / 2)
 
 
points = Triangle((1, 1), (15, 8), (6, 15))

print('Параметры треугольника: ')
print(f'- площадь = {round(points.area(),2)};')
print(f'- высота = {round(points.hTriangle(),2)};')
print(f'- периметр = {round(points.perimeter(),2)}.')

"""

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

"""

import math

class Trapeze:
    def __init__(self, a, b, c, d):
        # Метод считает длинну стороны по координатам точек
        def side(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2
                             + (point1[1] - point2[1]) ** 2)
        # Считаем площадь треугольника как в 1-й задаче
        def areatri(len1, len2, len3):
            semiperim = (len1 + len2 + len3) / 2
            return math.sqrt(semiperim
                             * (semiperim - len1)
                             * (semiperim - len2)
                             * (semiperim - len3))
        
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = side(self.a, self.b)
        self.bc = side(self.b, self.c)
        self.cd = side(self.c, self.d)
        self.da = side(self.d, self.a)
        self.diagonalac = side(self.c, self.a)
        self.diagonalbd = side(self.b, self.d)
        self.perimeter = self.ab + self.bc + self.cd + self.da
        # Площадь трапеции проще посчитать 
        # как сумму площадей 2-х треугольников из которых она состоит
        self.area = areatri(self.ab, self.diagonalbd, self.da) \
                    + areatri(self.diagonalbd, self.bc, self.cd)
    def areat(self):
        return self.area
    def perimetert(self):
        return self.perimeter
    def sideab(self):
        return self.ab
    def sidebc(self):
        return self.bc
    def sidecd(self):
        return self.cd
    def sideda(self):
        return self.da
    # Проверка равнорабочести трапеции
    def isTrapezeEqu(self):
        if self.diagonalac == self.diagonalbd:
            return True
        return False


# Для упрощения проверки возьмем координаты квадрата,  
# т.к. это частный случай равнорабочей трапеции
points = Trapeze((3, 3), (12, 3), (12, 12), (3, 12))

if points.isTrapezeEqu() == True:
    print('Параметры равнорабочей трапеции: ')
    print(f'- площадь = {round(points.areat(),2)};')
    print(f'- периметр = {round(points.perimetert(),2)};')
    print(f'- длинны сторон AB = {round(points.sideab(),2)}, \
BC = {round(points.sidebc(),2)}, \
CD = {round(points.sidecd(),2)}, \
DA = {round(points.sideda(),2)}.')
else:
    print('Трапеция не равнорабочая.')

"""
