"""
Min Stack

Design a stack that supports push, pop, top, and 
retrieving the minimum element in constant time.

Implement the MinStack class:

    -> MinStack() initializes the stack object.
    -> void push(int val) pushes the element val onto the stack.
    -> void pop() removes the element on the top of the stack.
    -> int top() gets the top element of the stack.
    -> int getMin() retrieves the minimum element in the stack.
    -> You must implement a solution with O(1) time complexity for each function.
"""

class MinStack:

    def __init__(self):
        self.main_stack = []
        self.auxilary_stack = []

    def push(self, val: int) -> None:
        if (not self.auxilary_stack) or (val <= self.auxilary_stack[-1]):
            self.auxilary_stack.append(val) 
        self.main_stack.append(val)

    def pop(self) -> None:
        if self.main_stack.pop() == self.auxilary_stack[-1]:
            self.auxilary_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.auxilary_stack[-1]

    def __repr__(self) -> str:
        return f"{self.main_stack}"


if __name__ == "__main__":
    minStack = MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    print(minStack.getMin()) # return -3
    minStack.pop();
    minStack.top()    # return 0
    print(minStack.getMin()); # return -2
