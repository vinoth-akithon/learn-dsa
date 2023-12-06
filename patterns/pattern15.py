"""

Example1:
    Input: 5
    Output:
            ABCDE
            ABCD
            ABC
            AB
            A
             
"""


class Solution:
    def printTriangle(self, N):
        for i in range(N, 0, -1):
            for j in range(i):
                print(chr(j+65), end="")
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)