# Data Structures
This repository includes answers to six questions related to data structures.  Each problem includes a Python file with the solution, as well as an introduction to the problem and an explanation about the efficiency of the code and the design choices.

## Project 1 - Least Recently Used Cache (LRU)
* [Solution](https://github.com/fastalana/Data-Structures/blob/master/01-LRUCache.py)
* [Explanation](https://github.com/fastalana/Data-Structures/blob/master/01-LRUCache.md)

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
* [Explanation](https://github.com/fastalana/Data-Structures/blob/master/02-FileRecursion.md)

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
* [Explanation](https://github.com/fastalana/Data-Structures/blob/master/03-HuffmanCoding.md)

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
* [Explanation](https://github.com/fastalana/Data-Structures/blob/master/04-ActiveDirectory.md)

_Description:_
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

Write a function that provides an efficient look up of whether the user is in a group.

## Project 5 - Block Chain
* [Solution](https://github.com/fastalana/Data-Structures/blob/master/05-BlockChain.py)
* [Explanation](https://github.com/fastalana/Data-Structures/blob/master/05-BlockChain.md)

_Description:_
A [Blockchain](https://en.wikipedia.org/wiki/Blockchain) is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash, the [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a [blockchain implementation](https://github.com/fastalana/Data-Structures/blob/master/Blockchain.png).

## Project 6 - Union and Intersection of Two Linked Lists
* [Solution](https://github.com/fastalana/Data-Structures/blob/master/06-UnionAndIntersection.py)
* [Explanation](https://github.com/fastalana/Data-Structures/blob/master/06-UnionAndIntersection.md)

_Description:_
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.