import sys
sys.setrecursionlimit(10 ** 4)

class Node:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            if key < p.key:
                p = p.left
            if key > p.key:
                p = p.right
    
    def add(self, key, value):
        
        def add_node(node, key, value):
            if node.key == key:
                return False
            if node.key < key:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            if node.key > key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
        else:
            add_node(self.root, key, value)
    
    def preorder(self):

        def pre(node):
            print(node.key)
            if node.left:
                pre(node.left)
            if node.right:
                pre(node.right)
            return

        if self.root:
            pre(self.root)
    
    def postorder(self):

        def post(node):
            if node.left:
                post(node.left)
            if node.right:
                post(node.right)
            print(node.key)
            return

        if self.root:
            post(self.root)

btree = BinarySearchTree()

while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        btree.add(n, n)
    except:
        break

# btree.preorder()
btree.postorder()