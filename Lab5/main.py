from BinaryTree import BinaryTree, Node
import math

bt = BinaryTree(1)
bt.insert(5)
bt.insert(6)
bt.insert(10)
bt.insert(2)
bt.insert(56)
bt.insert(12)
bt.insert(107)
bt.insert(8)
bt.insert(27)

print()
print("Remove 1")
bt.remove(1)
bt.print()
print()
print()
bt.insert(99)
bt.insert(21)
bt2 = BinaryTree(23)
bt2.insert(7)
bt2.insert(16)
bt2.insert(8)
bt2.insert(4)
bt2.insert(88)
bt2.insert(72)

bt2.print()
print()
bt.print()
print()
print("Merge two trees")
bt.merge(bt2)
bt.print()
print()
print()

print("Find")
print(bt.find(88))
print()

print("Inorder")
bt.inorder()
print()

print("Postorder")
bt.postorder()
print()

print("Preorder")
bt.preorder()
print()

print("Max")
print(bt.max())
print()

print("Min")
print(bt.min())
print()




