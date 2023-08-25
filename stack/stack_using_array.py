

from typing import Any


class StackUsingArray(object):
    def __init__(self) -> None:
        self.__stack = []

    def push(self, item: Any) -> None:
        self.__stack.append(item)

    def pop(self):
        if self.is_empty():
            raise AssertionError("Stack is Empty")
        return self.__stack.pop()

    def peek(self):
        if self.is_empty():
            raise AssertionError("Stack is Empty")
        return self.__stack[-1]

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return not self.__stack

    def __str__(self):
        return str(self.__stack)
    


stack = StackUsingArray()
# print(stack)

# pushing object to stack
stack.push(1)
stack.push(2)
stack.push(3)
# print(stack)


# poping object from stack
# print(stack.pop())
# print(stack)
    

# peeking the top object
# print(stack.peek())
# print(stack)

# getting the size of the stack
# print(stack.size())

# checking the stack empty or not
# print(stack.is_empty())

import re

def is_expression_balenced(expression: str) -> bool:
    stack = StackUsingArray()
    # Regular expression to match open brackets
    left_pattern = r"[\(\[\{<]"
    right_pattern = r"[\)\]\}>]"
    bracket_mapping = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    for char in expression:
        if re.findall(left_pattern, char):
            stack.push(char)
        elif re.findall(right_pattern, char):
            if bracket_mapping[stack.pop()] != char:
                return False
    return True if stack.is_empty() else False
print(is_expression_balenced("(([1][] + {})) [a]"))