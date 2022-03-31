from csv import writer


class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None
        self.size  = 0

    def insert(self, node, data, file_url):
        if not self.root: # BST is empty
            self.root = Node(data)
            self.__db_insert(data.get_all(), file_url)
        elif node.data.get_id() >= data.get_id(): # Go left
            if not node.left: # If current node's left is empty
                node.left = Node(data)
                self.__db_insert(data.get_all(), file_url)
            else: # Insert into left subtree
                self.insert(node.left, data, file_url)
        else: # Go right
            if not node.right: # If current node's right is empty
                node.right = Node(data)
                self.__db_insert(data.get_all(), file_url)
            else: # Insert into right subtree
                self.insert(node.right, data, file_url)
        self.size += 1 # Increase size attribute

    def __db_insert(self, data, file_url):
        with open(file_url, 'a', newline='') as file: # Keep file open in append mode
            file_writer = writer(file) # File writer
            file_writer.writerow(data) # Write the file with new student data
            file.close() # Close file

    
    def remove(self, node, target, file_url):
        if not node:
            return node
        else:
            if node.data.get_id() < target:
                node.right = self.remove(node.right, target)
            elif node.data.get_id() > target:
                node.left = self.remove(node.left, target)
            else:
                if node.left and node.right:
                    temp = self.find_min_node(node.right)
                    node.data = temp.data
                    node.right = self.remove(node.right, temp.data.get_id())
                else:
                    if not node.left:
                        temp = node.right
                        node = None
                        return temp
                    else:
                        temp = node.left
                        node = None
                        return temp
            return node


    def find_min_node(self, node):
        if not node.left:
            return node
        else:
            return self.find_min_node(node.left)

    def __insert(self, node, data):
        if not self.root: # BST is empty
            self.root = Node(data)
        elif node.data.get_id() >= data.get_id(): # Go left
            if not node.left: # If current node's left is empty
                node.left = Node(data)
            else: # Insert into left subtree
                self.__insert(node.left, data)
        else: # Go right
            if not node.right: # If current node's right is empty
                node.right = Node(data)
            else: # Insert into right subtree
                self.__insert(node.right, data)
        self.size += 1 # Increase size attribute

    def create_bst(self, list):
        for item in list:
            self.__insert(self.root, item)

    def is_bst(self, tree):
        if not tree: # BST is empty
            return
        else:
            if tree.left != None and tree.left.data.get_id() > tree.data.get_id():
                return False # If left child is > parent
            if tree.right != None and tree.right.data.get_id() < tree.data.get_id():
                return False # If right child is < parent
            if self.is_bst(tree.left) == False or self.is_bst(tree.right) == False:
                return False
            return True 


    def find(self, node, target):
        if node.data.get_id() == target: # Student is found
            return node # Return node that contains the student
        elif node.data.get_id() >= target and node.left: # Traverse left
            return self.find(node.left, target)
        elif node.data.get_id() < target and node.right: # Traverse right
            return self.find(node.right, target)
        else:
            return None # student not found


    def inorder(self):
        if self.root:
            self.__inorder(self.root)

    def __inorder(self, node):
        if node:
            self.__inorder(node.left) # Print left node first
            print(node.data.get_all(), end=" ") # Print parent node
            self.__inorder(node.right) # Print right node
