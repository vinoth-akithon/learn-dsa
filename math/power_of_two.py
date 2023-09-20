
from math import log2

class PowerOfTwo(object):
    def is_powerof_two(n: int) -> bool:
        # return PowerOfTwo.__power_of_two_using_bitwise(n)
        return PowerOfTwo.__power_of_two_using_math(n)
    

    def __power_of_two_using_math(n: int) -> bool:
        if n == 0:
            return False
        return log2(n).is_integer()

    def __power_of_two_using_bitwise(n: int) -> bool:
        if n == 0:
            return False
        
        count = 0
        while (n > 0):
            count += (n & 1) #Increment of counter variable if we get 1 as the rightmost bit
            n >>= 1 #Right Shift n to remove the rightmost bit.
        
        return count == 1 #returning true if number of set bits is 1 otherwise false.
        


if __name__ == "__main__":
    print(PowerOfTwo.is_powerof_two(8))
    print(PowerOfTwo.is_powerof_two(9))
