import sys

class Sorter:

    def selection_sort(self, l, key):
        for item in range(len(l)):
            smallest = item
            for item2 in range(item + 1, len(l)):
                if l[item2][key] < l[smallest][key]:
                    smallest = item2
            l[item], l[smallest] = l[smallest], l[item]
        return l

    def insertion_sort(self, l, key):
        for item in range(1, len(l)):
            value = l[item][key]
            while l[item - 1][key] > value and item > 0:
                l[item], l[item - 1] = l[item - 1], l[item]
                item = item - 1
            print("ins (value)" + str(sys.getsizeof(value)))
        print("ins (l)" + str(sys.getsizeof(l)))
        print("ins (key)" + str(sys.getsizeof(key)))
        return l


    def bubble_sort(self, l, key):
        for item in range(len(l) - 1):
            for item2 in range(len(l) - 1 - item):
                if l[item2][key] > l[item2 + 1][key]:
                    l[item2], l[item2 + 1] = l[item2 + 1], l[item2]
        print("bubble (l)" + str(sys.getsizeof(l)))
        print("bubble (key)" + str(sys.getsizeof(key)))
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
        print("ms (l)" + str(sys.getsizeof(l)))
        print("ms (r)" + str(sys.getsizeof(l)))
        print("ms (key)" + str(sys.getsizeof(l)))
        print("ms (temp)" + str(sys.getsizeof(temp)))
        return temp      

    def merge(self, l, key):
        if len(l) == 1:
            return l
        print("merge (l)" + str(sys.getsizeof(l)))
        print("merge (key)" + str(sys.getsizeof(key)))
        return self.merge_sort(self.merge(l[:(len(l) // 2)], key), self.merge((l[(len(l) // 2):]), key), key)

    def swap(self, l, a, b):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp
        print("swap (l)" + str(sys.getsizeof(l)))
        print("swap (a)" + str(sys.getsizeof(a)))
        print("swap (b)" + str(sys.getsizeof(b)))
        print("swap (temp)" + str(sys.getsizeof(temp)))

    def partition(self, l, left, high, key):
        pivot = l[high][key]
        right = high
        while left < right:
            while l[left][key] <= pivot and left < right:
                left = left + 1
            while l[right][key] >= pivot and left < right:
                right = right - 1
            self.swap(l, left, right)
        self.swap(l, left, high)
        print("part (l)" + str(sys.getsizeof(l)))
        print("part (left)" + str(sys.getsizeof(left)))
        print("part (high)" + str(sys.getsizeof(high)))
        print("part (key)" + str(sys.getsizeof(key)))
        print("part (right)" + str(sys.getsizeof(right)))
        print("part (pivot)" + str(sys.getsizeof(pivot)))
        return left

    def quick_sort(self, l, low, high, key):
        if low > high:
            return
        print("qs (l)" + str(sys.getsizeof(l)))
        print("qs (low)" + str(sys.getsizeof(low)))
        print("qs (high)" + str(sys.getsizeof(high)))
        print("qs (key)" + str(sys.getsizeof(key)))
        pivot = self.partition(l, low, high, key)
        print("qs (pivot)" + str(sys.getsizeof(pivot)))
        self.quick_sort(l, low, pivot - 1, key)
        self.quick_sort(l, pivot + 1, high, key)
        


