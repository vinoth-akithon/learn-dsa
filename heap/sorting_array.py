"""
Sorting array using Heap data structure
"""

from heap_using_array import Heap

def sort(arr: list, decending=False) -> list:
    heap = Heap()
    for element in arr:
        heap.insert(element)

    if decending:
        for i in range(len(arr)):
            arr[i] = heap.remove()
    else:
        for i in range(len(arr) - 1, -1, -1):
            arr[i] = heap.remove()
    

    
arr = [100, 20, 50, 30, 10, 40, 90]
# Accendig Order
sort(arr)
print(arr)
# Decending Order
sort(arr, decending=True)
print(arr)
