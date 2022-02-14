import array


class Vector:

    def __init__(self):
        self.arr = array.array('i', [0, 0])
    
    def length(self):
        return len(self.arr)

    def contains(self, item):
        return item in self.arr

    def get_item(self, ndx):
        if ndx <= self.length():
            return self.arr[ndx]
        else:
            return None

    def set_item(self, ndx, item):
        if ndx <= self.length() - 1:
            self.arr[ndx] = item
            return self.arr
        elif ndx == self.length():
            self.append(item)
            return self.arr
        else:
           return None

    def append(self, item):
        return self.arr.append(item)

    def insert(self, ndx, item):
        return self.arr.insert(ndx, item)
                
    def remove(self, ndx):
        return self.arr.pop(ndx)

    def index_of(self ,item):
        for items in range(self.length() - 1):
            if self.arr[items] == item:
                return items
        return None

    def extend(self, other_vector):
        self.arr = self.arr + other_vector.arr
        return self.arr

    def sub_vector(self, fro, to):
        sub = Vector()
        index = 0
        while fro <= to and to < self.length():
            sub.set_item(index, self.arr[fro])
            fro += 1
            index += 1
        return sub



