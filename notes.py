"""

>> Data types
    - It deals with classification and characteristics of individual data items

>> Data Structure
    - It deals with how collection of data items are organised and accessed in memeory
    - It allowing the efficient operation like searching, accessing, inserting and removing

>> Linear data structure 
    Array
    Linked list
    Stacks
    Queues
    Hash tables

>> Non-linear data structure
    Trees
    Graphs


>> Big O notation
    - used to describe the performance of the algorithms
    - to analyze both time(runtime) and space complexity
    - constant growth O(1)
        def print_something(n: list):
            # O(1) the time taken is not depends upon input.
            print(n[0])

    - linear growth O(n)
        def print_something(n: list):
            for item in n:
                print(item)

    - quadratic growth O(n^2)
        def print_something(n: list):
            for item1 in n:
                for item2 in n:
                    print(item1 + item2)

    - logarithmic O(log(n))
    - exponentail growth O(2^n)
    
    
>> Array
    - fundamental data structure.
    - most programming languages, arrays have a fixed size.
    - some programming languages, provides dynamic arrays or resizable arrays.
    - deleting and inserting a new element at the end of array is less costy [O(1)].
    - deleting and inserting a new element at the middle of the array is more costly [O(n)], here shifting takes place.

    Key charactaristics
        - storing a collection of similar data type (Hemogeneous).
        - stored in contiguous memory location (like 1,2,3...).
        - each element accessed through its index (starts with 0).
        - useful when the size of the collection is known and fixed.
        - useful for implementing 'queues' and 'stack' data structure.
        - useful for representing matrices and multi dimentaion data.

    Limitations:
        - fixed size
        - costly insertion and deletion
        - inefficent resizing

    Address Limitations:
        - linked list 
        - dynamic array
        - hash tables

    
    
"""