## Explanation

In the given examples and test cases, a pattern was identified:
* Each of the two digits start with the largest digit in the array
* Alternate the next largest digits to find the maxium sum

For example:
[1, 2, 3, 4, 5] would result in [531, 42], where 5 is the largest number in the array, followed by 4.  The next largest digit is 3, followed by 2.  These numbers are the succeeding numbers of 5 and 4 respecitively to create the largest sum.

After identifying the pattern, it became apparent that the list needed to be sorted.  The given expected time complexity of this function is O(nlog(n)).  To keep this within the time complexity bound, the quicksort algorithm is used to sort the input array.  From there the `rearrange_digits` function goes through each digit in the sorted array.  The time complexity of `rearrange_digits` is O(n) which is less than quicksort; the time complexity of this function is still O(nlogn).  The space complexity is independent of the input, the function is merely pointing to specific numbers and then generating a new array of two digits.


* Time Complexity: O(nlogn)
* Space Complexity: O(1)