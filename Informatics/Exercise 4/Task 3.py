#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    if a>0:
        return a
    elif a<0:
        return -a
    else:
        return 0

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a, b):
    # implement this function
    if a==0 and b==0:
        return None
    elif a>b:
        return gcd(b,a)
    else:
        if a==0:
            return b
        else:
            return gcd(b%a,a)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 15
b = 20
print(f"greatest common divisor of {a} and {b} is = {gcd(absolute_value(a),absolute_value(b))}")
