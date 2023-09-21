"""
Remove deplicates from the string
"""


def remove_duplicates(s: str) -> str:
    if not isinstance(s, str):
        raise ValueError("Argument 's' must be a 'str' object")
    
    seen = set()
    output = []
    for char in s:
        if char not in seen:
            seen.add(char)
            output.append(char)
    return "".join(output)


if __name__ == "__main__":
    input_str = "banana"
    # input_str = " "

    print(remove_duplicates(input_str))