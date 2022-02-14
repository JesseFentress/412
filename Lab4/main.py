import sys
from Sorter import Sorter
from random import randint
import json

l = []
for i in range(0, 9999):
    l.append(randint(0, 10000))
l.sort()

def binary_search_game(l):
    temp = l
    print(temp.__sizeof__())
    while len(temp) > 0:
        input1 = input("Is your number: " + str(temp[len(temp) // 2]) + "? (Reply: Y/H/L)")
        if input1 == 'H' or input1 == 'h':
            temp = temp[len(temp)// 2:]
            print(len(temp))
        elif input1 == 'L' or input1 == 'l':
            temp = temp[:len(temp) // 2]
            print(len(temp))
        elif input1 == 'Y' or input1 == 'y':
            return "I guessed the number correctly!"
        else:
            input1 = input("Invalid input please enter (Y/H/L): ")
    return "I can't figure out the number!"


print(binary_search_game(l))

file = open('students.json')
data = json.load(file)

sorter = Sorter()
#print(sorter.selection_sort(data['students'], 'last_name'))
#print(sorter.insertion_sort(data['students'], 'student_id'))
#print(sorter.bubble_sort(data['students'], 'student_id'))
#print(sorter.merge(data['students'], 'first_name'))
sorter.quick_sort(data['students'], 0, len(data['students']) - 1, 'student_id')
print(data)
