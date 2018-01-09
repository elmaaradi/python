from classes import Ecurve
from classes import Point

c = Ecurve(-2, 4, 5)
p_1 = Point(c, 3, 5)
p_2 = Point(c, -2, 0)
res = p_1 + p_2
multiple=p_1*3
res.printPoint()
#multiple.printPoint()
print("the point 1 belongs ? :", c.belongs(p_1))
print("the point 2 belongs ? :", c.belongs(p_2))
# p_m=2p
p_m = p_1.multiple()
p_m.printPoint()
