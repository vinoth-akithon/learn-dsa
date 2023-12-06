"""

Example 1:
    Input: 5
    Output: 
        * * * * * 
        * * * *
        * * *
        * *
        *

Example2:
    Input: 3
    Output: 
        * * *
        * *
        *
             
"""



class Solution:
    def printTriangle(self, N):
        for i in range(N, 0, -1):
            for _ in range(i):
                print("*", end=" ")
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(3)