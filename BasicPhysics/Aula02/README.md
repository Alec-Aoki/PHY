Sendo $$\vec r\ = (x(t), y(t), z(t))$$ o vetor posição, temos:

$x(t) = a\cos(\omega t)$

$y(t) = a\sin(\omega t)$

$z(t) = bt^2$

Como $\vec v(t)\ = ( \vec v_x(t)\ , \vec v_y(t)\ , \vec v_z(t)\ ) = ( \dot {x} (t) \ , \dot {y} (t) \, \dot {z} (t) \ )$ e:

$ \dot {x} (t) \ = -a \omega \sin(\omega t) $

$ \dot {y} (t) \ = a \omega \cos(\omega t) $

$ \dot {z} (t) \ = 2 b t $

Temos $\vec v(t)\ = ( -a \omega sin(\omega t), a \omega cos(\omega t), 2 b t )$.

Sendo $a = 5$, $\omega = 5$, $b = 9,3$ e $t = 1,8$:

$\left\| \vec v(t) \right\| = \sqrt{ a^2 \omega^2 \sin^2( \omega t ) + a^2 \omega^2 \cos^2( \omega t ) + 4 b^2 t^2 }$

$\left\| \vec v(t) \right\| = \sqrt{ a^2 \omega^2 + 4 b^2 t^2 }$

$\left\| \vec v(1,8) \right\| = \sqrt{ 5^2 . 5^2 + 4 . 9,3^2 . 1,8^2} = \sqrt{ 25 . 25 + 4 .86,49 . 3,24 }$

$\left\| \vec v(1,8) \right\| = \sqrt{ 625 + 1120,9104 } = \sqrt{ 1745,9104 }$

$\left\| \vec v(1,8) \right\| = 41,748 m/s$

Código em python:
```python
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
```
Comentário do monitor Gustavo: O cálculo está correto e o código compilou direitinho :)