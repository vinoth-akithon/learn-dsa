"""

Example1:
    Input: 5
    Output:
            1 
            0 1 
            1 0 1
            0 1 0 1 
            1 0 1 0 1
             
"""

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(0, i+1):
                if (i+j) %2 == 0:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)