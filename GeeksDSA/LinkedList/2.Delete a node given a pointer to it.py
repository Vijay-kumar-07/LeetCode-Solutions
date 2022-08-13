class Node:
    def __init__(self, val = None):
        self.data = val
        self.next = None
    
def push(head, val):
    newnode = Node(val)
    newnode.next = head.next
    head.next = newnode

def print_list(head):
    temp = head.next
    while (temp != None):
        print(temp.data, end = ' ')
        temp = temp.next
    print()

def delete_node(node):
    prev = Node()
    if (node == None):
        return
    else:
        while (node.next != None):
            node.data = node.next.data
            prev = node
            node = node.next
        prev.next = None

if __name__ == "__main__":
    head = Node()
    push(head, 2)
    push(head, 4)
    push(head, 3)
    push(head, 1)
    push(head, 29)
    push(head, 26)
    push(head, 35)
    print("List before deleting")
    print_list(head)

    delete_node(head.next.next)

    print("List after deleting")
    print_list(head)