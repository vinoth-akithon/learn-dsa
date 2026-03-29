"""


"""

def naive_approach(arr: list[int]) -> None:
    """
        - Complexity Analysis:
            - Time -> O(n^2) 
    """
    n = len(arr)
    visited = [False] * n
    lowest_elem = 0
    lowest_freq = float("inf")
    highest_elem = 0
    highest_freq = float("-inf")
    
    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        count = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        
        print(f"{arr[i]} -> {count}")
        if count < lowest_freq:
            lowest_elem = arr[i]
            lowest_freq = count
        if count > highest_freq:
            highest_elem = arr[i]
            highest_freq = count 
    print(f"Lowest Frequency Element: {lowest_elem}, Frequency: {lowest_freq}")
    print(f"Highest Frequency Element: {highest_elem}, Frequency: {highest_freq}")



def optimal_approach(arr: list[int]) -> dict[int, int]:
    """
    Complexity Analysis:
        - Time -> O(n)
        - Space -> O(U) -> No. of unique elements
    """
    hashmap = {}
    for e in arr:
        if e in hashmap:
            hashmap[e] += 1
        else:
            hashmap[e] = 1
    
    items = sorted(hashmap.items(), key=lambda item: item[1])
    print(f"Lowest Frequency Element: {items[0][0]}, Frequency: {items[0][1]}")
    print(f"Highest Frequency Element: {items[-1][0]}, Frequency: {items[-1][1]}")


if __name__ == "__main__":
    arr = [10,20,10,30,20,10]
    naive_approach(arr)
    print()
    optimal_approach(arr)