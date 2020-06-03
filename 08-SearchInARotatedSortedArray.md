## Explanation

This uses variations of binary search to:

* Find the location of the pivot in `find_pivot` 
* Find the location of the target in `rotated_array_search`

In a traditional binary search implementation the array is sorted.  However, this array is rotated on a pivot.  It is critcal to find the pivot to determine which side of the pivot the target will be on; left, right or equal to the pivot.  Further, arrays on either side of the pivot will be sorted.  Once you know what side of the pivot the target is on, you can use binary search on the approriate side of the pivot.  The time complexity of this solution is O(logn), because both functions leverage binary search.  The space complexity is independent of the input, the function is merely pointing to specific numbers in an existing array.


* Time Complexity: O(logn)
* Space Complexity: O(1)