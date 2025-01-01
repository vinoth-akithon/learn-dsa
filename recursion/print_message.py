# Recursion works this way in behind
def greet():
    greet4()
    print("Hello World!")

def greet4():
    greet3()
    print("Hello World!")

def greet3():
    greet2()
    print("Hello World!")

def greet2():
    greet1()
    print("Hello World!")

def greet1():
    greet0()
    print("Hello World!")

def greet0():
    return



def greet_recursive(n: int) -> None:
    if n == 0:
        return
    greet_recursive(n-1)
    print("Hello World!")


if __name__ == "__main__":
    greet()
    print("-"*12)
    greet_recursive(5)