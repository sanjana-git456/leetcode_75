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
    while even and even.next:
        even.next = even.next.next
        odd.next = odd.next.next
    return head