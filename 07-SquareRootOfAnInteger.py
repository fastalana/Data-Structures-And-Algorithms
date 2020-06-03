def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == None:
        return None

    if(number < 0):
        return None
    
    left = 0
    middle = 0
    right = number
    
    while left <= right:
        middle = (left + right)//2
        target = middle*middle
        if target == number:
            return middle
        elif target > number:
            right = middle - 1
        else:
            left = middle + 1
            
    return right
        
print ("Pass" if  (None == sqrt(number=None)) else "Fail")
print ("Pass" if  (None == sqrt(-2)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (10 == sqrt(100)) else "Fail")
print ("Pass" if  (11 == sqrt(128)) else "Fail")
