## Explanation

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
