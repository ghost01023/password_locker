# LAB 1

# from sympy import *
# x, y, z = symbols('x, y, z')
# w1 = integrate(x ** 2 + y ** 2, (y, 0, x), (x, 0, 1))
# print(w1)


# from sympy import *
# x, y, z = symbols('x, y, z')
# w1 = integrate((x * y * z), (z, 0, 3 - x - y), (y, 0, 3 - x), (x, 0, 3))
# print(w1)


# LAB 2

# from sympy import *
# x = symbols('x')
#
# w1 = integrate(exp(-x), (x, 0, float('inf')))
# print(simplify(w1))


# from sympy import *
#
# x = symbols('x')
# w2 = integrate()


# LAB 3

from sympy.vector import *
from sympy import symbols

N = CoordSys3D('N')
x, y, z = symbols('x y z')
A = N.x**2*N.y + 2*N.x*N.z - 4
develop = Del()
display(develop(A))

gradA = gradient(A)
print(f"\nGradient of {A} is \n", gradA)

