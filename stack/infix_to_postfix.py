"""

"""


def brute_force(s: str):
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    stack = []
    precedence_map = {
        '^': 3,   # Bitwise XOR
        '*': 2,   # Multiplication
        '/': 2,   # Division
        '+': 1,   # Addition
        '-': 1,   # Subtraction
    }

    res = ""
    operators = precedence_map.keys()
    for c in s:
        # If operand
        if c == " ":
            continue
        elif c == "(":
            stack.append(c)
        elif c == ")":
            # pop all the operators in the until "("
            while stack[-1] != "(":
                res += stack.pop()
            # pop open parenthesis "("
            stack.pop()
        elif c not in operators:
            # add char directly to the result
            res += c

        # If operator
        # elif not len(stack) or stack[-1] == "(" or precedence_map[c] > precedence_map[stack[-1]]:
        #     stack.append(c)
        else:
            while stack \
                and stack[-1] != "(" and \
                (precedence_map[stack[-1]] > precedence_map[c] \
                    or (precedence_map[stack[-1]] == precedence_map[c] and c != "^")) :
                res += stack.pop()
            stack.append(c)

    while stack:
        res += stack.pop()

    return res


def prec(c):
    if c == '^':  # Exponent operator has highest precedence
        return 3
    elif c == '/' or c == '*':  # Multiplication and division have higher precedence than addition
        return 2
    elif c == '+' or c == '-':  # Addition and subtraction have lowest precedence
        return 1
    else:
        return -1

# Function to convert infix expression to postfix expression
def infixToPostfix(s):
    stack = []  # Stack to hold operators and parentheses
    result = ""  # String to hold the resulting postfix expression

    for c in s:
        if c == " ":
            continue
        # If the scanned character is an operand, add it to the result string
        if c.isalnum():
            result += c
        # If the scanned character is an ‘(‘, push it to the stack
        elif c == '(':
            stack.append('(')
        # If the scanned character is a ‘)’, pop from stack until an ‘(‘ is encountered
        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # Pop the ‘(‘ from the stack
        # If an operator is scanned
        else:
            while stack and prec(c) <= prec(stack[-1]):
                result += stack.pop()
            stack.append(c)  # Push the current operator to the stack

    # Pop all the remaining elements from the stack
    while stack:
        result += stack.pop()

    print(f"Postfix expression: {result}")  # Output the result


if __name__ == "__main__":
    # s = "(p + q) * (m - n)"
    s = "a + b * (c^d - e) ^ (f + g * h) - i  "
    # s = "h^m^q^(7-4)"
    print(brute_force(s))
    # print(infixToPostfix(s))