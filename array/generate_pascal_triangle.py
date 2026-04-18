"""

"""
import math


def naive_approach(n: int) -> list:
    """
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n^2)
    """
    result = []

    for i in range(n):
        for j in range(i+1):
            if j == 0:
                result.append([1])
            elif j == i:
                result[i].append(1)
            else:
                result[i].append(result[i-1][j] + result[i-1][j-1])

    return result

def using_ncr_formula1(N: int) -> list:
    """
        - Using Direct nCr combinators formula.
            - c(n,k) = n! / (k! (n-k)!) 

        - Complexity Analysis:
            - Time -> O(n^3) here O(n) is for computing factorial every time so, it applies for O(n^2) elements
            - Space -> O(n^2) 
    """

    res = []
    for n in range(N):
        res.append([])
        for k in range(n+1):
            e = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
            res[n].append(e)
    
    return res

def using_ncr_formula2(N: int) -> list:
    """
        - Using Direct nCr combinators formula.
            - c(n,k) = n! / (k! (n-k)!) 
        -  But Instead of computing factorial every time, precompute factorials

        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n^2) 
    """

    facts = [1, 1]
    for i in range(2, N):
        facts.append(facts[i-1] * i)
    
    res = []
    for n in range(N):
        res.append([])
        for k in range(n+1):
            e = facts[n] // (facts[k] * facts[n-k])
            res[n].append(e)
    
    return res

def using_ncr_formula3(N: int) -> list:
    """
        - Using Incremental nCr combinators formula.
            - c(n,k) = n! / (k! * (n-k)!)
            - c(n,k-1) = n! / ((k-1)! * (n-k+1)!)
            
            - divide c(n,k) and c(n, k-1) and rearrange them
            - c(n,k) = c(n, k-1) * (n-k+1) / k

        - Here are not utilizing factorials

        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n^2) 
    """

    
    res = []
    for n in range(N):
        curr = [1]
        for k in range(1, n+1):
            e = curr[k-1] * (n-k+1) / k
            curr.append(int(e))
        res.append(curr)
    return res


def getNthRow(N):
    # Result list to store the row
    row = []
    
    # First value of the row is always 1
    val = 1
    row.append(val)
    
    # Compute remaining values using the relation:
    # C(n, k) = C(n, k-1) * (n-k) / k
    for k in range(1, N):
        val = val * (N - k) / k
        row.append(val)
    
    return row

def temp(N):
    res = []
    for i in range(N):
        res.append(getNthRow(i))
    return res

if __name__ == "__main__":
    # print(naive_approach(5))
    print(using_ncr_formula1(13))
    # print(using_ncr_formula2(5))
    print(using_ncr_formula3(13))
    print()
    # print(temp(13))