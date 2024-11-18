class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize root as None

    def insert(self, key):
        """Insert a new key into the BST"""
        if self.root is None:
            # If the tree is empty, create the root node
            self.root = Node(key)
        else:
            # Insert recursively starting from the root
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """Helper function to insert recursively"""
        if key < current_node.key:
            # Key should go to the left subtree
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            # Key should go to the right subtree
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        # If key == current_node.key, we do nothing to avoid duplicates

    def inorder_traversal(self):
        """Perform an inorder traversal to print the BST in sorted order"""
        def _inorder_recursive(node):
            if node:
                _inorder_recursive(node.left)
                print(node.key, end=" ")
                _inorder_recursive(node.right)

        _inorder_recursive(self.root)
        print()  # For newline after traversal




class Node:
    def __init__(self, key):
        self.key = key
        self.left = None  # Left child
        self.right = None  # Right child


class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize root as None

    def insert(self, key):
        """Insert a new key into the BST"""
        if self.root is None:
            # If the tree is empty, create the root node
            self.root = Node(key)
        else:
            # Insert recursively starting from the root
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """Helper function to insert recursively"""
        if key < current_node.key:
            # Key should go to the left subtree
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            # Key should go to the right subtree
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        # If key == current_node.key, we do nothing to avoid duplicates

    def inorder_traversal(self):
        """Perform an inorder traversal to print the BST in sorted order"""
        def _inorder_recursive(node):
            if node:
                _inorder_recursive(node.left)
                print(node.key, end=" ")
                _inorder_recursive(node.right)

        _inorder_recursive(self.root)
        print()  # For newline after traversal

    def preorder_traversl(self):
        """Perform an preorder traversal to print the BST in sorted order"""
        def _preorder_recursive(node):
            if node:
                print(node.key, end=" ")
                _preorder_recursive(node.left)
                _preorder_recursive(node.right)
        _preorder_recursive(self.root)
        print()
    
    def postorder_traversl(self):
        """Perform an postorder traversal to print the BST in sorted order"""
        def _postorder_recursive(node):
            if node:
                _postorder_recursive(node.left)
                _postorder_recursive(node.right)
                print(node.key, end=" ")
        _postorder_recursive(self.root)
        print()

    def delete(self,key):
        """Delete a key from BST"""
        self.root=self._delete_recursive(self.root, key)
    
    def _delete_recursive(self,node, key):
        if node is None:
            return node
        
        #Locate the node to delete
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        
        elif key> node.key:
            node.right = self._delete_recursive(node.right, key)
            
        else:
            #Case 1: Node with no children
            if node.left is  None and node.right is None:
                return None
            
            #Case 2: Node has only 1 child
            if node.left is None:
                return node.right
            
            elif node.right is None:
                return node.left
            
            #Case 3: Node with two children
            #Find the inorder sucessor(smallest in the right subtree)
            # Alternative is to find largest in the left subtree
            sucessor = self._find_min(node.right)
            node.key = sucessor.key
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, sucessor.key)

        return node
    
    def _find_min(self, node):
        """Find the node with the smallest key in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current


# Example usage
bst = BinarySearchTree()
keys = [15, 10, 20, 8, 12, 17, 25]  # Elements to insert

for key in keys:
    bst.insert(key)


print("Pre-order traversal of the BST after insertions:")
bst.preorder_traversl()

print("Post-order traversal of the BST after insertions:")
bst.postorder_traversl()

print("Inorder traversal of the BST after insertions:")
bst.inorder_traversal()  

# Delete cases
bst.delete(8)   # Leaf node
print("After deleting 8 (leaf node):")
bst.inorder_traversal()

bst.delete(10)  # Node with one child
print("After deleting 10 (one child):")
bst.inorder_traversal()

bst.delete(15)  # Node with two children
print("After deleting 15 (two children):")
bst.inorder_traversal()