# Problem #1
# Implement the evaluate_poly function. This function evaluates a polynomial function for the
# given x value. It takes in a tuple of numbers poly and a number x. By number, we mean
# that x and each element of poly is a float. evaluate_poly takes the polynomial represented
# by poly and computes its value at x. It returns this value as a float.

def eval_poly(poly, x):
    """takes in a tuple (), where the index is the power, and a value for x, and computes the polynomial"""

    total = 0.0 #initialize the base variable
    for value in range(len(poly)): #for the each element in the range that is equal to the length of the poly,
        total += poly[value] * (x**value) #increment the total by the value of the poly, time x raised to the index value
    return total

print eval_poly((0.0, 0.0, 5.0, 9.3, 7.0),-13)
