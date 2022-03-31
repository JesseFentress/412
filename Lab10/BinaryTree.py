import math
import sys

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self, data=None):
        self.root = Node(data)
    
    def insert(self, data):
        if self.root.data == None:
            self.root.data = data
        else:
            new_node = Node(data)
            self._insert(self.root, new_node)

    def _insert(self, node, new_node): 
        if not node:
            root = new_node
            return
        node_queue = [] # Holds nodes to visit
        node_queue.append(node) # Adds current node to queue
        while len(node_queue): # Continue while there are still nodes to visit
            node = node_queue[0] # Current node
            node_queue.pop(0) # Remove the current node from queue    
            if not node.left: # Insert new node at left if not there
                node.left = new_node
                break
            else:
                node_queue.append(node.left) # Add left to queue
            if not node.right: # Insert new node at right if not there
                node.right = new_node
                break
            else:
                node_queue.append(node.right) # Add right to queue

    def remove(self, data):
        if not self.root:
            return None
        else:
            return self.__remove(self.root, data)

    def remove_node(self, root, node):
        if not root: # Return if root is None
            return
        if root == node: # If root is the target node
            root = None # Set root to None
            return
        if root.left == node: # If the roots left child is target
            root.left = None # Set left to None
            return
        if root.right == node: # If the roots right child is target
            root.right = None # Set right to None
            return
        self.remove_node(root.left, node) # Remove from left sub tree
        self.remove_node(root.right, node) # Remove from right sub tree


    def __remove(self, root, data):
        if not root:
            return None
        if not root.left and not root.right: # If no children
            if root.data == data: # If root is the target
                root = None # Set root to none
                return root 
            return root # Return root if not the target
        node_queue = [] # Holds nodes to visit
        node_queue.append(root) # adds current root node
        found_node = None # Pointer for found node
        while len(node_queue): # Contine while there are still nodes to visit
            node = node_queue[0] # current node
            node_queue.pop(0) # Remove current node from the queue
            if node.data == data: #If the current node is target
                found_node = node
            if node.left: # Add left node to queue
                node_queue.append(node.left)
            if node.right: # Add right node to queue
                node_queue.append(node.right)
        if found_node: # If the target was found
            found_node.data = node.data # Get its value 
            self.remove_node(root, node) # Remove the found node
        return root # Return if not found
    
    def __traverse_right(self, node):
        if node.right == None:
            return node
        else:
            return self.__traverse_right(node.right)
    
    def find(self, data):
        if self.root.data == data:
            return self.root
        else:
            return self.__find(data, self.root)

    def __find(self, data, node):
        node_queue = [] # Holds nodes to visit
        node_queue.append(node) # Adds the current node to the queue
        while len(node_queue): # Continue while there are still nodes to visit
            node = node_queue[0] # Current node
            node_queue.pop(0) 
            if (node.data == data): # If the current node is correct node
                return node
            else:   
                if node.left: # Add left child node to queue
                    node_queue.append(node.left)
                if node.right: # Add right child node to queue
                    node_queue.append(node.right)
        return None # Target node was not found
               
    def min(self):
        if not self.root:
            return None
        else:
            return self.__min(self.root)         

    def __min(self, node):
        if not node:
            return
        min = node.data # Set min to current node data
        left_min = sys.maxsize # Base min for left
        right_min = sys.maxsize # Base min for right
        if node.left: # Find min value of left subtree
            left_min = self.__min(node.left) 
        if node.right: # Find mi value of right subtree
            right_min = self.__min(node.right)
        if min < left_min and min <  right_min:
            return min # Return current node as min
        elif left_min < min and left_min < right_min:
            return left_min # Return left min
        else:
            return right_min # Return right min

    def max(self):
        if not self.root:
            return None
        else:
            return self.__max(self.root)

    def __max(self, node):
        if not node:
            return
        max = node.data # Set max to current node data
        left_max = -(sys.maxsize) # Base max for left
        right_max = -(sys.maxsize) # Base max for right
        if node.left: # Find max value of left subtree
            left_max = self.__max(node.left)
        if node.right: # Fine max value of right subtree
            right_max = self.__max(node.right)
        if max > left_max and max > right_max:
            return max # Return current node as max
        elif left_max > max and left_max > right_max:
            return left_max # Return left max
        else:
            return right_max # Return right max

    def inorder(self):
        if self.root:
            self.__inorder(self.root)

    def __inorder(self, node):
        if node:
            self.__inorder(node.left) # Print left node first
            print(node.data, end=" ") # Print parent node
            self.__inorder(node.right) # Print right node
            
    def preorder(self):
        if self.root:
            self.__preorder(self.root)

    def __preorder(self, node):
        if node:
            print(node.data, end=" ") # Print parent node first
            self.__preorder(node.left) # Print left node
            self.__preorder(node.right) # Print right node         

    def postorder(self):
        if self.root:
            self.__postorder(self.root)

    def __postorder(self, node):
        if node:
            self.__postorder(node.left) # Print left node first
            self.__postorder(node.right) # Print right node
            print(node.data, end=" ") # Print parent node

    def merge(self, tree):
        if not self.root:
            self.root = tree.root
        else:
            # Count the number of nodes in the trees
            this_tree_size = self.size()
            new_tree_size = tree.size()
            # Use the number of of node to calculate the height
            # of the two trees (floor so only looking at level)
            this_tree_height = math.floor(math.log2(this_tree_size))
            new_tree_height = math.floor(math.log2(new_tree_size))
            if this_tree_height > new_tree_height:          
                self._insert(self.root, tree.root)
            elif new_tree_height > this_tree_height:
                tree._insert(tree.root, self.root)
                self.root = tree.root
            else: # Height is equal so add tree with more nodes to less
                if this_tree_size < new_tree_size:
                    self._insert(self.root, tree.root)
                else:
                    tree._insert(tree.root, self.root)
                    self.root = tree.root
    
    def size(self):
        if not self.root:
            return 0
        else:
            return self.__size(self.root)
            
    def __size(self, node):
        if not node:
            return 0
        else: # Count the number of nodes
            return (1 + self.__size(node.left) + self.__size(node.right))
    
    def print(self):
        node_queue = [] # Holds nodes to visit
        node_queue.append(self.root) # Adds the current node to the queue
        while len(node_queue): # Continue while there are still nodes to visit
            node = node_queue.pop()
            print(str(node.data), end=" ")
            if node.left: # Add left child node to queue
                node_queue.append(node.left)
            if node.right: # Add right child node to queue
                node_queue.append(node.right)
        return None # Target node was not found
