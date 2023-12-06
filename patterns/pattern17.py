"""

Example1:
    Input: 3
    Output:
            A
           ABA
          ABCBA
             
"""


class Solution:
    def printTriangle(self, N):
        for i in range(N):
            print(" " * (N-i-1), end="")

            break_point = (2*i+1)//2
            index = 0
            for j in range(2*i+1):
                if j <= break_point:
                    index = j
                    print(chr(j+65), end="")
                else:
                    print(chr(index-1+65), end="")
                    index -= 1
            print()


if __name__ == "__main__":
    sn = Solution()
    sn.printTriangle(3)