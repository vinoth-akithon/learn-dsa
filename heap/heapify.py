"""
Heapify algorithm
"""

class Maxheap(object):
    def heapify(arr: list) -> list:
        last_parent_index = Maxheap.__get_last_parent_index(arr)
        # for index in range(last_parent_index):
        #     Maxheap.__heapify(arr, index)

        # More optimized way(less recursion)
        for index in range(last_parent_index, -1, -1):
            Maxheap.__heapify(arr, index)
        return arr
    
    def __heapify(arr, index):
        largest_index = index

        left_index = Maxheap.__get_left_child_index(index)
        if (left_index < len(arr) ) and (arr[left_index] > arr[index]):
            largest_index = left_index
        
        right_index = Maxheap.__get_right_child_index(index)
        if (right_index < len(arr)) and (arr[right_index] > arr[index]):
            largest_index = right_index

        if (largest_index == index):
            return 
        Maxheap.__swap_node(arr, index, largest_index)
        Maxheap.__heapify(arr, largest_index)
        
    def __get_left_child_index(parent_index: int) -> int:
        return (parent_index * 2) + 1

    def __get_right_child_index(parent_index: int) -> int:
        return (parent_index * 2) + 2
    
    def __get_last_parent_index(arr: list) -> int:
        return (len(arr)// 2) - 1
    
    def __swap_node(arr, first, second) -> None:
        arr[first], arr[second] = arr[second], arr[first]
            


input_array = [ 5, 3, 8, 4, 1, 2 ]
print(f"Input array: {input_array}")
print(f"Output array: {Maxheap.heapify(input_array)}")