import math

def reverse_number(num: int) -> int:
    if num <= 9:
        return num
    remainder = num%10
    quotient = num//10
    num_digits_in_quotient = math.floor(math.log10(quotient)) + 1
    return (remainder * (10**num_digits_in_quotient)) + reverse_number(quotient)


if __name__ == "__main__":
    print(reverse_number(182))