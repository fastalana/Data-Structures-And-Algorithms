class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        else: 
            pass
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        if len(self.children) == 0:
            return results
        
        for character in self.children:
            results.extend(self.children[character].suffixes(suffix=suffix+character))

        return results
        
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
                
        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        
        for character in prefix:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        
        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print("ANT has the following suffixes: ", MyTrie.find('ant').suffixes())
# ['hology', 'agonist', 'onym']

print("TRI has the following suffixes: ", MyTrie.find('tri').suffixes())
# ['e', 'gger', 'gonometry', 'pod']

print("FUN has the following suffixes: ", MyTrie.find('fun').suffixes())
# ['ction']

print("No character has the following suffixes: ", MyTrie.find('').suffixes())
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 
#  'trie', 'trigger', 'trigonometry', 'tripod']