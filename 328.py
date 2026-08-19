class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def oddeven(head):
    odd = head
    even = head.next
    evenhead = even
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = evenhead
    return head

def printnode(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

result = oddeven(head)
printnode(result)