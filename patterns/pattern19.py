"""

Example 1:
    Input: 5
    Output: 
        **********
        ****  ****
        ***    ***
        **      **
        *        *
        *        *
        **      **
        ***    ***
        ****  ****
        **********

"""


class Solution:
    def printTriangle(self, N):
        for i in range(N-1, -1, -1):
            for _ in range(i+1):
                print("*", end="")
            print(" " * (N-i-1) * 2, end="")
            for j in range(i+1):
                print("*", end="")
            print()
        for i in range(N):
            for _ in range(i+1):
                print("*", end="")
            print(" " * (N-i-1) * 2, end="")
            for j in range(i+1):
                print("*", end="")
            print()

    
if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)