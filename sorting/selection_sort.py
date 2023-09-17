"""
Selection Sort Implementation

The name selction sort implies that for each pass,
we are selecting the minimum value from the un sorted array.
"""

class SelectionSort(object):
    def __init__(self, array: list) -> None:
        self.__array = array


    def sort(self) -> list:
        no_of_passes = len(self.__array)
        for i in range(no_of_passes - 1):
            min_value_index = i
            for j in range(i, no_of_passes):
                if self.__array[j] < self.__array[min_value_index]:
                    min_value_index = j
            self.__array[i], self.__array[min_value_index] = \
                self.__array[min_value_index], self.__array[i]
        return self.__array



if __name__ == "__main__":

    input_array = [8, 2, 4, 1, 3]
    # input_array = [10, 2]
    s_sort = SelectionSort(input_array)
    print(s_sort.sort())

     