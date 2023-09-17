"""
Insertion sort implementation
"""


class InsertionSort(object):
    def __init__(self, array: list) -> None:
        self.__array = array 

    def sort(self) -> list:
        for i in range(1, len(self.__array)):
            current_item = self.__array[i]
            # Here shifting instead of swapping
            j = i - 1
            while (j >= 0 and self.__array[j] > current_item):
                self.__array[j+1] = self.__array[j]
                j -= 1
            self.__array[j + 1] = current_item
        return self.__array

    def __repr__(self):
        return f"{self.__array}"



if __name__ == "__main__":
    input_array = [8, 2, 4, 1, 3]

    i_sort = InsertionSort(input_array)
    print(i_sort.sort())