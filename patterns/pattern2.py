"""

Example 1:
    Input: 5
    Output: 
        * 
        * *
        * * *
        * * * *
        * * * * *

Example2:
    Input: 2
    Output: 
        * 
        * *
        * * *
             
"""

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for _ in range(i+1):
                print("*", end=" ")
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)