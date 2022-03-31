class LLNode:

    def __init__(self, data, tail=None):
        self.data = data
        self.tail = tail

class LinkedList:

    def __init__(self, node=None):
        self.head = node
        self.last = node
        self.size = 0

    def append(self, new_data):
        if not self.head:
            self.head = LLNode(new_data)
        else:
            self.last.tail = LLNode(new_data)
            self.last = self.last.tail
    
    def delete(self, target_data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                if current_node == self.head:
                    self.head = current_node.tail
                    current_node.tail = None
                elif current_node == self.tail:
                    previous_node.tail = None
                    self.last = previous_node
                else:
                    previous_node.tail = current_node.tail
                    current_node.tail = None
                return current_node.data
            else:
                previous_node = current_node
                current_node = current_node.tail
        return None
    
    def find(self, target_data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                return current_node
            current_node = current_node.tail
        return None
    
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            
        