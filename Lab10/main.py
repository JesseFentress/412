from operator import indexOf
from random import randint
import timeit
from BST import BST
from BinaryTree import BinaryTree
from LinkedList import LinkedList
import uuid

values_list = []
list1 = []
dictionary1 = {}
binary_tree1 = BinaryTree()
binary_search_tree1 = BST()
linked_list1 = LinkedList()

for index in range(0,25000):
    values_list.append(randint(1, 10000))

def insert_list(values_list, list):
    start = timeit.default_timer()
    for item in values_list:
        list.append(item)
    return timeit.default_timer() - start

def insert_dictionary(values_list, dict):
    start = timeit.default_timer()
    for index in range(0, len(values_list) - 1):
        dict[index] = values_list[index]
    return timeit.default_timer() - start

def insert_binary_tree(values_list, bt):
    start = timeit.default_timer()
    for item in values_list:
        bt.insert(item)
    return timeit.default_timer() - start

def insert_binary_search_tree(values_list, bst):
    start = timeit.default_timer()
    for item in values_list:
        bst.insert(bst.root, item)
    return timeit.default_timer() - start

def insert_linked_list(values_list, ll):
    start = timeit.default_timer()
    for item in values_list:
        ll.append(item)
    return timeit.default_timer() - start

def find_list(target_number, list):
    for item in list:
        if item == target_number:
            return target_number
    return None


insert_list(values_list, list1)
insert_dictionary(values_list, dictionary1)
insert_binary_tree(values_list, binary_tree1)
insert_binary_search_tree(values_list, binary_search_tree1)
insert_linked_list(values_list, linked_list1)



# Print List
start = timeit.default_timer()
print(list1)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Print Dictionary
start = timeit.default_timer()
print(dictionary1)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Print Binary Tree
start = timeit.default_timer()
binary_tree1.inorder()
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Print Binary Search Tree
start = timeit.default_timer()
binary_search_tree1.inorder()
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Print LinkedList
start = timeit.default_timer()
linked_list1.print()
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()

random_retrieval_number = randint(1, 10000)

# Retrieve List
print('List Retrieval: ')
start = timeit.default_timer()
find_list(random_retrieval_number, list1)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Retrieve Dictionary
print('Dictionary Retrieval: ')
start = timeit.default_timer()
try:
    dictionary1[random_retrieval_number]
finally:
    print('Key not found')
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Retrieve Binary Tree
print('Binary Tree Retrieval: ')
start = timeit.default_timer()
binary_tree1.find(random_retrieval_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Retrieve Binary Search Tree
print('Binary Search Tree Retrieval: ')
start = timeit.default_timer()
binary_search_tree1.find(binary_search_tree1.root, random_retrieval_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Retrieve LinkedList
print('Linked List Retrieval: ')
start = timeit.default_timer()
linked_list1.find(random_retrieval_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()

random_insert_number = randint(1, 10000)

# Insert List
print('List Insert: ')
start = timeit.default_timer()
list1.append(random_insert_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Insert Dictionary
print('Dictionary Insert: ')
start = timeit.default_timer()
dictionary1[len(dictionary1)] = random_insert_number
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Insert Binary Tree
print('Binary Tree Insert: ')
start = timeit.default_timer()
binary_tree1.insert(random_insert_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Insert Binary Search Tree
print('Binary Search Tree Insert: ')
start = timeit.default_timer()
binary_search_tree1.insert(binary_search_tree1.root, random_insert_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Insert LinkedList
print('Linked List Insert: ')
start = timeit.default_timer()
linked_list1.append(random_insert_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


random_delete_number = randint(1, 10000)

# Delete List
print('List Delete: ')
start = timeit.default_timer()
list1.remove(random_insert_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Delete Dictionary
print('Dictionary Delete: ')
start = timeit.default_timer()
try:
    dictionary1.pop(random_delete_number)
finally:
    print('Key not found')
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Delete Binary Tree
print('Binary Tree Delete: ')
start = timeit.default_timer()
binary_tree1.remove(random_delete_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Delete Binary Search Tree
print('Binary Search Tree Delete: ')
start = timeit.default_timer()
binary_search_tree1.remove(binary_search_tree1.root, random_delete_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()


# Delete LinkedList
print('Linked List Delete: ')
start = timeit.default_timer()
linked_list1.delete(random_delete_number)
print('Elapsed Time: ' + str(timeit.default_timer() - start))
print()