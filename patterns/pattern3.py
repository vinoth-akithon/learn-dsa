"""

Example 1:
    Input: 5
    Output: 
        1 
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5

Example2:
    Input: 2
    Output: 
        1 
        1 2
 
"""

class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()



if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)