"""
Baseball Game

You are keeping the scores for a baseball game with strange rules.
At the beginning of the game, you start with an empty record.

You are given a list of strings operations, 
where operations[i] is the ith operation you must 
apply to the record and is one of the following:

    An integer x --> Record a new score of x.
    '+'          --> Record a new score that is the sum of the previous two scores.
    'D'          --> Record a new score that is the double of the previous score.
    'C'          --> Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate
calculations fit in a 32-bit integer and that all operations are valid.


Example 1:
    Input: ops = ["5","2","C","D","+"]
    Output: 30

Example 2:
    Input: ops = ["5","-2","4","C","D","9","+","+"]
    Output: 27

Example 3:
    Input: ops = ["1","C"]
    Output: 0
"""

class Solution:
    
    def __init__(self) -> None:
        self.stack = []

    def __push(self, data:int) -> None:
        self.stack.append(data)

    def __is_empty(self):
        return False if self.stack else True

    def __pop(self) -> int:
        if self.__is_empty():
            return 0
        return self.stack.pop()
    
    def __peek(self) -> int:
        if self.__is_empty():
            return 0
        return self.stack[-1]

    def calPoints(self, operations: list[str]) -> int:
        for i in operations:
            if i == "+":
                first = self.__pop()
                second = self.__peek()
                if first:
                    self.__push(first)
                self.__push(first+second)

            elif i == "D":
                previous_score = self.__peek()  
                self.__push(previous_score * 2)
            
            elif i == "C":
                self.__pop()
                
            else:
                self.__push(int(i))
        return sum(self.stack)
            


    
    def __repr__(self):
        return f"{self.stack}"


if __name__ == "__main__":
    ops = ["5","2","C","D","+"]
    # ops = ["5","-2","4","C","D","9","+","+"]
    # ops = ["1","C"]
    sn = Solution()
    print(sn.calPoints(ops))

    print(sn)