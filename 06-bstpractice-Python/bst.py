class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        current = self.root
        while True:
            if new_val < current.value:
                if current.left == None:
                    current.left = Node(new_val)
                else:
                    current = current.left
            elif new_val > current.value:
                if current.value == None:
                    current.right = Node(new_val)
                else:
                    current = current.right
            else:
                break

    def printAll(self, current):
        if current == None:
            return
        print(current.value)
        self.printAll(current.left)
        self.printAll(current.right)

    def printSelf(self):
        # Your code goes here
        self.printAll(self.root)

    def search(self, find_val):
        # Your code goes here
        current = self.root
        while current != None:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                current = current.right
            else:
                current = current.left
        return False
