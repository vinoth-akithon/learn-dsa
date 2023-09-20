"""
Count the vowels in the given string
"""


def count_vowel(s: str) -> int:
    if not isinstance(s, str):
        raise ValueError(f"Argument 's' should be a 'str' object")
    
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1

    return count



if __name__ == "__main__":
    # input_string = "I am bets in the World."
    input_string = ""
    print(count_vowel(input_string))