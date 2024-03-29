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
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
data10 = []
for item in data['students']:
    data1.append(item)
    data2.append(item)
    data3.append(item)
    data4.append(item)
    data5.append(item)
    data6.append(item)
    data7.append(item)
    data8.append(item)
    data9.append(item)
    data10.append(item)
    

sorter = Sorter()

# Selection Sort
# ID
start = timeit.default_timer()
sorter.selection_sort(data1, 'student_id')
print("Elapsed Time (Selection Sort: ID): " + str(timeit.default_timer() - start))
# First Name
start = timeit.default_timer()
sorter.selection_sort(data2, 'first_name')
print("Elapsed Time (Selection Sort: First Name): " + str(timeit.default_timer() - start))


# Insertion Sort
# ID
start = timeit.default_timer()
sorter.insertion_sort(data3, 'student_id')
print("Elapsed Time (Insertion Sort: ID): " + str(timeit.default_timer() - start))
# First Name
start = timeit.default_timer()
sorter.insertion_sort(data4, 'first_name')
print("Elapsed Time (Insertion Sort: FirstName): " + str(timeit.default_timer() - start))

# Bubble Sort
# ID
start = timeit.default_timer()
sorter.bubble_sort(data5, 'student_id')
print("Elapsed Time (Bubble Sort: ID): " + str(timeit.default_timer() - start))
# First Name
start = timeit.default_timer()
sorter.bubble_sort(data6, 'first_name')
print("Elapsed Time (Bubble Sort: First Name): " + str(timeit.default_timer() - start))

# Merge Sort
# ID
start = timeit.default_timer()
sorter.merge(data7, 'student_id')
print("Elapsed Time (Merge Sort: ID): " + str(timeit.default_timer() - start))
# First Name
start = timeit.default_timer()
sorter.merge(data8, 'first_name')
print("Elapsed Time (Merge Sort: First Name): " + str(timeit.default_timer() - start))

# Quick Sort
# ID
start = timeit.default_timer()
sorter.quick_sort(data9, 0, len(data9) - 1, 'student_id', 0)
print("Elapsed Time (Quick Sort: ID): " + str(timeit.default_timer() - start))
#First Name
start = timeit.default_timer()
sorter.quick_sort(data10, 0, len(data10) - 1, 'first_name', 0)
print("Elapsed Time (Quick Sort: First Name): " + str(timeit.default_timer() - start))

print(sys.getsizeof(data1))
print(sys.getsizeof("first_name"))


'''sorter.quick_sort(data['students'], 0, len(data['students']) - 1, 'student_id')
with open('new_students.json', 'w') as new_file:
    json.dump(data, new_file, indent=4, ensure_ascii=True)'''
