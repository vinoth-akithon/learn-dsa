from linked_list import LinkedList

class Entry:
    def __init__(self, key: int, value: str) -> None:
        self.key = key
        self.value = value

    # def __str__(self):
    #     return str(f'{self.key}={self.value}')
    
    def __repr__(self) -> str:
        return str(f'{self.key}={self.value}')

entry = Entry(1, "eee")
print(entry)

class HashTable:

    def __init__(self, size) -> None:
        self.__size = size
        self.__hash_table = [None for _ in range(size)] 

    def __get_hash(self, key):
        return key % self.__size

    def put(self, key: int, value: str) -> None:
        index = self.__get_hash(key)
        if self.__hash_table[index] is None:
            self.__hash_table[index] = LinkedList()
        
        bucket = self.__hash_table[index]
        for entry in bucket.to_list():
            if entry.key == key:
                print(key)
                entry.value = value
                return
        bucket.add_last(Entry(key, value))

    def get(self, key: int) -> str:
        index = self.__get_hash(key)

        if self.__hash_table[index] is not None:
            for entry in self.__hash_table[index].to_list():
                if entry.key == key:
                    return entry.value
        
        raise KeyError(f"'{key}' not exist") 

    def remove(self, key: int) -> str:
        index = self.__get_hash(key)
        
        if self.__hash_table[index] is not None:
            bucket = self.__hash_table[index].to_list()
            
            for entry in bucket:
                if entry.key == key:
                    returned_entry = self.__hash_table[index].remove(entry)
                    if returned_entry:
                        if self.__hash_table[index].size == 0:
                            self.__hash_table[index] = None
                        return returned_entry.value
                    return 
                
        return KeyError(f"'{key}' not exist")
    def __str__(self):
        return str(self.__hash_table)


# hash_table = HashTable(5)
# print(hash_table)

# hash_table.put(1, "vinoth")
# print(hash_table.get(1))

# hash_table.put(2, "veeram")
# print(hash_table.get(2))

# hash_table.put(6, "aki")
# print(hash_table.get(6))

# print(hash_table.remove(2))