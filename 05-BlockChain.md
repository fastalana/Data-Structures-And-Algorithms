## Explanation

This problem was solved used a linked list.  Each new node points to the previous hash.  Each time a new node is added we add it to the end of the list.  However, if we keep track of the end of the list, which we do, the new block can be added directly to the end of the current blockchain making the complexity is O(1).