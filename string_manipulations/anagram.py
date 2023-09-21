"""
Check the two strings are anagram each other
"""


class Anagram(object):

    def check_anagram(str1: str, str2: str) -> bool:
        if (not isinstance(str1, str)) or (not isinstance(str2, str)) \
            or (len(str1) != len(str2)):
            return False
        
        # return Anagram.__check_anagram_using_sorting(str1, str2)
        return Anagram.__check_anagram_using_histogramming(str1, str2)
        
        
    def __check_anagram_using_sorting(str1: str, str2: str) -> bool:
        # O (n logn) due to sorting
        return sorted(str1.lower()) == sorted(str2.lower())


    def __check_anagram_using_histogramming(str1: str, str2: str) -> bool:
        AlPHA_SIZE = 26
        arr = [0 for _ in range(AlPHA_SIZE)]

        str1 = str1.lower()
        for char in str1:
            arr[Anagram.__get_index(char)] += 1

        str2 = str2.lower()
        for char in str2:
            index = Anagram.__get_index(char)
            if not arr[index]:
                return False
            arr[index] -= 1
        return True


    def __get_index(char: str) -> int:
        return ord(char) - ord("a")




if __name__ == "__main__":
    # input_str1 = "ABCD"; input_str2 = "cABD"
    input_str1 = "ABCD"; input_str2 = "aabc"

    print(Anagram.check_anagram(input_str1, input_str2))
