"""

Example1:
    Input: 3
    Output: 
            *  
           ***
          *****
          *****
           ***
            *
             
"""


class Solution:
    def printDiamond(self, N):
        for i in range(N):
            print(" " * (N-i-1), end="")
            print("* " * (i+1))

        for i in range(N-1, -1, -1):
            print(" " * (N-i-1), end="")
            print("* " * (i+1))


# class Solution:
#     def printDiamond(self, N):
#         # Code here
#         for i in range(N):
#             print(" " * (N-i-1),end="")
#             print("* " * (i+1))
        
#         for i in range(N):
#             print(" " * i, end="")
#             print("* " * (N-i))



if __name__ == "__main__":
    sn = Solution()
    sn.printDiamond(3)