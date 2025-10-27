"""
    Approach 1: Using a hash set for tracking previous processed number
        - We can solve it using either iterative or recursive (Best use case for using recursive function)
        - Using number theory concept we can grab the last digit dividing a number by 10, take remainder for last digit and quotient for getting next digit.
        - Summing up all the individual digits square. 
        - Complexity Analysis: 
            - Time -> O(d) or O(log n) Digit Extraction + O(1) Iteration 
            - Space -> O(k) Seen number
    Approach 2: Using Fast and slow pointers
        - As per number theory sum of the square of individual digits fall into either `1` or `cyclic`.
        - So, fast and slow pointers meet at one number, if the number is `1` then happy number else it's cycling.
        - Complexity Analysis:
            - Time -> O(d) or O(log n) Digit Extraction + O(1) Iteration 
            - Space -> O(1)
"""



def happy_number_iterative(n: int) -> bool:
    seen = set()
    while True:
        seen.add(n)
        s = 0
        while (n):
            s += (n%10)**2
            n //= 10
        if s == 1:
            return True
        elif s in seen:
            return False
        n = s

def get_happy_number(n: int) -> int:
    q = n // 10
    r = n % 10
    # Base Condition
    if q == 0:
        return r**2
    return r**2 + get_happy_number(q)


def happy_number_recursive(n: int) -> bool:
    if n <= 0:
        return False
    seen = set()
    while (n not in seen):
        seen.add(n)
        happy_number = get_happy_number(n)
        if happy_number == 1:
            return True
        else:
            n = happy_number
    return False

def square_of_digits(n: int) -> int:
    sum = 0
    while (n != 0):
        sum += n % 10
        n //= 10
    return sum
    

def happy_number_two_pointer(n: int) -> bool:
    s = f = n

    while True:
        s = square_of_digits(s)
        f = square_of_digits(square_of_digits(f))

        if s == f:
            if s == 1:
                return True
            else:
                return False    

    
if __name__ == "__main__":
    n = 19
    # n = 2
    # print(happy_number_iterative(n))
    # print(happy_number_recursive(n))
    print(happy_number_two_pointer(n))