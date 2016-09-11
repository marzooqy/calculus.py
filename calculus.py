def d(f, x):
	h = 0.000001
	return (f(x + h) - f(x - h)) / (2 * h)
	
def i(f, a, b):
	n = 1000000
	deltax = (b - a) / n
	return deltax * sum(f(a + deltax * (i + 0.5)) for i in range(n))
