"""

Example1:
    Input: 5
    Output:
            1
            2 3
            4 5 6
            7 8 9 10
            11 12 13 14 15
             
"""


class Solution:
    def printTriangle(self, N):
        start = 1
        for i in range(1, N+1):
            for j in range(start, start+i):
                print(j, end=" ")
                start += 1
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)