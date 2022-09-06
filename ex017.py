from math import hypot
co = float(input('qual é o comprimento do cteto oposto:'))
ca = float(input('qual é o comprimento do cteto adjacente:'))
h = hypot(co, ca)
print(f'a hipotenusa vai medir {h:.2f}')