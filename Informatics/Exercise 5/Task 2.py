#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    d2={}
    for i in d.items():
        if i[1] not in d2:
            d2[i[1]]=[i[0]]
        else:
            d2[i[1]].append(i[0])
            d2[i[1]].sort()
    return d2

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"b":1, "a":1, "c":3}))
