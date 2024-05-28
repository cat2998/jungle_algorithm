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
        # node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            elif key > node.key:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)