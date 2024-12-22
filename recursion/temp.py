def greet():
    print("Hello World")
    greet1()

def greet1():
    print("Hello World")
    greet2()

def greet2():
    print("Hello World")
    greet3()

def greet3():
    print("Hello World")
    greet4()

def greet4():
    print("Hello World")


def printNumber(n: int):
    print(n)
    printNumber1(n+1)

def printNumber1(n: int):
    print(n)
    printNumber2(n+1)

def printNumber2(n: int):
    print(n)
    printNumber3(n+1)

def printNumber3(n: int):
    print(n)
    printNumber4(n+1)

def printNumber4(n: int):
    print(n)


def printNumberRecursion(n: int):
    # Base condition
    if n > 5:
        return
    
    # Function body
    print(n)

    # Recursive call
    printNumberRecursion(n+1)


def getNthFibonacci(n: int):
    # Base condition
    if n < 2:
        return n

    # Recursive call
    left = getNthFibonacci(n-1)
    right = getNthFibonacci(n-2)

    # Function body
    return left + right


if __name__ == "__main__":
    # greet()
    # printNumber(1)
    # printNumberRecursion(1)
    print(getNthFibonacci(6))