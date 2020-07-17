class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        if not isinstance(find_val, int):
            return False
        current = self.root
        while current != None:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                current = current.right
            else:
                current = current.left
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        self.preorder_print(self.root)
        self.preorder_print(self.root.right)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        pass

    def preorder_print(self, start):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        if start == None:
            return
        print(start.value)
        self.preorder_print(start.left)
        self.preorder_print(start.right)
