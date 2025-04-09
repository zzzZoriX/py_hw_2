from __future__ import annotations
import math

class Vector2d:
    x: float; y: float
    
    def __init__(self, x: float, y:float):
        self.x = x
        self.y = y
        
    def __add__(self, other: Vector2d): return Vector2d(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vector2d): return Vector2d(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float): return Vector2d(self.x * scalar, self.y * scalar)
    
    def __len__(self): return int(math.sqrt(self.x ** 2 + self.y ** 2)) # интерпритатор ругался на float, поэтому пришлось запихнуть в int
    
    def __str__(self): return f'[{self.x} ; {self.y}]'
    
v = Vector2d(12, 32)
y = Vector2d(4, 1)

print(v + y)
print(v - y)
print(v * 12)
print(len(v))
print(v)

# -------------------------------------------------- #

class Money:
    dollars: int; cents: int
    
    def __init__(self, dollars: int, cents: int):
        self.cents = cents
        self.dollars = dollars
        
    def __add__(self, other: Money):
        dollars: int = self.dollars + other.dollars
        cents: int = self.cents + other.cents
        if(cents >= 100):
            dollars += 1
            cents -= 100
            
        return Money(dollars, cents)
    
    def __sub__(self, other: Money):
        dollars: int = self.dollars - other.dollars
        cents: int = self.cents - other.cents
        if(cents < 0):
            dollars -= 1
            cents = 100 - abs(self.cents - other.cents)
            
        return Money(dollars, cents)
    
    def __str__(self): return f'{self.dollars}.{self.cents}$'
    
a = Money(12, 42)
b = Money(1, 7)

print(a + b)
print(a - b)
print(a)

# -------------------------------------------------- #

class Time:
    h: int; m: int; s: int
    
    def __init__(self, h: int, m: int, s: int):
        self.s = s
        self.h = h
        self.m = m
        
    def __add__(self, other: Time):
        h = self.h + other.h
        
        m = self.m + other.m
        s = self.s + other.s
        if(s >= 60):
            m += 1
            s -= 60
            
        if(m >= 60):
            h += 1
            m -= 60
            
        return Time(h, m, s)
    
    def __len__(self): return self.s + self.m * 60 + self.h * 3600
    
    def __str__(self): return f'{self.h}:{(self.m if self.m >= 10 else f'0{self.m}')}:{self.s}'
    
d = Time(12, 5, 32)
y = Time(3, 8, 35)

print(d + y)
print(len(d))
print(d)

# -------------------------------------------------- #

class Point:
    x: int; y: int
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def __add__(self, other: Point): return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Point): return Point(self.x - other.x, self.y - other.y)
    
    def __str__(self): return f'[{self.x} ; {self.y}]'
    
p = Point(5, 7)
f = Point(9, 10)

print(p + f)
print(p - f)
print(p)

# -------------------------------------------------- #

class ColoredPoint(Point):
    color: str
    
    def __init__(self, x: int, y: int, color: str):
        super().__init__(x, y)
        self.color = color
        
    def __add__(self, other: ColoredPoint):
        point: Point = super().__add__(other)        
        return ColoredPoint(point.x, point.y, (self.color if self.color == other.color else 'black'))
    
    def __sub__(self, other: ColoredPoint):
        point: Point = super().__sub__(other)        
        return ColoredPoint(point.x, point.y, (self.color if self.color == other.color else 'black'))
    
    # len нету в базовом классе
    
    def __str__(self): return f'[ [{self.x} ; {self.y}]\tcolor: {self.color} ]'
    
r = ColoredPoint(3, 5, 'red')
h = ColoredPoint(8, -1, 'red')

print(r + h)
print(r - h)
print(r)

# -------------------------------------------------- #

class Matrix:
    a: int; b: int; c: int; d: int
    
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def __add__(self, other: Matrix): return Matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    
    def __mul__(self, num: int): return Matrix(self.a * num, self.b * num, self.c * num, self.d * num)
    
    def __len__(self): return 4 
    
    def __str__(self): return f'[[{self.a}, {self.b}], [{self.c}, {self.d}]]'
    
m = Matrix(1, 3, 5, 1)
g = Matrix(0, -1, 3, 4)

print(m + g)
print(m * 3)
print(len(m))
print(m)

# -------------------------------------------------- #

class Temperature:
    degrees: float
    
    def __init__(self, degrees: float):
        self.degrees = degrees
        
    def __add__(self, other: Temperature): return Temperature(self.degrees - other.degrees)
    def __sub__(self, other: Temperature): return Temperature(self.degrees - other.degrees)
    def __mul__(self, factor: int): return Temperature(self.degrees * factor)
    
    def __str__(self): return f'{self.degrees}C'
    
t = Temperature(32.4)
k = Temperature(36.6)

print(t + k)
print(t - k)
print(t * 4)
print(t)