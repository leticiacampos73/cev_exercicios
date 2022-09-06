import math
a = float(input('digite o angulo q deseja?'))
r = math.radians(a)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print(f'se o angulo for {a} \n o seno sera {s:.2f} \n o coseno sera{c:.2f} \n e a trangente sera {t:.2f}')