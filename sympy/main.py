#!/usr/bin/env python

import sympy as sp
x, y, z = sp.symbols('x y z')
sp.init_printing(use_unicode=True)

print(sp.diff(x**3 + 5 + 7))
