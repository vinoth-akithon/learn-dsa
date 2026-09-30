"""

"""



def print_message_n_times(n: int, message: str):
    """
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive stack

        - Behind the scene Recursion work this way
            def fun(3):
                print("Hello World!")
                fun(2)

            def fun(2):
                print("Hello World!")
                fun(1)

            def fun(1):
                print("Hello World!")
                fun(0)

            def fun(0):
                return
    """
    # Base condition
    if n == 0:
        return 
    print(message)
    print_message_n_times(n-1)


if __name__ == "__main__":
    n = 3
    print_message_n_times(n)


                                                      
# print_message_n_times(3) -> print("x") -> print_message_n_times(2) -> print("x")  -> print_message_n_times(1) -> print("x")-> print_message_n_times(0) -> return None