import numpy as np
import matplotlib.pyplot as plt

x = [ 0.0, 1.5, 3.6, 4.3, 5.0 ]
y = [ 1.732, 0.931, 1.732, 1.327, 1.289 ] 

def func ( x ):
    return (x + 3 * np.cos(x) ** 2) ** 0.5 - 0.2 * x

origX = np.linspace(min(x), max(x), 1000)
origY = func(origX)

def simpson_integral(function, start_p, end_p, eps = 0.0001):
    """
    Simpson's rule integration.
    pieces is a power of 2.
    Returns numeric value of the integral of the given function.  
    """
    pieces = 2
    offset = (end_p - start_p) / pieces

    integral = (end_p - start_p) / (3 * pieces) * (function(start_p) + 4 * function(start_p + offset) + function(end_p))

    while True:
        old = integral
        pieces *= 2
        pos = x[0] + (end_p - start_p) / pieces * 2
        offset = (end_p - start_p) / pieces
        integral /= 2
        for i in range(int(pieces / 4)):
            integral -= (end_p - start_p) / (3 * pieces) * 2 * function(pos)
            integral += (end_p - start_p) / (3 * pieces) * 4 * (function(pos - offset) + function(pos + offset))
            pos += offset * 4
        if abs(integral - old) < eps:
            break

    return integral

plt.fill_between(origX, origY, 0.8, color = 'red')
plt.plot(origX, origY)

#plt.suptitle('m = {}'.format(pieces))
plt.title('Integral = {}'.format(simpson_integral(func, x[0], x[-1])))
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
