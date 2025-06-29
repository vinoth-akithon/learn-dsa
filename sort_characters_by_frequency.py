import string

def sort_characters_by_frequency(s: str) -> str:
    """
        - Using Bucket sort the charectors sets are constant.
        - s contains (lower case alphabet, uppercase alphabet, digits)
        - lower case alphabets start at 97 in ascii.
        - Upper case alphabets start at 65 in ascii
        - Digits start at 48 in ascii.
        - So, keep a array buckets (it's tuple of length 2, one for actual char and another one for frequency) totally 26(lower case)+ 26(upper case) + 10(digits)
        - Iterate the input str and pick a character and find its ordinal number and update the frequency in the bucket.
        - Finally sort the array based frequency.
        - Iterate the buckets and update the input str for returing result.
    """
    buckets = [
        *[[i, 0] for i in string.ascii_lowercase],
        *[[i, 0] for i in string.ascii_uppercase],
        *[[i, 0] for i in string.digits]
    ]
    
    for i in s:
        ordinal_value = ord(i)
        if ordinal_value >= 97: # lower case
            bucket = ordinal_value - 97
        elif ordinal_value >= 65: # upper case
            bucket = ordinal_value - 65 + 26
        else: # digits
            bucket = ordinal_value - 48 + 26 + 26

        buckets[bucket][1] += 1

    # sort based on frequency and reverse 
    buckets.sort(key= lambda i: i[1], reverse=True)

    res = ""
    for i in buckets:
        if not i[1]:
            return res
        res += i[0] * i[1]
    return res

if __name__ == "__main__":
    s = "tree"
    # s = "cccaaa"
    # s = "Aabb"
    s = "2a554442f544asfasssffffasss"
    print(sort_characters_by_frequency(s))