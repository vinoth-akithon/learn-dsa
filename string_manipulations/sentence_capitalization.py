"""
Capitalize all the words in the give string
"""
import re

def capitalize(s: str) -> str:
    if not isinstance(s, str):
        raise ValueError("Argument 's' must be 'str' object")
    if not s:
        raise ValueError("Empty string found") 
    
    words = re.sub("\s+", " ", s).strip().replace(r'\s+', ' ').split(" ")

    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return " ".join(words)




if __name__ == "__main__":
    input_str = "   I am the best               in the world"
    # input_str = "  "

    print(capitalize(input_str))

