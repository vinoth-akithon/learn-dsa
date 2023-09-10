"""
Finding the Kth largest item in the heap
"""

from heapify import Maxheap
from heap_using_array import Heap


def kth_largest_item(arr: list, k: int) -> int: 
    if not arr:
        raise ValueError("Array is Empty")
    
    elif (k < 1) or (k > len(arr)):
        if len(arr) == 1:
            raise ValueError(f"k must be 1")
        raise ValueError(f"k must be in range 1-{len(arr)}")
    heap = Heap()
    for item in arr:
        heap.insert(item)

    for _ in range(k-1):
        heap.remove()

    return heap.max()


# Need to add extra logic for getting Kth largest
# because the heapified function does not return sorted one.
# def kth_largest_item(arr: list, k: int) -> int: 
#     if not arr:
#         raise ValueError("Array is empty")
#     elif (k < 1) or (k > len(arr)):
#         if len(arr) == 1:
#             raise ValueError(f"k must be 1")
#         raise ValueError(f"k must be in range 1-{len(arr)}")
    
#     heap = Maxheap.heapify(arr)
#     return heap[k-1]


input_array = [ 5, 3, 8, 4, 1, 2 ]
print(kth_largest_item(input_array, 1))
