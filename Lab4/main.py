import sys
from Sorter import Sorter
from random import randint
import json
import time
import timeit

l = []
for i in range(0, 9999):
    l.append(randint(0, 10000))
l.sort()

def binary_search_game(l):
    temp = l
    print("Size of 10000 int list: " + str(temp.__sizeof__()))
    while len(temp) > 0:
        user_input = input("Is your number: " + str(temp[len(temp) // 2]) + "? (Reply: Y/H/L)")
        print("Size of user input: " + str(user_input.__sizeof__()))
        if user_input == 'H' or user_input == 'h':
            temp = temp[len(temp)// 2:]
        elif user_input == 'L' or user_input == 'l':
            temp = temp[:len(temp) // 2]
        elif user_input == 'Y' or user_input == 'y':
            return "I guessed the number correctly!"
        else:
            user_input = input("Invalid input please enter (Y/H/L): ")
    return "I can't figure out the number!"


#print(binary_search_game(l))

file = open('students.json')
data = json.load(file)
sorter = Sorter()

'''start = timeit.default_timer()
print(sorter.selection_sort(data['students'], 'first_name'))
print("Elapsed Time (Selection Sort: First Name): " + str(timeit.default_timer() - start))
start = timeit.default_timer()
print(sorter.insertion_sort(data['students'], 'student_id'))
print("Elapsed Time (Insertion Sort: ID): " + str(timeit.default_timer() - start))
start = timeit.default_timer()
print(sorter.bubble_sort(data['students'], 'student_id'))
print("Elapsed Time (Bubble Sort: ID): " + str(timeit.default_timer() - start))
start = timeit.default_timer()
print(sorter.merge(data['students'], 'first_name'))
print("Elapsed Time (Merge Sort: First Name): " + str(timeit.default_timer() - start))
start = timeit.default_timer()
sorter.quick_sort(data['students'], 0, len(data['students']) - 1, 'first_name')
print("Elapsed Time (Quick Sort: First Name): " + str(timeit.default_timer() - start))'''

print(sys.getsizeof(data))
sorter.quick_sort(data['students'], 0, len(data['students']) - 1, 'student_id')
with open('new_students.json', 'w') as new_file:
    json.dump(data, new_file, indent=4, ensure_ascii=True)
