from typing import Self

class Node(object):
    def __init__(self, char: str|None =None) -> None:
        self.__value = char
        self.__children = {}
        self.is_end = False

    @property
    def get_char(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return f"Value: {self.__value}"
    
    def has_child(self, char) -> bool:
        return self.__children.__contains__(char)
    
    def get_child(self, char) -> Self:
        return self.__children.get(char)
    
    def add_child(self, char) -> None:
        self.__children[char] = Node(char)

    def get_children(self) -> list[Self]:
        return list(self.__children.values())
    
    @property
    def has_empty_children(self) -> bool:
        return self.__children == {}
    
    def remove_child(self, char) -> None:
        self.__children.pop(char, None)