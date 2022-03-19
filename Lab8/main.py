from BST import BST
from Student import Student
import csv
import json


file = open('students.json')
data = json.load(file)
data = data['students']


file = open('students.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(Student(row))
file.close


bst = BST()
print("Empty BST:")
bst.inorder()
print("Create BST from students:")
bst.create_bst(rows)
bst.inorder()
print()

#bst.remove(bst.root, '34234')
print(bst.inorder())


print("Find ID 123:")
print(bst.find(bst.root, '123'))
print("Find ID 56387")
print(bst.find(bst.root, '56387'))

print("Insert new student 29999")
bst.insert(bst.root, Student(['29999', 'sf', 'sf', 'sd', 'sf']), 'students.csv')

print("Is BST")
print(bst.is_bst(bst.root))


