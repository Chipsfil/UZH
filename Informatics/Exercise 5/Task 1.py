#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    mergelist = []
    if len(a)==0 or len(b)==0:
        return mergelist
    elif len(a)>len(b):
        b.append(b[-1])
    elif len(a)<len(b):
        a.append(a[-1])
    elif len(a)==len(b):
        pass

    for i in range(len(a)):
        mergelist.append((a[i],b[i]))
    return mergelist



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [2,4]))
