"""

Example1:
    Input: 5
    Output:
            A
            AB
            ABC
            ABCD
            ABCDE
             
"""


class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print(chr(j+65), end="")
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)