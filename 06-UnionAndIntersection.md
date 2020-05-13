For the union and intersection the linked lists were transformed into lists.  The location/ order of the list is irrelevant, however the value was critical to determine the union and intersected sets.  Once the intersection or union was known the list was transformed back into a linked list.  Let's take a closer look at the complexity of each of these functions.

* Union 
    * Takes two different linked lists and makes them lists - O(n)
    * Combines boths lists and makes the new, combined list a set - O(n)
    * Take the set list of the union of both lists and makes the list a linked list - O(n)
* Intersection - class with only one `__init__` function, O(1)
    * Takes two different linked lists and makes them lists - O(n)
    * Makes each list a unique set - O(1)
    * Create a map of the first list - O(n)
    * Check the second list to see if it contains the value in the dictonary of the first list.  If the second list contains the value from the first list add the value to a new list. - O(n)
    * Take the list of the intersection of both lists and make the list a linked list - O(n)

Summary:
The time complexity to determine the union or intersecton of a linked list is O(n).
