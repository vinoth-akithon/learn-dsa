"""
Reverse a String
(You are given a string s. You need to reverse the string.)

input --> Geeks  result --> skeeG
input --> for  result --> rof

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Note:
    --> Noation O(n) (when processing about linked list and array),  
    --> Notation O(|S|) (when processing about String or Sequence of characters)
""" 

def reverse_string(s: str):
    lst = list(s)
    input_string_length = len(s)
    first_pointer = 0
    second_pointer = input_string_length - 1
    quotient = input_string_length // 2
    while first_pointer < quotient:
        lst[first_pointer], lst[second_pointer] = \
            lst[second_pointer], lst[first_pointer]
        first_pointer +=1
        second_pointer -=1

    return "".join(lst)

print(reverse_string("Geeks"))