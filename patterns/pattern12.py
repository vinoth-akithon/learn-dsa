"""

Example1:
    Input: 3
    Output:
            1         1
            1 2     2 1
            1 2 3 3 2 1
             
"""

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print(j+1, end=" ")
            print("  " * (N-i-1) * 2, end="")
            for j in range(i, -1, -1):
                print(j+1, end=" ")
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(3)