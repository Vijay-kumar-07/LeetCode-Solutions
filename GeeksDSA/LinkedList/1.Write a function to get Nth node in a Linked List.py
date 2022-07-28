# Question:

# Write a GetNth() function that takes a linked list and an integer index and returns the data value stored in the node at that index position. 

# Input:  1->10->30->14,  index = 2
# Output: 30  
# The node at index 2 is 30

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def getNth(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        assert(False)
        return 0
        

if __name__ == '__main__':
    llist = LinkedList()
    value = [1,10,30,14]
    for i in reversed(value):
        llist.push(int(i))
    n = 2
    print(llist.getNth(n))