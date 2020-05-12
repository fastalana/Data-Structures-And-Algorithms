class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_list(llist):
        """Given a linked list, return a list."""
        out = []
        node = llist.head

        while node is not None:
            out.append(node.value)
            node = node.next
        return out
    
def to_llist(list):
    """Given a list, return a linked list."""
    llist = LinkedList()
    for i in list:
        llist.append(i)
    return llist

def union(llist_1, llist_2):
    """
    Given two linked lists, return all the values present, with no duplicates.
    :param llist_1: first linked list
    :param llist_2: second linked list
    :return: all the values present, with no duplicates.
    """
    if LinkedList.size(llist_2) == 0:
        return llist_1
    
    if LinkedList.size(llist_1) == 0:
        return llist_2
    
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()

    list_all = list(set(list_1 + list_2))

    linked_list = to_llist(list_all)

    return linked_list


def intersection(llist_1, llist_2):
    """
    Given two linked lists, return values that are present in both linked lists, with no duplicates.
    :param llist_1: first linked list
    :param llist_2: second linked list
    :return: values that are present in both linked lists, with no duplicates.
    """
    if LinkedList.size(llist_2) == 0:
        return "No intersection between the two linked lists."
    
    if LinkedList.size(llist_1) == 0:
        return "No intersection between the two linked lists."
    
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()
    
    list_1 = list(set(list_1))
    list_2 = list(set(list_2))

    # Create a dictionary of the first list
    list_1_dict = {}
    for item in list_1:
        list_1_dict[item] = 0
    
    # Check the second list to see if it contains an item in the dictonary of the first list
    intersection_list = []
    for item in list_2:
        if item in list_1_dict:
            intersection_list.append(item)
            
    if len(intersection_list) == 0:
        return "No intersection between the two linked lists."
    else:      
        # Create a linked list from the intersection list above
        intersection_llist = to_llist(intersection_list)
        return intersection_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print(intersection(linked_list_1,linked_list_2))
# 4 -> 6 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
print (intersection(linked_list_3,linked_list_4))
# No intersection between the two linked lists.


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
# 1 -> 
print (intersection(linked_list_5,linked_list_6))
# No intersection between the two linked lists.