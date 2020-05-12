import sys

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self, root):
        self.root = root
        
# take a string (data) and determine the relevant frequencies of the characters
def character_frequencies(data):
    character_frequency_dict = {}
    for a in data:
        if a not in character_frequency_dict:
            character_frequency_dict[a] = 1
        else:
            character_frequency_dict[a] += 1
               
    return(character_frequency_dict)

# build and sort a list of tuples from lowest to highest frequencies
def sort_character_frequencies(data):
    items = list(data.items())
    items.sort(key=lambda x : x[1])
    return items
        
def encode_tree(root, string, encoded_characters):
    if(root.right is None and root.left is None):
        encoded_characters[root.key] = string
    else:
        if root.left is not None:
            encode_tree(root.left, string + "0", encoded_characters)
        if root.right is not None:
            encode_tree(root.right, string + "1", encoded_characters)
            
def insert_element_into_list(node, mapped_sorted_frequencies):
    for index, element in enumerate(mapped_sorted_frequencies):
        if node.value < element.value:
            mapped_sorted_frequencies.insert(index, node)
            break
        elif index == len(mapped_sorted_frequencies) - 1:
            mapped_sorted_frequencies.append(node)
            break
            
# build the Huffman Tree by assigning a binary code to each letter           
def huffman_encoding(data):
    if not data:
        return data, None
    else:
        frequencies = character_frequencies(data)
        sorted_frequencies = sort_character_frequencies(frequencies)
        
        # Create a Node object that includes a key value pair, but make it a list so we maintain the order
        mapped_sorted_frequencies = list( 
            map(lambda x: Node(x[0], x[1]), sorted_frequencies))
        
        tree = None
        
        while len(mapped_sorted_frequencies) > 1:
            # trim the Huffman Tree, i.e. remove the frequencies from the previously built tree
            first_item = mapped_sorted_frequencies.pop(0)
            second_item = mapped_sorted_frequencies.pop(0)
            root_node = Node(first_item.value + second_item.value, first_item.value + second_item.value)
            root_node.left = first_item
            root_node.right = second_item
            # insert the root node into the mapped_sorted_frequencies list
            insert_element_into_list(root_node, mapped_sorted_frequencies) 
            if len(mapped_sorted_frequencies) == 0:
                tree = Tree(root_node)
                
        if tree is None:
            if len(mapped_sorted_frequencies) == 1:
                first_item = mapped_sorted_frequencies.pop(0)
                tree = Tree(Node(first_item.value, first_item.value))
                tree.root.left = Node(first_item.key, first_item.value)
                
        encoded_characters = dict()
        encoded_string = ""
        encode_tree(tree.root, "", encoded_characters)
        for character in data:
            encoded_string += encoded_characters[character]
        return tree, encoded_string

def huffman_decoding(data, root):
    if root is None:
        return data, None
    
    def decode(data, root, index, decode_string):
        if root.left is None and root.right is None:
            decode_string += root.key
            return index, decode_string
        elif data[index] == "0":
            return decode(data, root.left, index + 1, decode_string)
        else:
            return decode(data, root.right, index + 1, decode_string)
        
    index = 0
    decode_string = ""
    while(index <= len(data) - 1):
        index, decode_string = decode(data, root, index, decode_string)
        
    return decode_string

def run_tests(string):
    print ("The content of the data is: {}\n".format(string))
    print ("The size of the data is: {}\n".format(sys.getsizeof(string)))
    
    
    tree, encoded_data = huffman_encoding(string)
    
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    if encoded_data == None:
        print("This is an empty string and cannot be encoded.")
    else:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))


        decoded_data = huffman_decoding(encoded_data, tree.root)

        print ("The content of the decoded data is: {}\n".format(decoded_data))
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

if __name__ == "__main__":
    codes = {}
    
    # Test 1, one character
    run_tests("a")
    # The content of the data is: a
    # The size of the data is: 50
    # The content of the encoded data is: 0
    # The size of the encoded data is: 24
    # The content of the decoded data is: a
    # The size of the decoded data is: 50
    
    # Test 2, multiples of the same character
    run_tests("aaa")
    # The content of the data is: aaa
    # The size of the data is: 52
    # The content of the encoded data is: 000
    # The size of the encoded data is: 24
    # The content of the decoded data is: aaa
    # The size of the decoded data is: 52
    
    # Test 3, a simple string
    run_tests("apple")
    # The content of the data is: apple
    # The size of the data is: 54
    # The content of the encoded data is: 0011110110
    # The size of the encoded data is: 28
    # The content of the decoded data is: apple
    # The size of the decoded data is: 54

    # Test 4, an empty string
    run_tests("")
    # The content of the data is: 
    # The size of the data is: 49
    # The content of the encoded data is: None
    # This is an empty string and cannot be encoded.

    # Test 5, a simple sentence
    run_tests("The bird is the word.")
    # The content of the data is: The bird is the word.
    # The size of the data is: 70
    # The content of the encoded data is: 0100101111101100101111100000111011110110110011110111110110100010010000011010
    # The size of the encoded data is: 36
    # The content of the decoded data is: The bird is the word.
    # The size of the decoded data is: 70