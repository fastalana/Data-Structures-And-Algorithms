# Data Structures
This repository includes answers to six questions related to the data structures.  Each answer includes Python file, as well as an introduction to the problem and an explanation about the efficiency of the code and the design choices.

## Project 1 - Least Recently Used Cache (LRU)
The lookup operation (i.e., `get()`) and `put()` / `set()` is supposed to be fast for a cache memory.

While doing the `get()` operation, if the entry is found in the cache, it is known as a `cache hit`. If, however, the entry is not found, it is known as a `cache miss`.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the `put()` operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a **Least Recently Used (LRU) cache**. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both `get` and `set` operations as an `use operation`.

Use an appropriate data structure(s) to implement the cache.

* In case of a `cache hit`, your `get()` operation should return the appropriate value.
* In case of a `cache miss`, your `get()` should return -1.
* While putting an element in the cache, your `put()` / `set()` operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.

All operations must take `O(1)` time.

For the current problem, you can consider the `size of cache = 5`. 

### Time and Space complexity
_Explanation_
