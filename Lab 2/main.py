from Vector import Vector

vec = Vector()
vec2 = Vector()
vec.set_item(0, 13)
vec.set_item(1, 145)

print("Vector: " + str(vec.arr))
print("Vector length: " + str(vec.length()))
print()

print("Vector: " + str(vec.arr))
print("Vector item 0: " + str(vec.get_item(0)))
print()

print("Vector: " + str(vec.arr))
print("Vector extension: "  + str(vec.extend(vec2)))
print()

print("Vector: " + str(vec.arr))
print("Vector contains 100: " + str(vec.contains(100)))
print()

print("Vector set item at 2: ")
print("Before (" + str(vec.arr) + ")")
print("After: (" + str(vec.set_item(2, 79)) +")")
print()
print("Vector set item at 3: " + str(vec.set_item(3, 19)))

print("Vector item 2: " + str(vec.get_item(2)))
print()
print("Vector length: " + str(vec.length()))
print()

print("Vector insert at 1: ")
print("Before (" + str(vec.arr) + ")")
vec.insert(1, 35)
print("After (" + str(vec.arr) + ")")
print()

print("Vector set item at 2: ")
print("Before (" + str(vec.arr) + ")") 
print("After (" + str(vec.set_item(2, 88)) + ")")
print()

print("Vector remove at 2: ")
print("Before (" + str(vec.arr) + ")")
print("Removed: " + str(vec.remove(2)))
print("After (" + str(vec.arr) + ")")
print()

print("Vector append 9: ")
print("Before (" + str(vec.arr) + ")")
vec.append(9)
print("After (" + str(vec.arr) + ")")
print()

print("Subvector 1-3: " + str(vec.sub_vector(1, 3).arr))
print()

print("Vector index of 79: " + str(vec.index_of(79)))
