## Explanation

This problem uses the trie data structure which is a type of tree.  The trie data structure offers a good payoff between time and space complexity.

The RouteTrieNode and RouteTrie is very similar to a regular TrieNode and Trie with the exception of adding a handler in the RouteTrieNode. In the `Router` function, routes are initialized with a `RouteTrie`, adding a "/" root route and a `not found handler`. To add a handler or lookup a route, call the RouteTrie `insert` and `find` passing a list of paths with the back slash removed.

The complexity of this function is similar to a traditional trie; O(k).  For this function 'k' is the length of the path between back slashes.  Ex: /home, k=1, whereas /home/about k=2.  The worst case space complexity of a triehappens when a word (or words) have no common characters between them leaving a node for each character. This would result in a space complexity of O(n).  In this case the space complexity would still be the same with the caveat that every route is just one word; i.e. /home, /contact, /about, etc.


* Time Complexity: O(k)
* Space Complexity: O(n)