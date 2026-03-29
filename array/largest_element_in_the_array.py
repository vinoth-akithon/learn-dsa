"""
Largest element in the given array
"""

def largest_element(arr: list[int]) -> int|None:
    if not arr:
        return None
    
    le = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > le:
            le = arr[i]
    return le


if __name__ == "__main__":
    arr = [2, 5, 1, 3, 0]
    print(largest_element(arr))