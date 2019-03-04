import math

class polynomial():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x):
        return self.a**2 * x + self.b * x + self.c

    def find_roots(self):
        d = self.b*self.b - 4*self.a*self.c
        if d < 0:
            return ()
        elif d == 0:
            return (-self.b / (2 * self.a),)
        else:
            x1 = (-self.b + math.sqrt(d))/(2 * self.a)
            x2 = (-self.b - math.sqrt(d))/(2 * self.a)
            return (x1, x2) 

    def __str__(self):
        return str(self.a) + "x^2 + " + str(self.b) + "x + " + str(self.c) 

# Test Cases

p1 = polynomial(1,5,6)
p2 = polynomial(2,4,2)
p3 = polynomial(5,5,6)

assert len(p1.find_roots()) == 2
assert len(p2.find_roots()) == 1
assert len(p3.find_roots()) == 0
assert str(p3) == "5x^2 + 5x + 6"
assert p3.evaluate(5) == 156