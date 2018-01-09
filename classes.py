class Ecurve:
    """ELLIPTIC CURVE CLASS"""

    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def getDescriminant(self):
        return ""

    def __str__(self):
        return 'y^2 = x^3 + {}x + {}'.format(self.a, self.b)

    def belongs(self, point):
        return point.y ** 2 == point.x ** 3 + self.a * point.x + self.b
    # def generatePoint(self):
    #     s=randint(99999999,646845666456864)
    #     res=s**3+self.a*s+self.b
    #     return (math.sqrt(res))


class Point:
    """pint has x and y"""

    def __init__(self, curve, x, y):
        self.x = x
        self.y = y
        self.curve = curve

    def printPoint(self):
        print("(", self.x, ",", self.y, ")")

    # Si on additionne deux points distincts, P + Q = R.
    #
    # λ = (yq − yp) / (xq − xp)
    # xr = λ2 − xp − xq
    # yr = λ(xp − xr) − yp
    # Si on additionne additionne(double) un point avec lui - même, P + P = R.
    # λ = (3x2p + a) / (2yp)
    # xr = λ2 − 2x_p
    # yr = λ(xp − xr) − yp
    def __add__(self, Q):

        x_1, x_2 = self.x, Q.x
        y_1, y_2 = self.y, Q.y
        lamda = (y_2 - y_1) / (x_2 - x_1)
        x_3 = lamda * lamda - x_1 - x_2
        y_3 = lamda * (x_1 - x_3) - y_1
        # point confondu
        if y_1 == y_2 and y_1 == 0 and x_1 == x_2:
            raise Exception("point confondu unique")
        # point resultat à l'infini
        if x_2 == x_1 and y_1 == -y_2:
            raise Exception('Point resultat situé à l infini')
        return Point(self.curve, x_3, y_3)

    def multiple(self, n):
        lambda2 = (3 * self.x ** 2 + self.curve.a) / 2 * self.y
        xr = lambda2 ** 2 - 2
        p_m = Point(self.curve, xr, lambda2 * (self.x - xr) - self.y)
        if(n==0):
            return p_m
        else:
            return self.multipleHint(p_m,n)

    def multipleHint(self):
        lambda2 = (3 * self.x ** 2 + self.curve.a) / 2 * self.y
        xr = lambda2 ** 2 - 2
        p_m = Point(self.curve, xr, lambda2 * (self.x - xr) - self.y)
        return p_m

def __mul__(self, n):
    if n < 0:
        return -self * -n
    if n == 0:
        return Point(self.curve)
    else:
        Q = self
        R = self if n & 1 == 1 else Point(self.curve)
        i = 2
        while i <= n:
            Q = Q + Q
            if n & i == i:
                R = Q + R
    return R
