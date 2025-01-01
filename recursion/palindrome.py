import math
from reverse_number import reverse_number

def palindrome(num: int) -> bool:
    if num <= 9:
        return True
    last = num%10
    total_digits = math.floor(math.log10(num)) + 1
    first = num//(10**(total_digits-1))
    if first != last:
        return False
    return palindrome((num//10) - (first * 10**(total_digits-2)))

def palindrome2(num: int) -> bool:
    return num == reverse_number(num)


if __name__ == "__main__":
    print(palindrome(823328))
    print(palindrome2(8238))
