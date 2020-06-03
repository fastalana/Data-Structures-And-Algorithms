def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == []:
        return -1

    if number == None or number <= 0:
        return -1

    left = 0
    middle = find_pivot(input_list)
    right = len(input_list) - 1

    if number > input_list[middle]:
            return -1 # the number is not in the list

    while left < right:
        if number == input_list[middle]:
            return middle
        elif number < input_list[middle]:
            if number >= input_list[left]:
                right = middle - 1
            else: # number < input_list[left]
                left = middle + 1
            middle = (left + right)//2
        else: # number > input_list[middle]
            if number > input_list[right]:
                return -1
            elif number == input_list[right]:
                return right
            else: # number < input_list[right]
                left = middle + 1
                right = right - 1
                middle = (left + right)//2
    if number != input_list[middle]:
        return -1
    else:      
        return middle

def find_pivot(input_list):
    """
    Find the pivot in the array using binary search

    Args:
       input_list(array)
    Returns:
       int: pivot or 0 (if the array is sorted)
    """
    left = 0
    mid = 0
    right = len(input_list) - 1

    if input_list[0] > input_list[1]:
        return 0
    else:
        while left < right:
            mid = (left + right)//2
            if input_list[mid] > input_list[left]: # this side of the list is sorted
                    return mid
            else:
                mid += 1
                right -= 1
    
def linear_search(input_list, number):
    if input_list == []:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[],1])
test_function([[1],None])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], -1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 0])

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4]) 
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 8]) 

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 100])
test_function([[600, 700, 800, 900, 1000, 100, 200, 300, 400], 125])