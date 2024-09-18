import math
import numpy as np
import sympy

t = sympy.symbols('t')
omega = sympy.symbols('w')
a = sympy.symbols('a')
b = sympy.symbols('b')

#componentes do vetor posição:
x = a*sympy.cos(omega*t)
y = a*sympy.sin(omega*t)
z = b*(t**2)

#componentes do vetor velocidade:
Vx = x.diff(t)
Vy = y.diff(t)
Vz = z.diff(t)

# a = 5
# w = 5
# b = 9.3
# t = 1.8
Vx = float(Vx.subs([(a, 5), (omega, 5), (t, 1.8)]))
Vy = float(Vy.subs([(a, 5), (omega, 5), (t, 1.8)]))
Vz = float(Vz.subs([(b, 9.3), (t, 1.8)]))

V = np.array([Vx, Vy, Vz])

V_norm = np.linalg.norm(V)

print(V_norm)

