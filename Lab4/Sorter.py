import sys

class Sorter:
    def __init__(self):
        s_size = 0
        i_size = 0
        b_size = 0
        m_size = 0
        q_size = 0

    def selection_sort(self, l, key):
        for item in range(len(l)):
            smallest = item
            for item2 in range(item + 1, len(l)):
                if l[item2][key] < l[smallest][key]:
                    smallest = item2
            l[item], l[smallest] = l[smallest], l[item]
        print("Selection Sort Size " + str(key) + " : " + str(sys.getsizeof(l) + sys.getsizeof(key) + sys.getsizeof(smallest)))
        return l

    def insertion_sort(self, l, key):
        for item in range(1, len(l)):
            value = l[item][key]
            while l[item - 1][key] > value and item > 0:
                l[item], l[item - 1] = l[item - 1], l[item]
                item = item - 1
        print("Insertion Sort Size " + str(key) + " : " + str(sys.getsizeof(l) + sys.getsizeof(key) + sys.getsizeof(value) + sys.getsizeof(item)))
        return l


    def bubble_sort(self, l, key):
        for item in range(len(l) - 1):
            for item2 in range(len(l) - 1 - item):
                if l[item2][key] > l[item2 + 1][key]:
                    l[item2], l[item2 + 1] = l[item2 + 1], l[item2]
        print("Bubble Sort Size " + str(key) + " : " + str(sys.getsizeof(l) + sys.getsizeof(key)))
        return l

    def merge_sort(self, l, r, key):
        temp = []
        left = right = 0
        while left < len(l) and right < len(r):
            if l[left][key] < r[right][key]:
                temp.append(l[left])
                left += 1
            else:
                temp.append(r[right])
                right += 1
        temp.extend(l[left:])
        temp.extend(r[right:])
        return temp      

    def merge(self, l, key):
        if len(l) == 1:
            return l
        return self.merge_sort(self.merge(l[:(len(l) // 2)], key), self.merge((l[(len(l) // 2):]), key), key)

    def swap(self, l, a, b, sum):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp
        sum = sum + sys.getsizeof(l) + sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(temp)
        return sum
        

    def partition(self, l, left, high, key, sum):
        pivot = l[high][key]
        right = high
        while left < right:
            while l[left][key] <= pivot and left < right:
                left = left + 1
            while l[right][key] >= pivot and left < right:
                right = right - 1
            sum = sum + self.swap(l, left, right, sum)
        sum = sum + self.swap(l, left, high, sum)
        return left

    def quick_sort(self, l, low, high, key, sum):
        if low > high:
            return
        pivot = self.partition(l, low, high, key, sum)
        sum = sum + sys.getsizeof(pivot) + sys.getsizeof(high) + sys.getsizeof(low) + sys.getsizeof(l) + sys.getsizeof(key)
        self.quick_sort(l, low, pivot - 1, key, sum)
        self.quick_sort(l, pivot + 1, high, key, sum)
        return sum
        


