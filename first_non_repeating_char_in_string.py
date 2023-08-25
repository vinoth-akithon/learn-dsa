def find_first_non_repeating_char_in_str(input_str: str):
    hash_table = dict()

    for item in input_str:
        if item == " ":
            continue
        elif item in hash_table:
            hash_table[item] += 1
        else:
            hash_table[item] = 1
    
    # This won't for this problem because hash function doesn't follow contigous memory location
    # for key, value in hash_table.items( ):
    #     if value == 1:
    #         return key

    for item in input_str:
        if item == " ":
            continue
        elif hash_table[item] == 1:
            return item
    return None

print(find_first_non_repeating_char_in_str("a green apple"))