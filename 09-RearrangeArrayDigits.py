def sort_a_little_bit(items, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
    
    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
    sort_all(items, 0, len(items) - 1)
    return items

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list == [] or input_list == None:
        return None

    sort_input_list = quicksort(input_list)
    highest_sum_list = []
    first_num = ''
    second_num = ''
    while len(sort_input_list) > 0:
        first = sort_input_list[-1]
        sort_input_list.pop(-1)
        first_num = first_num + str(first)
        if len(sort_input_list) == 0:
            break
        else:
            second = sort_input_list[-1]
            sort_input_list.pop(-1)
            second_num = second_num + str(second)

    highest_sum_list.append(int(first_num))
    highest_sum_list.append(int(second_num))
    return highest_sum_list

print ("Pass" if  (rearrange_digits([]) == None) else "Fail") # empty input_list
print ("Pass" if  (rearrange_digits(input_list=None) == None) else "Fail") # input_list is None
print ("Pass" if  (rearrange_digits([1, 2]) == [2, 1]) else "Fail") # input_list with only two digits
print ("Pass" if  (rearrange_digits([201, 200, 202, 203]) == [203201, 202200]) else "Fail") # input_list with large digits
print ("Pass" if  (rearrange_digits([4, 6, 2, 5, 9, 8]) == [964, 852]) else "Fail") # even number of digits in input_list
print ("Pass" if  (rearrange_digits([1, 2, 3, 4, 5]) == [531, 42]) else "Fail") # odd number of digits in input_list
