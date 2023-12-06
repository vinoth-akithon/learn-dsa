"""

Example1:
    Input: 5
    Output:
            A
            BB
            CCC
            DDDD
            EEEEE
             
"""


class Solution:
    def printTriangle(self, N):
        for i in range(N):
            char = chr(i+65)
            for _ in range(i+1):
                print(char, end="")
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)