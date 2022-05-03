class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def printPoint(point):
    print("(" + str(point.x) + "," + str(point.y) + ")")
    
def negative(point):
    point.y = -point.y
    point.x = point.x
    return point
        
class Polynomial:
    def __init__(self, a,b,p):
        self.a = a
        self.b = b
        self.p = p
    def pointsIsValid(self,x,y):
        if x**3 + self.a*x + self.b == y**2:
            return True
        else:
            return False

def inverse(point,mod):
    for i in range(mod):
        if (point*i)%mod == 1:
            return i

def addition(p1, p2, polynomial):
    λ = 0
    if((p1.x == p2.x and p1.y == p2.y) or (p1.x == p2.x and p1.y == -p2.y)):
        λ = ((3 * p1.x * p1.x + polynomial.a) * inverse(2 * p1.y, polynomial.p)%polynomial.p)%polynomial.p
    else:
        λ = ((p2.y - p1.y) * inverse(p2.x - p1.x, polynomial.p)%polynomial.p)%polynomial.p
    x = (λ**2 - p1.x - p2.x) % polynomial.p
    y = (λ * (p1.x - x) - p1.y) % polynomial.p
    point = Point(x,y)
    return point

def multiplication(n, p1, polynomial):
    point = p1
    for i in range(n-1):
        point = addition(point, p1, polynomial)
    return point

polynomial = Polynomial(1,1,23)
p =  Point(3, 10)
q =  Point(9,7)

printPoint(addition(p, negative(q), polynomial))
printPoint(multiplication(2, p, polynomial))