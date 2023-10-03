"""
Valid Parentheses

"""

class Solution:
    def __init__(self) -> None:
        self.stack = []
        self.bracket_mapping = {"{": "}", "[": "]", "(": ")", "<":">"}

    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        for char in s:
            if char in self.bracket_mapping:
                self.__push(char)
            else:
                top_element = self.__pop()
                if (not top_element) or (self.bracket_mapping[top_element]) != char:
                    return False
        return self.__is_empty()
            

    def __push(self, data:int) -> None:
        self.stack.append(data)


    def __is_empty(self):
        return False if self.stack else True


    def __pop(self) -> int:
        if self.__is_empty():
            return 0
        return self.stack.pop()


if __name__ == "__main__":
    s = "{}"
    s = "()[]{}"
    s = "(]"
    s = "["
    # s = "]"

    sn = Solution()
    print(sn.isValid(s))