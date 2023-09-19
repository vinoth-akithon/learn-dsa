"""
Implementing Quick Sort Algorithm
"""


class QuickSort(object):
    def __init__(self, array: list) -> None:
        self.__array = array


    def sort(self) -> list:
        return self.__sort(self.__array, 0, len(self.__array)-1)
    

    def __sort(self, array: list, start: int, end: int):
        # Base condition
        if start >= end:
            return array
        
        # Partition
        boundary = self.__partition(array, start, end)

        # Left Sort
        self.__sort(array, start, boundary - 1)

        # Right Sort
        self.__sort(array, boundary + 1 , end) 

        return array

    
    def __partition(self, array: list, start: int, end: int) -> int:
        pivot = array[end]
        boundary = start - 1
        for i in range(start, end+1):
            if array[i] <= pivot:
                boundary +=1
                self.swap(array, i, boundary)
        return boundary


    def swap(self, array: list, index1: int, index2: int) -> None:
        array[index1], array[index2] = \
        array[index2], array[index1]

    
    def __repr__(self) -> str:
        return f"{self.__array}"




if __name__ == "__main__":
    # input_array = [2, 8, 3, 5, 4]
    input_array = [2, 1, 11, 100, 12]

    q_sort = QuickSort(input_array)
    print(q_sort.sort())