

class RotationsCheck(object):

    def are_rotations(str1: str, str2: str) -> bool:
        if not isinstance(str1, str):
            raise ValueError(f"Argument 'str1' must be the 'str' object")
        elif not isinstance(str2, str):
            raise ValueError(f"Argument 'str2' must be the 'str' object")
        
        if len(str1) != len(str2):
            return False

        # return RotationsCheck.__roration_check_using_string_concat(str1, str2)
        return RotationsCheck.__rotation_check_using_two_pointer(str1, str2)
        

    def __roration_check_using_string_concat(str1: str, str2: str) -> bool:
        if str2 in (str1 + str1):
            return True
        return False


    def __rotation_check_using_two_pointer(str1: str, str2: str) -> bool:
        str1_pointer = 0
        for i in range(len(str2)):
            if i == 0:
                str1_pointer = (str1.index(str2[i]) + 1) % len(str1)
            else:
                if str2[i] != str1[str1_pointer]:
                    return False
                str1_pointer = (str1_pointer + 1) % len(str1)
        return True

if __name__ == "__main__":
    # input_str1 = "ABCD"; input_str2 = "DABC"
    input_str1 = "ABC"; input_str2 = "BCA"

    print(RotationsCheck.are_rotations(input_str1, input_str2))