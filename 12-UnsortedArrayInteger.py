def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == []:
        return None

    min = ints[0]
    max = 0
    
    for i in ints:
        if i > max:
            max = i
        if i < min:
            min = i
    return (min, max)

### TESTS ###
print ("Pass" if (None == get_min_max([])) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0, 0])) else "Fail")
print ("Pass" if ((8, 9) == get_min_max([8,9])) else "Fail")
print ("Pass" if ((-50000000,9000256456) == get_min_max([-50000000,9000256456])) else "Fail")

import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

m = [i for i in range(0, 100)]  # a list containing 0 - 99
random.shuffle(m)
print ("Pass" if ((0, 99) == get_min_max(m)) else "Fail")

n = [i for i in range(-1, 60)]  # a list containing -1 - 59
random.shuffle(n)
print ("Pass" if ((-1, 59) == get_min_max(n)) else "Fail")