# Problem #1
# Implement the evaluate_poly function. This function evaluates a polynomial function for the
# given x value. It takes in a tuple of numbers poly and a number x. By number, we mean
# that x and each element of poly is a float. evaluate_poly takes the polynomial represented
# by poly and computes its value at x. It returns this value as a float.

def eval_poly(polyTuple, x):
    """takes in a tuple (), where the index is the power, and a value for x, and computes the polynomial"""

    total = 0.0
    for i in xrange(len(polyTuple)): #len returns the length of the elements, so range is length
        total += polyTuple[i] * (x ** i) #total is incremented by tuple element at [i], * x^i
    return total

print eval_poly((0.0, 0.0, 5.0, 9.3, 7.0),-13)
