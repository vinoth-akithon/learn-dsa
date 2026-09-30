- This is not a typical algo.
- It's a constructive algo requires concept understanding instead memorization.
- Useful when we need the solution of consecutive subarray or substring with some condition.
- Types:
  - Fixed size window (window size `k` is provided)
    - max/min sum or avg subarray size `k`.
    - Maximum points from cards.
  - Dynamic size window (window size `k` is not provided)
    - Smallest subarray whose sum is equal to `k`.
    - Longest subarray whose sum is equal to `k`.
    - Longest Substring without repeating char.
    - Longest substring with repeating char but `k` distinct char.
    - Fruit into baskets (Longest substring with repeating char but k=2 distinct char)
    - Longest repeating char after replacement of `k` char.
    - Longest subarray ones after replacement of `k` zeros (same to longest repeating char after replacement of `k` char).
    - Maximum consecutive ones



Maximum sum subarray of size k
-------------------------------
n = array size
k = window size
total_windows = n - k + 1

Brute force approach:
---------------------
- Use nested loops to get all possible windows.
- Whenever the current window sum is max than the tracked one, update the tracked one.
- finally return the tracked one.


Optimal approch using sliding window
------------------------------------
function solution(arr, k) {
  n = array size
  k = window size
  current_window_sum = 0

  for (from 0 to k) {
    current_window_sum += arr[e]
  }

  max_sum = max(current_sum)
  s = 0

  for (from k to n) {
    current_sum += arr[e]
    current_sum -= arr[s]
    s -= 1
    if max(current_sum) > max_sum {
      max_sum > current_sum
    }

  }

}


- Target Value Identification
- Longest/shorest/most optimal sequences
- Formulating Adjacent pairs
- Running Average 
  - Calculating average of fixed size window as new elements arrives in the stream of data.

- Main idea behind the SW reduces time complexit from O(n^2) or O(n^3) to O(n)
- Both fixed and variable size window problems can use 
  - Hashing (for tracking elements in the window as it provides efficient lookup)
  - Two pointers (for tracking the elements in the window by start and end pointers)
  - Sliding window optimization (Uses both Hashing and two poniters)
