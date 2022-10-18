#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):
    n_domino_pieces = len(top)
    rotation=0
    # check if the task is possible and save the number which will be equal in the top of bottom row
    merged=top+bottom
    possible=True
    for i in merged:
        if merged.count(i)>=n_domino_pieces:
            equal_number=i
            possible=possible*True
            break
        else:
            possible=possible*False

    if possible==False:
        return -1
    else:
        if top.count(equal_number)>bottom.count(equal_number):
            for i in range(len(top)):
                if top[i]==equal_number:
                    pass
                else:
                    temp=0
                    top[i]=temp
                    top[i]=bottom[i]
                    bottom[i]=temp
                    rotation+=1
        else:
            for i in range(len(bottom)):
                if bottom[i]==equal_number:
                    pass
                else:
                    temp=0
                    bottom[i]=temp
                    bottom[i]=top[i]
                    top[i]=temp
                    rotation+=1
        return rotation


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 4, 1, 2, 2], [5, 2, 2, 2, 3, 4]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
