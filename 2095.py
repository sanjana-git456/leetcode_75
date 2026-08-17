class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle(head):
    if head.next == None:
        return None
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    slow.next = None
    return head

def printnode(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = middle(head)
printnode(result)