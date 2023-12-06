"""

Example1:
    Input: 5
    Output: 
            * 
            * * 
            * * * 
            * * * * 
            * * * * *
            * * * *
            * * *
            * *
            *
             
"""



class Solution:
    def printTriangle(self, N):
        for i in range(N):
            print("* " * (i+1))
        for j in range(N-2, -1, -1):
            print("* " * (j+1))



if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(5)
