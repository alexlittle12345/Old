
nodeList = []

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        nodeList.append(self)


class BST:
    def __init__(self, node):
        self.root = node
    
    def insert(self, node):
        if node.val < self.root.val:
            if self.root.left is None:
                self.root.left = node
            else:
                self.root.left.insert(BST(node))
        else:
            if self.root.right is None:
                self.root.right = node
            else:
                self.root.right.insert(BST(node))



n1 = Node(20)
n2 = Node(10)
n3 = Node(5)
n4 = Node(6)

B = BST(n1)
B.insert(n2)
B.insert(n3)
B.insert(n4)


print (n1.left.val)
