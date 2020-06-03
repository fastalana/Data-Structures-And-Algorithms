# Data Structures and Algorithms
This repository includes answers to thirteen problems related to common data structures and algorithms.  Each problem includes:
* Description, included in this README file
* Solution, in the format of a Python file
* Explanation, included in a seperate README file linked [here](https://github.com/fastalana/Data-Structures-And-Algorithms/blob/master/Explanations.md), describing the efficiency of the code and the design choices.  

NOTE: Some problems can be solved without an algorithm or data structure.

## Project 1 - Least Recently Used Cache (LRU)
* [Solution](https://github.com/fastalana/Data-Structures/blob/master/01-LRUCache.py)

_Description:_

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

### Time and Space Complexity _Explanation_

## Project 2 - Finding Files
* [Solution](https://github.com/fastalana/Data-Structures/blob/master/02-FileRecursion.py)

_Description:_

Write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded [here](https://github.com/fastalana/Data-Structures/tree/master/testdir):
```
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
```

Python's os module will be useful—in particular, you may want to use the following resources:

* [os.path.isdir(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isdir)
* [os.path.isfile(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isfile)
* [os.listdir(directory)](https://docs.python.org/3.7/library/os.html#os.listdir)
* [os.path.join(...)](https://docs.python.org/3.7/library/os.path.html#os.path.join)

**Note:** `os.walk()` is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use `os.walk()`.

## Project 3 - Huffman Coding
* [Solution](https://github.com/fastalana/Data-Structures/blob/master/03-HuffmanCoding.py)

_Description:_

A **Huffman code** is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

#### Resources:
* [Huffman Visualization!](https://people.ok.ubc.ca/ylucet/DS/Huffman.html)
* [Tree Generator](http://huffman.ooz.ie/)

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

* Take a string and determine the relevant frequencies of the characters.
* Build and sort a list of tuples from lowest to highest frequencies.
* Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
* Trim the Huffman Tree (remove the frequencies from the previously built tree).
* Encode the text into its compressed form.
* Decode the text from its compressed form.

You then will need to create encoding, decoding, and sizing schemas.

## Project 4 - Active Directory
* [Solution](https://github.com/fastalana/Data-Structures/blob/master/04-ActiveDirectory.py)

_Description:_

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

Write a function that provides an efficient look up of whether the user is in a group.

## Project 5 - Block Chain
* [Solution](https://github.com/fastalana/Data-Structures/blob/master/05-BlockChain.py)

_Description:_

A [Blockchain](https://en.wikipedia.org/wiki/Blockchain) is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash, the [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a [blockchain implementation](https://github.com/fastalana/Data-Structures/blob/master/Blockchain.png).

## Project 6 - Union and Intersection of Two Linked Lists
* [Solution](https://github.com/fastalana/Data-Structures/blob/master/06-UnionAndIntersection.py)

_Description:_

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

## Problem 07 - Square Root of an Integer
* [Solution](https://github.com/fastalana/Problems-vs-Algorithms/blob/master/01-SquareRootOfAnInteger.py)

_Description:_

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

* For example if the given number is 16, then the answer would be 4.
* If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n)).

## Problem 08 - Search in a Rotated Sorted Array
* [Solution](https://github.com/fastalana/Problems-vs-Algorithms/blob/master/02-SearchInARotatedSortedArray.py)

_Description:_

You are given a sorted array which is rotated at some random pivot point.  Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].  You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example: 
* Input: nums = [4,5,6,7,0,1,2], target = 0 
* Output: 4

## Problem 09 - Rearrange Array Digits
* [Solution](https://github.com/fastalana/Problems-vs-Algorithms/blob/master/03-RearrangeArrayDigits.py)

_Description:_

Rearrange Array Elements so as to form two numbers such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the output numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

Example: [1, 2, 3, 4, 5, 6], The expected answer would be [642, 531].

## Problem 10 - Dutch National Flag Problem
* [Solution](https://github.com/fastalana/Problems-vs-Algorithms/blob/master/04-DutchNationalFlagProblem.py)

_Description:_

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

## Problem 11 - Autocomplete with Tries
* [Solution](https://github.com/fastalana/Problems-vs-Algorithms/blob/master/05-AutocompleteWithTries.py)

_Description:_

Using a Trie data strcuture, add the ability to list suffixes to implement an autocomplete feature. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

## Problem 12 - Unsorted Array Integer
* [Solution](https://github.com/fastalana/Problems-vs-Algorithms/blob/master/06-UnsortedArrayInteger.py)

_Description:_

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.  _Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?_

**Bonus Challenge:** Is it possible to find the max and min in a single traversal?

## Problem 13 - HTTP Router Using a Trie
* [Solution](https://github.com/fastalana/Problems-vs-Algorithms/blob/master/07-HTTPRouterUsingATrie.py)

_Description:_

For this exercise we are going to implement an HTTP Router like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content (handler) to return. In a dynamic web server, the content will often come from a block of code called a handler.

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's `SimpleHTTPRequestHandler` which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler.

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

`(root, None) -> ("about", None) -> ("me", "About Me handler")`

We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.  The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

* Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character
* Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.
* More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.