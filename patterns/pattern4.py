"""

Example 1:
    Input: 5
    Output: 
        1 
        2 2
        3 3 3
        4 4 4 4
        5 5 5 5 5

Example2:
    Input: 3
    Output: 
        1 
        2 2
        3 3 3
             
"""
class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            for j in range(i):
                print(i, end=" ")
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)