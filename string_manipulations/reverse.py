"""
Reverse a string
"""

class ReverseString(object):

    def reverse(s: str) -> str:
        if not isinstance(s, str):
            raise ValueError("Argument 's' must be a 'str' object")
        
        return ReverseString.__reverse_using_two_pointer(s) # O(n) due to type casting 
        # return ReverseString.__reverse_using_stack(s) # O(n) due to type casting(here is stack)
        # return ReverseString.__reverse_using_reverse_iteration(s) # O(n) due to type casting
        # return ReverseString.__reverse_using_string_concatination(s) # O(n^2) due to string concat


    def __reverse_using_string_concatination(s: str) -> str:
        result = ""
        for i in range(len(s)-1, -1, -1): # O(n)
            result += s[i] # O(n)

        return result
    

    def __reverse_using_reverse_iteration(s: str) -> str:
        return "".join([s[i] for i in range(len(s)-1, -1, -1)])
    
    
    def __reverse_using_stack(s: str) -> str:
        stack = [char for char in s]        
        return "".join([stack.pop() for _ in range(len(stack))])


    def __reverse_using_two_pointer(s: str) -> str:
        start = 0; end = len(s) -1
        s = list(s)
        for _ in range(len(s)//2):
            ReverseString.__swap(s, start, end)
            start += 1
            end -= 1
        return "".join(s)
    

    def __swap(array: list, index1: int, index2: int) -> None:
        array[index1], array[index2] = \
        array[index2], array[index1]



class ReverseWords(object):


    def reverse(s: str) -> list[str]:
        lst = s.strip().split(" ")
        lst.reverse()
        return " ".join(lst)

        


if __name__ == "__main__":

    # Reversing a string
    # input_string = "apple"
    # input_string = "banana"
    # print(ReverseString.reverse(input_string))

    # Reversing Word
    input_string = "I am the best in the World"
    print(f"'{ReverseWords.reverse(input_string)}'")