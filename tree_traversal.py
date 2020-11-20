# FB interview quesiton2:
class Node:
    def __init__(self, letter):
        self.left = None
        self.right = None
        self.data = letter

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)

    #         8  <------ root
    #        / \
    #      3    10
    #     / \     \
    #    1   6     14
    #       / \    /
    #      4   7  13


def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)


print(in_order(root)) # 1 3 4 6 7 8 10 13 14