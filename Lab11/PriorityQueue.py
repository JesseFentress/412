class PriorityQueue:

    def __init__(self):
        self.heap = [[None, None]]
        self.size = 0
    
    def parent(self, index):
        return index / 2

    def left(self, index):
        return 2 * index

    def right(self, index):
        return 2 * index + 1

    def heapify(self, index):
        l = self.left(index)
        r = self.right(index)
        if l <= self.size and self.heap[l][1] > self.heap[index][1]:
            largest = l
        else:
            largest = index
        if r <= self.size and self.heap[r][1] > self.heap[largest][1]:
            largest = r
        if largest != index:
            self.swap(index, largest)
            self.heapify(largest)
    
    def insert(self, item, priority):
        self.size += 1
        self.heap.append([item, priority])
        current_position = self.size
        while current_position > 1 and self.heap[int(self.parent(current_position))][1] < self.heap[current_position][1]:
            self.swap(current_position, int(self.parent(current_position)))
            current_position = int(self.parent(current_position))
    
    def peek(self):
        return self.heap[1][0]
    
    def remove(self):
        if self.size < 1:
            return "Empty queue"
        temp = self.heap[1][0]
        self.heap[1] = self.heap[self.size]
        self.heapify(1)
        self.size -= 1
        self.heap.pop()
        return temp

    def change_priority(self, item, priority):
        index = 0
        for i in range(1, self.size):
            if self.heap[1][0] == item:
                index = i
                break
        if priority < self.heap[index][1]:
            return
        else:
            self.heap[index][1] = priority
            while index > 1 and self.heap[self.parent(index)][1] < self.heap[index][1]:
                self.swap(index, self.parent(index))
                index = int(self.parent(index))
        
    def build_heap(self):
        length = len(self.heap)
        for i in range(length / 2, 1, -1):
            self.heapify(i)

    def heapsort(self):
        self.build_heap
        for i in range(self.size, 2, -1):
            self.swap(1, i)
            self.size = self.size - 1
            self.heapify(1)
        return self.heap
    
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp        
