"""
All searching algorithm implementation
"""

from math import sqrt

class Search(object):
    def __init__(self, array: list, target: int) -> None:
        self.__array = array
        self.__target = target

    
    def linear_search(self) -> int:
        for i in range(len(self.__array)):
             if self.__array[i] == self.__target:
                 return i
        return -1
    

    def binary_search(self) -> int:
        return self.__binary_search_using_recursion(self.__array, 0, len(self.__array)-1)
        # return self.__binary_search_using_iteration()
    

    def __binary_search_using_iteration(self):
        left, right = 0, len(self.__array) - 1
        while (left <= right):
            middle = (left + right) // 2

            if self.__target == self.__array[middle]:
                return middle
            
            if self.__target < self.__array[middle]:
                right = middle - 1
            elif self.__target > self.__array[middle]:
                left = middle + 1
                
        return -1

    

    def __binary_search_using_recursion(self, array, left: int, right: int) -> int:
        # Base condition
        if right < left:
            return -1

        middle = (right + left) // 2

        if self.__target < array[middle]:
            return self.__binary_search_using_recursion(array, left, middle-1)
        elif self.__target > array[middle]:
            return self.__binary_search_using_recursion(array, middle+1, right)
        return middle


    def ternary_search(self) -> int:
        return self.__ternary_search(0, len(self.__array)-1)
    

    def __ternary_search(self, left: int, right: int) -> int:
        # Base condition
        if left > right: return -1
        
        partition = (right - left)//3
        mid1 = left + partition
        mid2 = right - partition

        if self.__target == self.__array[mid1]:
            return mid1
        elif self.__target == self.__array[mid2]:
            return mid2
        elif self.__target < self.__array[mid1]:
            return self.__ternary_search(left, mid1-1)
        elif self.__target > self.__array[mid2]:
            return self.__ternary_search(mid2+1, right)
        return self.__ternary_search(mid1+1, mid2-1)
    

    def jump_search(self):
        block_size = int(sqrt(len(self.__array)))
        start = 0; 
        next = block_size

        while (start < len(self.__array) and self.__array[next -1] < self.__target):
            start = next
            next += block_size
            if next > len(self.__array):
                next = len(self.__array)
    
        for i in range(start, next):
            if self.__target == self.__array[i]:
                return i
        return -1


    def exponentail_search(self):
        bound = 1
        while (bound < len(self.__array) and self.__array[bound] < self.__target):
            bound *= 2

        lower_bound = bound // 2
        upper_bound = min(bound, len(self.__array) -1)
        return self.__binary_search_using_recursion(self.__array, lower_bound, upper_bound)

if __name__ == "__main__":

    # input_array = [1, 4, 3, 7, 2, 6]; target = 3
    input_array = [10, 20, 30, 40, 50, 60]; target = 100
    # input_array = []; target = 80

    # Search object Instatiation
    search = Search(input_array, target)
    
    # Linear Search
    # print(search.linear_search())

    # Binery Search
    # print(search.binary_search())

    # Ternary Search
    # print(search.ternary_search())

    # Jump search
    # print(search.jump_search())

    # Exponentail Search
    print(search.exponentail_search())