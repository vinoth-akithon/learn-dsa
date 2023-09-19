"""
Bucket Sort Implementation
"""

from quick_sort import QuickSort

class BucketSort(object):
    def __init__(self, array: list, no_of_buckets: int) -> None:
        self.__array = array
        self.__no_of_buckets = no_of_buckets

    
    def sort(self) -> list:
        i = 0
        for bucket in self.__create_buckets:
            # Sorting the bucket individually
            q_sort = QuickSort(bucket)
            q_sort.sort()
            for item in bucket:
                self.__array[i] = item
                i += 1
        return self.__array
    
    @property
    def __create_buckets(self) -> list[list[int]]:
        # Creating empty buckets
        buckets = [[] for _ in range(self.__no_of_buckets)]

        # Distributing items into buckets
        for item in self.__array:
            bucket = item//self.__no_of_buckets
            buckets[bucket].append(item)

        return buckets


if __name__ == "__main__":
    input_array = [6, 2, 5, 4, 3, 7]
    # input_array = []

    bt_sort = BucketSort(input_array, 3)
    print(bt_sort.sort())