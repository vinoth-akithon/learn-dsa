"""
"""

def int_to_bin(n: int, ans: str="") -> str:
    """
        - Complexity Analysis:
            - Time -> O(log n + (log n)^2 (for string concatenation))
            - Space -> O(log n)
    """
    # Base condition
    if n == 0:
        return ans
    ans = str(n%2) + ans  
    return int_to_bin(n//2, ans)

def brute_force(n: int, i: int) -> bool:
    """
        - Complexity Analysis:
            - Time -> O(log n + (log n)^2 (for string concatenation) + n) ~= O((log n)^2)
            - Space -> O(log n)
    """
    binary = int_to_bin(n)
    m = len(binary)
    if i >= m:
        return False
    return binary[m-1-i] == "1"


def optimal_approach(n: int, i: int) -> int:
    """
        Complexity Analysis:
            - Time -> O(1)
            - Space -> O(1)
    """
    return (n >> i) & 1 == 1

if __name__ == "__main__":
    # print(int_to_bin(4, ""))
    # n = 5; i = 2
    n = 4; i = 0
    print(brute_force(n, i))
    print(optimal_approach(n, i))

