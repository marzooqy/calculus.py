from math import *

def d(f):
	h = 0.000001
	return lambda x: (f(x + h / 2) - f(x - h / 2)) / h
	
def i(f, a, b):
	n = 1000000
	deltax = (b - a) / n
	return deltax * sum(f(a + deltax * (i + 0.5)) for i in range(n))