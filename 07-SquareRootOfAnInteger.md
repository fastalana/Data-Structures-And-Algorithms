## Explanation

This problem could be solved with:
```
	if(number < 0):
         print("Negative number does not have a square root")
         return None
	return round(number**(1/2),0)
```

Or one could use a variation of the binary search algorithm with a complexity of O(logn).  The `sqrt` function takes the midpoint of the input number and tries to determine if the square of the midpoint is the original number.  The midpoint is adjusted by incrementing or decrementing the bounds around the midpoint until the square root is found.  The space complexity is independent of the input, the function is guessing specific numbers and only three integer variables are held in memory.


* Time Complexity: O(logn)
* Space Complexity: O(1)