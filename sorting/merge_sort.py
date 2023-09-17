"""
Merge Sort Implementaion
"""

class MergeSort(object):
    def __init__(self, array: list) -> None:
        self.__array = array

    
    def sort(self) -> list:
        return self.__sort(self.__array)

    
    def __sort(self, array: list) -> list:
        # Base condition for recursion
        if len(array) < 2:
            return array
        
        # devide the array into half and sort them seperately
        middle = len(array)//2
        left_array = self.__sort(array[:middle])
        right_array = self.__sort(array[middle:])

        # merge the sorted sub array
        return self.__merge(left_array, right_array, array)

    
    def __merge(self, left_array: list, right_array: list, array: list) -> list:
        i = j = k = 0
        while (i < len(left_array) and j < len(right_array)):
            if (left_array[i] <= right_array[j]):
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1 
            k += 1

        while (i < len(left_array)):
            array[k] = left_array[i]
            i += 1
            k += 1

        while (j < len(right_array)):
            array[k] = right_array[j]
            j += 1
            k += 1

        return array
        



    def __repr__(self) -> str:
        return f"{self.__array}"



if __name__ == "__main__":

    # input_array = [8, 2, 4, 1 ,3]
    input_array = [8, 2, 4, 1]
    m_sort = MergeSort(input_array)
    print(m_sort.sort())