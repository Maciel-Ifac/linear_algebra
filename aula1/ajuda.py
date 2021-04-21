#import numpy as np 
#from numpy.linalg import det,inv
import sympy as sp


a, b, c, d = sp.symbols("a, b, c, d")
x, y, w, z = sp.symbols('x, y, w, z')


d1 = sp.Matrix([[a,b],[c,d]])
d2 = sp.Matrix([[x,y],[w,z]])

print(sp.Matrix.det(d1))