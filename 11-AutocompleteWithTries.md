## Explanation

This problem uses the trie data structure which is a type of tree.  The trie data structure offers a good payoff between time and space complexity.

To find suffixes, from a given prefix, we first call `find` on the Trie class to find the root node where the prefix exists. With the root node of the prefix, `suffixes` is called from the TrieNode class. Using recursion the function searches all children.  The time complexity is O(p+s), where `p` is the height of the nodes it takes to form the prefix and `s` is the numer of suffixes with the prefix.  The worst case space complexity of a triehappens when a word (or words) have no common characters between them leaving a node for each character. This would result in a space complexity of O(n).


* Time Complexity: O(p+s)
* Space Complexity: O(n)