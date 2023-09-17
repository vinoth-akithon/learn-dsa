"""
Bubble sorting algorithm implementation
"""


class BubbleSort(object):
    def __init__(self, array: list) -> None:
        self.__array = array

    def sort(self) -> list:
        no_of_passes = len(self.__array) - 1
        for j in range(no_of_passes):
            is_sorted = True # for best case
            for i in range(no_of_passes - j):
                if self.__array[i] > self.__array[i+1]:
                    self.swap(i, i+1)
                    is_sorted = False
            if is_sorted:
                return self.__array
        return self.__array
    
    def swap(self, index1: int, index2: int) -> None:
        self.__array[index1], self.__array[index2] = \
        self.__array[index2], self.__array[index1]


    def __repr__(self) -> str:
        return f"{self.__array}"
    


if __name__ == "__main__":
    input_array = [8, 2, 4, 1, 3]
    # input_array = []
    b_sort = BubbleSort(input_array)
    print(b_sort.sort())
