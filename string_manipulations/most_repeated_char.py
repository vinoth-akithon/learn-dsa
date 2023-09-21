"""
Find the most repeating charecter
"""
from collections import defaultdict


class RepeatingChar(object):

    def get_max_occuring_char(s: str) -> str:
        if not isinstance(s, str):
            raise ValueError("Argument 's' must be 'str' object")
        if not s:
            raise ValueError("Empty string found")
        
        # return RepeatingChar.__get_repeating_char_using_hash_table(s)
        return RepeatingChar.__get_repeating_char_using_array(s)
    

    def __get_repeating_char_using_array(s: str) -> str:
        ASCII_SIZE = 256
        arr = [0 for _ in range(ASCII_SIZE)]

        for char in s:
            arr[ord(char)] +=1

        max_value = 0
        max_char_index = 0
        for i in range(len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]
                max_char_index = i

        return chr(max_char_index)
    
    
    
    def __get_repeating_char_using_hash_table(s: str) -> str:
        hash_table = defaultdict(int)
        for char in s:
            hash_table[char] +=1

        max_value = 1
        max_char = " "
        for key, value in hash_table.items():
            if value > max_value:
                max_value = value
                max_char = key
        return max_char





if __name__ == "__main__":
    input_str = "banana"
    input_str = " "

    print(RepeatingChar.get_max_occuring_char(input_str))