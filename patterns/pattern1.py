"""

Example 1:
    Input: 5
    Output: 
        * * * * * 
        * * * * *
        * * * * *
        * * * * *
        * * * * *

Example2:
    Input: 2
    Output: 
        * * 
        * *
             
"""

class Solution:
    def printSquare(self, N):
        for _ in range(N):
            for _ in range(N):
                print("*", end=" ")
            print()



if __name__ == '__main__':
    sn = Solution()
    sn.printSquare(2)