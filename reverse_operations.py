class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    dummy = Node(0)
    dummy.next = head

    prev, cur = dummy, head

    while cur:
        while cur and cur.data % 2 == 1:
            prev, cur = cur, cur.next
        p0 = prev
        c0 = cur
        while cur and cur.data % 2 == 0:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        p0.next = prev
        c0.next = cur
    return dummy.next