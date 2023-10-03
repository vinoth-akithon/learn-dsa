"""
Magical Number

Your friend loves magic and he has coined a new term - "Magical number".
To perform his magic, he needs that Magic number. 
There are N number of people in the magic show, 
seated according to their ages in ascending order. 
A magical number is that seat no. where the person has 
the same age as that of the given seat number.
Help your friend in finding out that "Magical number".

Note: If there are multiple magical numbers in the array, 
return the any one valid value.

Input:
1
10
-10 -1 0 3 10 11 30 50 100 150

Output:
3

"""
# from typing import 

def binarySearch(arr: list[int], low: int, high: int):
    '''
    arr: given array
    low: low index initialize as zero
    high: high index initialize as len(arr)-1
    return: magical n.o or -1
    '''
    while (low <= high):
        middle_index = (low + high) // 2
        if middle_index == arr[middle_index]:
            return middle_index
        
        elif middle_index < arr[middle_index]:
            high = middle_index - 1
        
        else:
            low = middle_index + 1

    return -1


if __name__ == "__main__":
    arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100, 150]
    print(binarySearch(arr, 0, len(arr)-1))