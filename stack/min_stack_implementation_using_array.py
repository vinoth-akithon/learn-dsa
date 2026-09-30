"""

"""


class MinStack:
    def __init__(self):
        self._items = []
        self._size = 0


    def push(self, data: int) -> None:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        self._items.append(data)
        self._size += 1

    
    def get_min(self) -> None:
        """
            - Complexity Analysis:
                - Time -> O(n)
                - Space -> O(n)
        """
        if self.is_empty:
            raise Exception("Stack is Empty")
        # Pop from the stack and keep track of running min store into auxiliary stack
        aux_stack = []
        curr_min = float("inf")
        for _ in range(self._size):
            curr = self._items.pop()
            if curr < curr_min:
                curr_min = curr
            aux_stack.append(curr)

        # pop all the items from the auxiliary stack and push into the original stack
        for _ in range(self._size):
            self._items.append(aux_stack.pop())

        return curr_min

    def pop(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if self.is_empty:
            raise Exception("Stack is Empty")

        data = self._items.pop()
        self._size -= 1
        return data

    def top(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if self.is_empty:
            raise Exception("Stack is Empty")
        return self._items[-1]

    @property
    def size(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        return self._size

    @property
    def is_empty(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        return self._size == 0

class MinStackEfficient:
    def __init__(self):
        self._items = []
        self._aux_stack = []

    def push(self, data: int) -> None:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if not self._aux_stack or data <= self._aux_stack[-1]:
            self._aux_stack.append(data)
        self._items.append(data)

    
    def get_min(self) -> None:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if not self._aux_stack:
            raise Exception("Stack is Empty")
        return self._aux_stack[-1]

    def pop(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if not self._items:
            raise Exception("Stack is Empty")

        if self._items[-1] == self._aux_stack[-1]:
            self._aux_stack.pop()
        data = self._items.pop()
        return data

    def top(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if not self._items:
            raise Exception("Stack is Empty")
        return self._items[-1]

    @property
    def size(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        return len(self._items)

class MinStackEfficient2:
    def __init__(self):
        self._items = []

    def push(self, data: int) -> None:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if not self._items:
            self._items.append((data, data))
        else:
            self._items.append((data, min(data, self._items[-1][0])))

    def get_min(self) -> None:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if not self._items:
            raise Exception("Stack is Empty")
        return self._items[-1][1]

    def pop(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if not self._items:
            raise Exception("Stack is Empty")

        data = self._items.pop()[0]
        return data

    def top(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if not self._items:
            raise Exception("Stack is Empty")
        return self._items[-1][0]

    @property
    def size(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        return len(self._items)


if __name__ == "__main__":
    # stack = MinStack()
    # stack = MinStackEfficient()
    stack = MinStackEfficient2()



    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.top())
    print(stack.pop())
    print(stack.top())
    print(stack.get_min())