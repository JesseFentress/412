from plistlib import InvalidFileException
from Stack import Stack
from Queue import Queue

def p_check(data): 
    stack = Stack()
    new = ""
    index = len(data) - 1
    for c in range(0, len(data)):
        if data[c].isalpha():
            stack.push(data[c])
    while stack.is_Empty() is False:   
        if data[index].isalpha():
            if stack.peek() == data[index]:
                stack.pop()
                index  = index - 1
            else:
                return False
        else:
            index = index - 1
    return True


print("Madam, I'm Adam: " + str(p_check("Madam, I'm Adam")))
print("racecar: " + str(p_check("racecar")))

def balanced_brackets(data):
    stack = Stack()
    stack.push(data[0])
    for c in range(1, len(data)):
        if (data[c] == "{" or data[c] == "[" or data[c] == "("):
            stack.push(data[c])
        else: 
            if stack.is_Empty() is False:
                top = stack.pop()
                match data[c]:
                    case "}":
                        if top != "{":
                            return False
                    case "]":
                        if top != "[":
                            return False
                    case ")":
                        if top != "(":
                            return False
            else:
                return False
    return True


print("{()]}: " + str(balanced_brackets("{()]}")))
print("([[]({{()}})]): " + str(balanced_brackets("([[]({{()}})])")))

queue = Queue()
print("Enqueue 1: " + str(queue.enqueue(1)))
print("Enqueue 2: " + str(queue.enqueue(2)))
print("Dequeue 1: " + str(queue.dequeue()))
print("Enqueue 3: " + str(queue.enqueue(3)))
print("Dequeue 2: " + str(queue.dequeue()))
print("is_Empty(): " + str(queue.is_Empty()))
print("Size: " + str(queue.size()))







