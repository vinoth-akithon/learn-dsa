"""
Check the given string is palindrome
"""


class Palindrome(object):

    def is_palindrome(s: str) -> bool:
        if not isinstance(s, str):
            raise ValueError("Argument 's' must be 'str' object")
        
        # return Palindrome.__check_palindrome_using_reversing(s)
        return Palindrome.__check_palindrome_using_two_pointer(s)
    

    def __check_palindrome_using_reversing(s: str) -> bool:
        # O (n)
        return s == "".join(reversed(s))
    

    def __check_palindrome_using_two_pointer(s: str) -> bool:
        # O (log n)
        for i in range(len(s)//2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

    


if __name__ == "__main__":
    input_str = "madam"
    # input_str = "vinoth"

    print(Palindrome.is_palindrome(input_str))