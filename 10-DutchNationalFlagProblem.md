## Explanation

This algorithm is implemented in place and done with a single traversal.  The time complexity is O(n); each item is looked at once. 0's go to the front and 2's to the back.  `next_0` increments for 0 integers, `next_2` decrements for 2 integers and `index` is incremented once for 1 integers.  Everything is done in place making the space complexity O(n), where n is the size of the original array.


* Time Complexity: O(n)
* Space Complexity: O(n)