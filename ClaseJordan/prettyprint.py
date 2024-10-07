from sympy import *
from sympy import init_printing
from sympy.abc import x

init_printing() 
funcion = sqrt(1/x)
mostrar_integral = Integral(funcion,x)
pprint(mostrar_integral)