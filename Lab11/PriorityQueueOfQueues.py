from PriorityQueue import PriorityQueue
from Queue import Queue

class PriorityQueueOfQueues:

    def __init__(self, number_of_queues):
        self.priority_queue = PriorityQueue()
        self.number_of_queues = number_of_queues
        self.dictionary_of_queues = {}

    def fill_queues(self, queue_sizes):
        for i in range(0, int(self.number_of_queues)):
            self.dictionary_of_queues['queue'+str(i+1)] = Queue()
            self.dictionary_of_queues['queue'+str(i+1)].id = 'queue'+str(i+1)
            for n in range(0, int(queue_sizes[i])):
                self.dictionary_of_queues['queue'+str(i+1)].enqueue('Line ' + str(i+1) + ' Person ' + str(n))
    
    def insert(self, queue_id, num_of_items):
        for i in range(self.dictionary_of_queues['queue'+queue_id].size(), self.dictionary_of_queues['queue'+queue_id].size() + num_of_items):
            self.dictionary_of_queues['queue'+queue_id].enqueue('Line ' + queue_id + ' Person ' + str(i))
        self.priority_queue.change_priority('queue'+queue_id, self.dictionary_of_queues['queue'+queue_id].size())


    def load_priority_queue(self):
        for queue in self.dictionary_of_queues:
            self.priority_queue.insert(self.dictionary_of_queues[queue], self.dictionary_of_queues[queue].size())
    
    def remove_one_item(self):
        removed = self.priority_queue.remove()
        removed_item = removed.dequeue()
        self.print_removed(removed, removed_item)
        if not removed.is_Empty():
                self.priority_queue.insert(removed, removed.size())
        return removed_item
   
    def remove_all_items(self):
        items = []
        while self.priority_queue.size > 0:
            removed = self.priority_queue.remove()
            removed_item = removed.dequeue()
            self.print_removed(removed, removed_item)
            items.append(removed_item)
            if not removed.is_Empty():
                self.priority_queue.insert(removed, removed.size())
        return items

    def print_removed(self, removed_queue, removed_item):
        print('Line ' + str(removed_queue) + ' has dequeued ' + str(removed_item))

    def print(self):
        print('There are ' + str(self.number_of_queues) + ' queues.')
