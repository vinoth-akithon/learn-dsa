def count_zeros(num: int, count=0) -> int:
    """Special pattern, how to pass a value(base condition returned one) to all above call"""
    if num <= 9:
        return count
    
    rem = num%10
    if rem == 0:
        return count_zeros(num//10, count+1)
    return count_zeros(num//10, count)
    

def count_zeros2(num: int) -> int:
    if num <= 9:
        return 0
    
    rem = num%10
    if rem == 0:
        return 1 + count_zeros2(num//10)
    return count_zeros2(num//10)



if __name__ == "__main__":
    print(count_zeros(450732000))
    print(count_zeros2(450732000))
    print(count_zeros(0))
    print(count_zeros2(0))