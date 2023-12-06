"""

Example 1:
    Input: 5
    Output: 
        E 
        E D
        E D C
        E D C B
        E D C B A

"""


class Solution:
    def printTriangle(self, N):
        for i in range(N-1, -1, -1):
            for j in range(N-1, i-1 , -1):
                print(chr(j+65), end=" ")
            print()
    
if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)