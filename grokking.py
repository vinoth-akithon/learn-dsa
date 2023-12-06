"""
Intro
------
    - This course is catogories interview problems in
    16 set (150 problems) of patterns.
    - It will cover DFS, BFS, Backtracking, Dynamic programming,
    Greedy algo, Recursion, Devide and Conquer.

Pattern 1: Sliding Window
------------------------
    - Many times dealing with array, we are given to calculate something
    among all the contiguous subarray of given size.

    - Ex:
        Given an array, find the average of all contiguous 
        subarrays of size K in it.

    - We need to iterate until we get first window, then we 
    need to slide the window one step by adding next element
    and removing the first element to form a window.

    - For the above problem size of the window fixed (K),
    but some problems, size is not fixed, we have to expand or 
    shrink window based on prolem constrains. 


"""
