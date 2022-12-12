import math

def find_roots(a, b, c):
    x1 =  ((math.sqrt(b*b-4*a*c)) - b)/(2*a)
    x2 =   (- (math.sqrt(b*b-4*a*c)) - b)/(2*a)
    return (x1,x2)
print(find_roots(2, 10, 8))
