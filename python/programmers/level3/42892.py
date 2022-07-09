import sys
sys.setrecursionlimit(10**6)


def solution(nodeinfo):
    dic = dict()
    for i, info in enumerate(nodeinfo, start=1):
        dic[tuple(info)] = i
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    tree = make_tree(nodeinfo, dic)

    return [tree.preorder([]), tree.postorder([])]


def make_tree(nodeinfo, dic):
    if not nodeinfo:
        return None

    root_x, root_y = nodeinfo.pop(0)
    root_number = dic[(root_x, root_y)]

    left, right = [], []
    for info in nodeinfo:
        if info[0] < root_x:
            left.append(info)
        else:
            right.append(info)
    return Tree(root_number, make_tree(left, dic), make_tree(right, dic))


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def preorder(self, values):
        values.append(self.value)
        if self.left is not None:
            self.left.preorder(values)
        if self.right is not None:
            self.right.preorder(values)
        return values

    def postorder(self, values):
        if self.left is not None:
            self.left.postorder(values)
        if self.right is not None:
            self.right.postorder(values)
        values.append(self.value)
        return values
