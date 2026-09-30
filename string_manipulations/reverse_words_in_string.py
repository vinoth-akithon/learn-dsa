"""

"""



def brute_force(s: str) -> str:
    """
        - Using Auxiliary DB (Stack for keeping words)
        - Complexity Analysis:
            - Time -> O(n + n^2)
            - Space -> O(n + n)

    """
    n = len(s)
    stack = []

    # striping the leading spaces
    l = 0
    while l < n:
        if s[l] == " ":
            l += 1
        else:
            break

    # String the trailing spaces
    r = n-1
    while r >= 0:
        if s[r] == " ":
            r -= 1
        else:
            break

    # Capturing the words and adding to the stack
    i = l
    while i <= r:
        if s[i] == " ":
            stack.append(s[l:i])
            while s[i] == " ":
                i += 1
            l = i

        i += 1

    # Adding the last word to the stack
    stack.append(s[l:r+1])

    # Updating the input string by adding the words in the reverse order
    s = ""
    words_count = len(stack)
    for i in range(words_count):
        if i == words_count-1:
            word = stack.pop()
        else:
            word = stack.pop() + " "
        s += word

    return s

def better_approach(s: str) -> str:
    """
        - Using Auxiliary DS (list for easier reversing)
        - Complexity Analysis:
            - Time -> O(n + n) ~= O(n)
            - Space -> O(n+n)

    """
    n = len(s)
    arr = []

    # striping the leading spaces
    l = 0
    while l < n:
        if s[l] == " ":
            l += 1
        else:
            break

    # String the trailing spaces
    r = n-1
    while r >= 0:
        if s[r] == " ":
            r -= 1
        else:
            break

    # Capturing the words and adding to the stack
    i = l+1
    while i <= r:
        if s[i] == " ":
            arr.append(s[l:i])
            while s[i] == " ":
                i += 1
            l = i

        i += 1

    # Adding the last word to the stack
    arr.append(s[l:r+1])

    # Updating the input string by adding the words in the reverse order
    arr.reverse()
    return " ".join(arr)


def better_approach2(s: str) -> str:
    """
        - Slightly cleaner approach, still uses auxiliary DS (list for storing words)
        - Complexity Analysis:
            - Time -> O(n + n) ~= O(n)
            - Space -> O(n+n)
    """
    arr = []
    word = ""

    for c in s:
        if c != " ":
            word += c
        elif c == " " and word:
            arr.append(word)
            word = ""

    if word:
        arr.append(word)

    arr.reverse
    return " ".join(arr)


def optimal_approach(s: str) -> str:
    """
        - Traversing from end of the string
        - Complexity Analysis:
            - Time -> O(n + n)
            - Space -> O(n)
    """
    n = len(s)
    res = ""

    i = n-1
    while (i >= 0):
        while i >= 0 and s[i] == " ":
            i -= 1

        if i < 0:
            break

        end = i

        while i >= 0 and s[i] != " ":
            i -= 1

        word = s[i+1:end+1]
        if res:
            res += "" + word
        else:
            res += word
    
    return res

if __name__ == "__main__":
    s = "welcome to the  jungle"
    # s = " amazing coding skills "
    # s = "  hello world  "
    # print(brute_force(s))
    print(better_approach(s))
