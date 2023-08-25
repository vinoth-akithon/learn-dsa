def find_first_repeating_char_in_str(input_str: str) -> str | None:
    hash_table = set()
    for char in input_str:
        if char in hash_table:
            return char
        hash_table.add(char)
    return None

print(find_first_repeating_char_in_str("green apple"))