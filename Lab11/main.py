from PriorityQueue import PriorityQueue
from Queue import Queue
from PriorityQueueOfQueues import PriorityQueueOfQueues

num_of_queues = input("How many lines do you want to add? ")
queue_sizes = input("Enter the size of each queue you want to create: ").split()

q = PriorityQueueOfQueues(num_of_queues)
q.fill_queues(queue_sizes)
q.load_priority_queue()
q.print()
print(q.remove_all_items())
