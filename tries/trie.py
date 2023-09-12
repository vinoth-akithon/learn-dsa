# trie Using hash table
from tries_using_hash_table import Node

class Trie(object):
    def __init__(self, root_node: Node) -> None:
        self.__root: Node = root_node


    def insert(self, word: str) -> None:
        current = self.__root
        for char in word:
            if not current.has_child(char):
                current.add_child(char)
            current = current.get_child(char)
        current.is_end = True
    

    def contain(self, word: str) -> bool:
        if not isinstance(word, str):
            raise ValueError("Argument 'word' should be 'str' type")
        
        current = self.__root
        for char in word:
            if not current.has_child(char):
                return False
            current = current.get_child(char)
        return current.is_end
    

    def traverse(self) -> None:
        self.__traverse(self.__root)


    def __traverse(self, root: Node) -> None:
        #  Pre order traveral
        print(root.get_char) # (process root at first)
        children = root.get_children()
        for child in children:
            self.__traverse(child)
 
        # # Post order traversal # (if process root at last)
        # print(root.get_char)


    def remove(self, word: str) -> None:
        if not isinstance(word, str):
            raise ValueError("Argument 'word' should be 'str' type")
        self.__remove(self.__root, word, 0)


    def __remove(self, root: Node, word: str, index: int) -> None:
        # Base condition
        if index == len(word):
            root.is_end = False
            return
        
        char = word[index]
        child = root.get_child(char)
        if child is None: return
        
        self.__remove(child, word, index + 1)
        if child.has_empty_children and not child.is_end:
            child.remove_child(char)


    def __find_last_node(self, word: str) -> Node | None:
        current = self.__root
        for char in word:
            child = current.get_child(char)
            if child is None:
                return 
            current = child
        return current
    

    def auto_completion(self, word: str) -> list[str]:
        words = []
        last_node = self.__find_last_node(word)
        if last_node:
            self.__auto_completion(last_node, word, words)
        return words
        
    
    def __auto_completion(self, root: Node, word: str, words: list):
        if root.is_end:
            words.append(word)
        
        childrens = root.get_children()
        for child in childrens:
            self.__auto_completion(child, word+child.get_char, words)
        

# trie Using array
# from tries_using_array import Node



# Trie instantiation
tries = Trie(root_node=Node(""))

# Insert opertaion
tries.insert("care")
tries.insert("card")
tries.insert("carful")
tries.insert("egg")

# Traversing 
# tries.traverse()

# Deletion
tries.remove("cargo")

# Lookup 
# print(tries.contain("car"))
# print(tries.contain("care"))

# Autocompletion or Prefix search
print(tries.auto_completion(""))

print("Done")