
from typing import Self

class Node(object):
    def __init__(self, char: str|None =None) -> None:
        self.__value = char
        self.__children = [None for _ in range(26)]
        self.is_end = False

    def __repr__(self) -> str:
        return f"Value: {self.__value}"
    
    def __get_index(self, char) -> int:
        return ord(char) - ord("a")
    
    def has_child(self, char) -> bool|None:
        return self.__children[self.__get_index(char)]
    
    def get_child(self, char) -> Self:
        return self.__children[self.__get_index(char)]
    
    def add_child(self, char) -> None:
        self.__children[self.__get_index(char)] = Node(char)