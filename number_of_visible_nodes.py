def left_view(root, level, max_level):
    count = 0
    if root is None:
        return count

    if max_level[0] < level:
        count = 1
        max_level[0] = level

    count += left_view(root.left, level+1, max_level)
    count += left_view(root.right, level+1, max_level)

    

    return count


def visible_node(root):
    max_level = [0]

    return left_view(root, 1, max_level)