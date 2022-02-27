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

    def __remove(self, root, data):
        node = self.find(data) 
        if node:
            if node.left and node.right:
                temp = self.__traverse_right(node.right)
                node.data = temp.data
                node.right = self.__remove(node.right, temp)
                return
            else:
                if node.left:
                    temp = node.left
                    node = None
                    print(str(temp) + ' 233421edsadasda')
                    return temp
                else:
                    temp = node.left
                    print(str(temp) + ' FSDFSDFSFS')
                    node = None
                    return temp
            print(str(temp.data) + ' 234fads')
            return node.data
    
    def __traverse_right(self, node):
        if not node.right:
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
        if not root:
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
            left_max = self.__min(node.left) 
        if node.right: # Find mi value of right subtree
            right_max = self.__min(node.right)
        if min < left_min and min <  right_min:
            return min # Return current node as min
        elif left_min < min and left_min < right_min:
            return left_min # Return left min
        else:
            return right_min # Return right min

    def max(self):
        if not root:
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
            print(node.data) # Print parent node
            self.__inorder(node.right) # Print right node
            
    def preorder(self):
        if self.root:
            self.__preorder(self.root)

    def __preorder(self, node):
        if node:
            print(node.data) # Print parent node first
            self.__preorder(node.left) # Print left node
            self.__preorder(node.right) # Print right node         

    def postorder(self):
        if self.root:
            self.__postorder(self.root)

    def __postorder(self, node):
        if node:
            self.__postorder(node.left) # Print left node first
            self.__postorder(node.right) # Print right node
            print(node.data) # Print parent node

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
