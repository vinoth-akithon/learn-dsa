"""

Example 1:
    Input: 5
    Output: 
        *    
       ***
      *****
     *******
    *********

Example2:
    Input: 3
    Output: 
        *****
         ***
          *
             
"""


class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for _ in range(N-i-1):
                print(" ", end="")
            for _ in range(2*(i+1)-1):
                print("*", end="")
            print()
    
if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)