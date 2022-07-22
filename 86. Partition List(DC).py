# Question:

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

class ListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
        
class Linkedlist:
    def __init__(self, head=None):
        self.head = head
        
    def insert(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "-> ", end = "")
            currentNode = currentNode.nextNode
        print("None")

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(-1)
        large = ListNode(-1)
        small_head = small
        large_head = large
        
        while head:
            
            if head.val < x:
                small.next = head
                head = head.next
                small = small.next
                small.next = None
            
            else:
                large.next = head
                head = head.next
                large = large.next
                large.next = None
        
        small.next = large_head.next
        
        return small_head.next