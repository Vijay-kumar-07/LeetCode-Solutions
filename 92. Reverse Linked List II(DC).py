# Question:

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        values = []                        # to stores the values that needed to be reverse
        nodes = []                         # to keep track of the nodes which needs to be reverse
        counter = 0
        curr = head
        while curr:
            counter += 1
            if counter >= left and counter <= right:
                values.append(curr.val)     #  | adding value and nodes in the list
                nodes.append(curr)          #  |
            curr = curr.next
        for node in nodes:
            node.val = values.pop(-1)       #  replace the value of nodes
        return head