# Explanations

## Project 01 - Least Recently Used Cache (LRU)
The `cache` is a dictonary/map.  When the `get()` and `set()` methods are called this is a simple lookup with a key making the complexity O(1).  `recent_keys` is a queue that keeps track of the order in which the cache has been accessed; adding keys to the end of `recent_key` when the `get()` **or** `set()` methods are called; this also has a complexity of O(1).  However, the function `cache` must check to see if the key is in the `recent_keys` list, making the complexity O(n).

## Project 02 - Finding Files
This problem was solved recursively, visiting each folder.  The complexity is dependent on the depth and width of the folders; i.e. how many folders and how deep does the folder strucutre go.  In this case the complexity is O(d*w) where _w_ is the maxium number of folders at any given path and _d_ is the maxium number of folders within any given folder.

## Project 03 - Huffman Coding
To implement the Huffmann Algorithm required the construction of several classes and functions.  Each of those functions are outlined below, along with an explanation of their implementation and complexity:

* Node - class with only one `__init__` function, O(1)
* Tree - class with only one `__init__` function, O(1)
* character_frequencies- From a string this method counts how many times each caracter is present in teh original string.  This information is stored in a map using the charcter as a key and frequency as the value.  Because we loop through the entire string the time complexity is O(n).
* sort_character_frequencies - This method takes the output, a map, from the character_frequencies function.  A new list is generated that uses Python's sort method making the complexity O(nlogn).
* encode_tree - This method encodes the entire length of the string, making the time complexity O(n).
* insert_element_into_list - When this method is called, it loops over the entire tree, making the time complexity O(n).
* huffman_encoding - The primary function of this method is to create the encoded tree.  Excluding other functions that are called within this method, this method has two independent (i.e. non-nested loops), making the time complexity O(n).
* huffman_decoding - The primary function of this method is to decode the tree.  Excluding other functions that are called within this method, this method has one independent (i.e. non-nested loops), making the time complexity O(n).  
* decode = The decode method within the `huffman_decoding` function iterates through the entire encoded string, recursively.  This function also has a complexity of O(n) 

Summary:
The time complexity to encode and decode a string using Huffman Coding is O(nlogn).

## Project 04 - Active Directory
This problem was solved recursively, visiting each group, to check if the user is in the group.  The complexity is dependent on the number of groups and the number of users.  In this case the complexity is O(g*u) where _g_ is the maxium number of groups in any given group and _u_ is the maxium number of users within any given group.

## Project 05 - Block Chain
This problem was solved used a linked list.  Each new node points to the previous hash.  Each time a new node is added we add it to the end of the list.  However, if we keep track of the end of the list, which we do, the new block can be added directly to the end of the current blockchain making the complexity is O(1).

## Project 06 - Union and Intersection of Two Linked Lists
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

## Problem 07 - Square Root of an Integer
This problem could be solved with:
```
	if(number < 0):
         print("Negative number does not have a square root")
         return None
	return round(number**(1/2),0)
```

Or one could use a variation of the binary search algorithm with a complexity of O(logn).  The `sqrt` function takes the midpoint of the input number and tries to determine if the square of the midpoint is the original number.  The midpoint is adjusted by incrementing or decrementing the bounds around the midpoint until the square root is found.  The space complexity is independent of the input, the function is guessing specific numbers and only three integer variables are held in memory.  The space complexity is O(1).

## Problem 08 - Search in a Rotated Sorted Array
This uses variations of binary search to:

* Find the location of the pivot in `find_pivot` 
* Find the location of the target in `rotated_array_search`

In a traditional binary search implementation the array is sorted.  However, this array is rotated on a pivot.  It is critcal to find the pivot to determine which side of the pivot the target will be on; left, right or equal to the pivot.  Further, arrays on either side of the pivot will be sorted.  Once you know what side of the pivot the target is on, you can use binary search on the approriate side of the pivot.  The time complexity of this solution is O(logn), because both functions leverage binary search.  The space complexity is independent of the input, the function is merely pointing to specific numbers in an existing array.  The space complexity is O(1).

## Problem 09 - Rearrange Array Digits
In the given examples and test cases, a pattern was identified:
* Each of the two digits start with the largest digit in the array
* Alternate the next largest digits to find the maxium sum

For example:
[1, 2, 3, 4, 5] would result in [531, 42], where 5 is the largest number in the array, followed by 4.  The next largest digit is 3, followed by 2.  These numbers are the succeeding numbers of 5 and 4 respecitively to create the largest sum.

After identifying the pattern, it became apparent that the list needed to be sorted.  The given expected time complexity of this function is O(nlog(n)).  To keep this within the time complexity bound, the quicksort algorithm is used to sort the input array.  From there the `rearrange_digits` function goes through each digit in the sorted array.  The time complexity of `rearrange_digits` is O(n) which is less than quicksort; the time complexity of this function is still O(nlogn).  The space complexity is independent of the input, the function is merely pointing to specific numbers and then generating a new array of two digits.  The space complexity is O(1).

## Problem 10 - Dutch National Flag Problem
This algorithm is implemented in place and done with a single traversal.  The time complexity is O(n); each item is looked at once. 0's go to the front and 2's to the back.  `next_0` increments for 0 integers, `next_2` decrements for 2 integers and `index` is incremented once for 1 integers.  Everything is done in place making the space complexity O(n), where n is the size of the original array.

## Problem 11 - Autocomplete with Tries
This problem uses the trie data structure which is a type of tree.  The trie data structure offers a good payoff between time and space complexity.

To find suffixes, from a given prefix, we first call `find` on the Trie class to find the root node where the prefix exists. With the root node of the prefix, `suffixes` is called from the TrieNode class. Using recursion the function searches all children.  The time complexity is O(p+s), where `p` is the height of the nodes it takes to form the prefix and `s` is the numer of suffixes with the prefix.  The worst case space complexity of a triehappens when a word (or words) have no common characters between them leaving a node for each character. This would result in a space complexity of O(n).

## Problem 12 - Unsorted Array Integer
This traverses the list once, keeping track of if the current number is larger or smaller than the stored minimum or maxium for previous values in the array.  The time complexity is O(n).  No algorithms or data structures were used to solve this problem.  Everything is done in place making the space complexity O(n), where n is the size of the original array.

## Problem 13 - HTTP Router Using a Trie
This problem uses the trie data structure which is a type of tree.  The trie data structure offers a good payoff between time and space complexity.

The RouteTrieNode and RouteTrie is very similar to a regular TrieNode and Trie with the exception of adding a handler in the RouteTrieNode. In the `Router` function, routes are initialized with a `RouteTrie`, adding a "/" root route and a `not found handler`. To add a handler or lookup a route, call the RouteTrie `insert` and `find` passing a list of paths with the back slash removed.

The complexity of this function is similar to a traditional trie; O(k).  For this function 'k' is the length of the path between back slashes.  Ex: /home, k=1, whereas /home/about k=2.  The worst case space complexity of a triehappens when a word (or words) have no common characters between them leaving a node for each character. This would result in a space complexity of O(n).  In this case the space complexity would still be the same, O(n), with the caveat that every route is just one word; i.e. /home, /contact, /about, etc.