import hashlib
import datetime

class Block:
    def __init__(self, data, timestamp, previous_hash):
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data) # no argument 
        self.next = None # no argument 
        
    def calc_hash(self, data):
        sha = hashlib.sha256()
        sha.update(data.encode('utf-8'))
        return sha.hexdigest()
    
class Blockchain:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        """ Appends a value to the end of the list. """
        if self.head is None:
            block = Block(data, datetime.datetime.utcnow(), None)
            self.head = block
            return
        
        # assign a variable to the head so we can keep track of the location of self.head
        node = self.head
        while node.next:
            node = node.next
        node.next = Block(data, datetime.datetime.utcnow(), node.hash)

# Tests
new_blockchain = Blockchain()

new_blockchain.append("Data A")
new_blockchain.append("Data B")
new_blockchain.append("Data C")

a = new_blockchain.head
b = new_blockchain.head.next
c = new_blockchain.head.next.next

# Recreate the blockchain, implementation linked above
print("BLOCK 0:")
print("Timestamp: ", a.timestamp)
print("Data: ", a.data)
print("SHA256 Hash:", a.hash)
print("Previous Hash:", a.previous_hash)


print("BLOCK 1:")
print("Timestamp: ", b.timestamp)
print("Data: ", b.data)
print("SHA256 Hash:", b.hash)
print("Previous Hash:", b.previous_hash)

print("BLOCK 2:")
print("Timestamp: ", c.timestamp)
print("Data: ", c.data)
print("SHA256 Hash:", c.hash)
print("Previous Hash:", c.previous_hash)

# Check to make sure previous_hashes are correct
print(a.hash == b.previous_hash)
# True

print(b.hash == c.previous_hash)
# True