"""
Counting Sort Algo Implementation
"""


class CountingSort(object):
    def __init__(self, array:list, k: int) -> None:
        self.__array = array
        self.__k = k + 1


    def sort(self) -> list:
        counter = [0 for _ in range(self.__k)]
        for i in self.__array:
            counter[i] += 1

        pointer = 0
        for i in range(self.__k):
            for _ in range(counter[i]):
                self.__array[pointer] = i
                pointer +=1
            
        return self.__array

    def __repr__(self) -> str:
        return f"{self.__array}"


if __name__ == "__main__":
    input_array = [5, 2, 1, 3, 2, 5]; max_element = 5
    # input_array = []; max_element = 5

    c_sort = CountingSort(input_array, max_element)
    print(c_sort.sort())