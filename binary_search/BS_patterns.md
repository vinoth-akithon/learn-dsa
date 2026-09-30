# BINARY SEARCH MASTERY — Pattern-First Learning Path

---

# PHASE 1 — BUILD THE MENTAL MODEL

---

## Lesson 1.1 — What Binary Search Actually Is

---

### The Wrong Mental Model (Most People Have This)

> "Binary Search = searching for a number in a sorted array"

This is **dangerously incomplete**. It will make you miss 80% of Binary Search problems.

---

### The Correct Mental Model

> **Binary Search = systematically eliminating half the search space at each step, given a monotonic condition.**

The array is just one *instance* of a search space. The real insight is:

```
If you can answer: "Should I go left or right from here?"
Then you can Binary Search.
```

---

### Real-World Analogy — The Dictionary

Imagine finding the word **"Manifest"** in a physical dictionary.

You don't start from page 1. You:

1. Open to the **middle** → land on "M" → "Manifest" must be here or to the right
2. Open to **middle of right half** → land on "Mo" → "Manifest" is to the left
3. Repeat until found

**What made this possible?**
- The dictionary is **sorted** (monotonic ordering)
- At each step, you could **eliminate half** the remaining pages
- You knew **which direction** to go

This is Binary Search. The "dictionary" is your search space.

---

### Visual Explanation

```
Search Space: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
               ^                                 ^
               lo                               hi

Step 1: mid = index 4 → value 9
        Target = 13
        9 < 13 → eliminate LEFT half

Search Space: [11, 13, 15, 17, 19]
               ^               ^
               lo             hi

Step 2: mid = index 7 → value 15
        15 > 13 → eliminate RIGHT half

Search Space: [11, 13]
               ^   ^
               lo  hi

Step 3: mid = index 5 → value 11
        11 < 13 → eliminate LEFT

Search Space: [13]
Found.
```

**Key Observation:** Each step doesn't "search" — it **eliminates**.

---

### The Three Core Ingredients

```
┌─────────────────────────────────────────────────────────┐
│  Binary Search requires:                                │
│                                                         │
│  1. SEARCH SPACE — a defined range of possibilities     │
│  2. MONOTONICITY — a condition that changes in ONE      │
│                    direction across the space           │
│  3. ELIMINATION — ability to discard half at each step  │
└─────────────────────────────────────────────────────────┘
```

---

### Preconditions for Binary Search

| Precondition | Explanation | Example |
|---|---|---|
| **Defined search space** | You know lo and hi | Array indices, answer range |
| **Monotonic property** | F(x) flips from False→True or True→False exactly once | sorted array, feasibility |
| **Deterministic direction** | At any mid, you know which half to discard | mid < target → go right |

---

### Hidden Search Spaces (This is Where Most People Fail)

The search space is **not always an array index**. It can be:

```
┌──────────────────────────────────────────────────────────┐
│  SEARCH SPACE TYPES                                      │
│                                                          │
│  1. Array indices        → [lo=0, hi=n-1]               │
│  2. Answer values        → [lo=min_possible, hi=max]    │
│  3. Continuous range     → [lo=0.0, hi=1.0]             │
│  4. Matrix positions     → mapped to 1D                  │
│  5. Time/Capacity values → [1, 10^9]                    │
└──────────────────────────────────────────────────────────┘
```

**Example of hidden search space:**

> "What is the minimum speed at which a worker can complete tasks within D days?"

Search space = **speed values** from 1 to max_task_size.
Not an array. Not indices. Pure answer space.

---

### When Binary Search Should NOT Be Used

```
❌ Unsorted data with no monotonic property
❌ Search space cannot be defined with lo/hi
❌ At mid, you cannot determine which side the answer is on
❌ You need ALL solutions (not just one boundary or value)
❌ The condition is not monotonic (flips multiple times)
```

**Counter-intuitive example where BS fails:**
> "Find the peak in an array where values go up, down, up, down..."
> → Multiple peaks → NOT monotonic → NOT Binary Search (in standard form)

But:
> "Find ANY peak in an array where arr[i] ≠ arr[i+1]"
> → At any point, going toward the higher neighbor guarantees a peak
> → **IS Binary Search** (direction-based elimination)

---

### The Generic Binary Search Template

This is the **foundation**. Every pattern is a specialization of this.

```python
def binary_search(lo, hi):
    while lo <= hi:              # or lo < hi depending on pattern
        mid = lo + (hi - lo) // 2   # prevents overflow
        
        if condition(mid):
            # Option A: found answer, return
            # Option B: try to do better (go left or right)
            hi = mid - 1        # or hi = mid
        else:
            lo = mid + 1        # or lo = mid + 1
    
    return lo   # or hi, or -1, depending on what you seek
```

**The three questions to answer before coding:**

```
1. What is lo and hi? (Define search space)
2. What is the condition at mid? (Define monotonic check)
3. What do I return? (lo, hi, mid, -1?)
```

---

### Complexity

```
Time:  O(log N) — halving at each step
Space: O(1)     — no extra space needed
                  (O(log N) for recursive, but iterative is preferred)
```

---

## ✅ Checkpoint 1.1

Before moving forward, answer these:

```
Q1. A problem asks: "Find minimum bandwidth such that 
    all files can be transferred in T hours."
    → Is this Binary Search? What is the search space?

Q2. A problem asks: "Find all pairs in array that sum to K."
    → Is this Binary Search? Why or why not?

Q3. What are the 3 core ingredients Binary Search needs?
```

**Answer these before I continue to Phase 2.**

---
---

# PHASE 2 — BINARY SEARCH PATTERNS

---

## PATTERN 1 — Exact Match

---

### Problem Signature

```
"Find the exact position/existence of a target value"
"Does X exist in the collection?"
"Find the index of X"
```

---

### Recognition Clues

```
✅ Sorted array (or sortable structure)
✅ Looking for a specific value
✅ Return index or -1
✅ No optimization involved ("minimum" or "maximum" not in the problem)
```

---

### The Invariant

> **The target, if it exists, always lies within [lo, hi]**

This invariant must hold after every update to lo and hi.

```
Before step:  target ∈ [lo, hi]
After step:   target ∈ [lo, hi]  ← must still be true
```

If mid is not the target:
- `arr[mid] < target` → target is in [mid+1, hi] → `lo = mid + 1` ✓
- `arr[mid] > target` → target is in [lo, mid-1] → `hi = mid - 1` ✓

---

### Visual Dry Run

```
arr = [2, 5, 8, 12, 16, 23, 38, 45]
target = 23

Step 1: lo=0, hi=7, mid=3 → arr[3]=12
        12 < 23 → lo = 4

Step 2: lo=4, hi=7, mid=5 → arr[5]=23
        23 == 23 → FOUND at index 5
```

---

### Variants Within Pattern 1

#### Variant A — Standard Search (exists or not)

```python
def search(arr, target):
    lo, hi = 0, len(arr) - 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if arr[mid] == target:
            return mid          # exact match found
        elif arr[mid] < target:
            lo = mid + 1        # eliminate left half
        else:
            hi = mid - 1        # eliminate right half
    
    return -1                   # not found
```

#### Variant B — First Occurrence

**Why different?** When we find the target, we don't stop. We ask: "Is there an earlier occurrence?"

```
Invariant: answer (first position) is always in [lo, hi]
When arr[mid] == target: answer might be at mid or LEFT of mid
→ Record mid as candidate, then search LEFT
```

```python
def first_occurrence(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if arr[mid] == target:
            result = mid        # candidate found
            hi = mid - 1       # but look further LEFT
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return result
```

#### Variant C — Last Occurrence

```
When arr[mid] == target: answer might be at mid or RIGHT of mid
→ Record mid as candidate, then search RIGHT
```

```python
def last_occurrence(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if arr[mid] == target:
            result = mid        # candidate found
            lo = mid + 1       # but look further RIGHT
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return result
```

---

### Common Mistakes — Pattern 1

```
❌ Using lo < hi instead of lo <= hi
   → Misses the case when lo == hi (single element)

❌ Writing mid = (lo + hi) / 2
   → Integer overflow when lo + hi > INT_MAX
   → Always use: mid = lo + (hi - lo) // 2

❌ Forgetting to update lo/hi (infinite loop)
   → lo = mid (not mid+1) when target > arr[mid]

❌ Not handling empty array (lo > hi from start)
```

---

### Problems — Pattern 1

#### Easy

```
E1. Search in a sorted array — return index or -1
E2. Count occurrences of target — use first + last occurrence
E3. Check if array has a duplicate — search for arr[i] 
    where arr[i] appears at first_occ ≠ last_occ
```

#### Medium

```
M1. Search in sorted matrix (each row sorted)
    → Hint: treat matrix as flattened sorted array
    
M2. Find floor and ceiling of a target in sorted array
    → Floor: largest element ≤ target
    → Ceiling: smallest element ≥ target
    
M3. Count negative numbers in sorted 2D grid
    → Find first negative in each row using binary search
```

#### Hard

```
H1. Find target in sorted array with unknown size (infinite array)
    → Hint: first find bounds using exponential search
    
H2. Search in a nearly sorted array 
    (arr[i] may be at i-1, i, or i+1)
    → Modify comparison logic carefully
```

---

## PATTERN 2 — Boundary Search (First True / Last False)

---

### The Core Idea

This pattern handles the most important generalization of Binary Search.

Instead of searching for an **exact value**, we search for the **boundary** where a condition flips:

```
[F, F, F, F, T, T, T, T]
             ^
         first TRUE  ← lower bound

[T, T, T, T, F, F, F, F]
          ^
       last TRUE ← upper bound
```

---

### Monotonic Condition

The key requirement:

```
There exists some point k such that:
- For all x < k: condition(x) = False
- For all x ≥ k: condition(x) = True

This is MONOTONICITY: condition flips exactly ONCE.
```

If condition doesn't flip exactly once → Binary Search breaks.

---

### The Two Sub-Patterns

#### Sub-Pattern 2A — Lower Bound (First True)

> "Find the first position where condition becomes True"

```
Array:     [F, F, F, F, T, T, T]
Indices:    0  1  2  3  4  5  6
                         ^
                    answer = 4
```

**Template:**

```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)       # hi = n, not n-1 (answer might be n)
    
    while lo < hi:             # NOTE: lo < hi, not lo <= hi
        mid = lo + (hi - lo) // 2
        
        if arr[mid] >= target: # condition: "is this ≥ target?"
            hi = mid           # mid might be answer, don't exclude it
        else:
            lo = mid + 1       # mid is definitely NOT answer
    
    return lo                  # lo == hi, converged to first True
```

**Why `lo < hi` here?**
Because when `lo == hi`, we've converged. One more iteration would be redundant.

**Why `hi = mid` (not `mid - 1`)?**
Because `mid` could BE the answer. We can't exclude it.

---

#### Sub-Pattern 2B — Upper Bound (Last True)

> "Find the last position where condition is True"

```
Array:     [T, T, T, T, F, F, F]
Indices:    0  1  2  3  4  5  6
                      ^
                 answer = 3
```

**Template:**

```python
def upper_bound(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if arr[mid] <= target:  # condition still True
            result = mid        # record and try going RIGHT
            lo = mid + 1
        else:
            hi = mid - 1
    
    return result
```

---

### The Unified Boundary Template

```python
def find_boundary(lo, hi, condition):
    """
    Find first index where condition(index) is True.
    Assumes: [False, False, ..., True, True, ...]
    """
    result = -1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if condition(mid):
            result = mid       # potential answer
            hi = mid - 1      # look for earlier True
        else:
            lo = mid + 1      # this is False, go right
    
    return result
```

---

### Visual Dry Run — Insert Position

```
arr = [1, 3, 5, 7, 9], target = 6
Find: first index where arr[index] >= 6

Index:  0  1  2  3  4
Value:  1  3  5  7  9
Cond:   F  F  F  T  T   (>= 6?)

Step 1: lo=0, hi=4, mid=2 → arr[2]=5, 5<6 → False → lo=3
Step 2: lo=3, hi=4, mid=3 → arr[3]=7, 7>=6 → True → hi=2
Step 3: lo=3 > hi=2 → stop

Answer: lo = 3 → insert at index 3
```

---

### Problems — Pattern 2

#### Easy

```
E1. Find insert position of target in sorted array (LeetCode 35)
E2. Lower bound — first element ≥ target
E3. Upper bound — first element > target
```

#### Medium

```
M1. Find first bad version (LeetCode 278)
    Condition: isBadVersion(mid) → first True
    
M2. First element in sorted array where arr[i] >= arr[i]*arr[i]
    (find where squared value crosses threshold)
    
M3. Minimize the maximum difference between heights (classic)
```

#### Hard

```
H1. Find smallest divisor given a threshold (LeetCode 1283)
    Condition: sum of ceil(arr[i]/d) <= threshold → find first True
    
H2. Koko eating bananas (LeetCode 875)
    Condition: can eat all bananas at speed k in h hours?
```

---

## PATTERN 3 — Answer Space Binary Search

---

### The Core Insight

> **Don't search through the array. Search through the ANSWER.**

Many optimization problems have this structure:

```
"Find the MINIMUM value of X such that some condition holds"
"Find the MAXIMUM value of X such that some condition holds"
```

These are **not** asking you to search an array. They're asking you to search through **possible answers**.

---

### The Transformation

```
Optimization Problem → Decision Problem

"What is the minimum speed S?"
↓  transform  ↓
"Is speed S feasible? (can we finish in time?)"

Now Binary Search on S from [min_possible, max_possible]
```

This is the most powerful and most hidden pattern.

---

### How to Identify Answer Space BS

```
Recognition clues:
✅ "Minimum possible X such that..."
✅ "Maximum possible X such that..."  
✅ "Minimize the maximum..."
✅ "Maximize the minimum..."
✅ Answer is a NUMBER (not an index)
✅ Feasibility can be checked in O(n) or O(n log n)
```

---

### Generic Template — Minimize Answer

```python
def solve():
    lo = minimum_possible_answer
    hi = maximum_possible_answer
    result = hi  # worst case
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if is_feasible(mid):    # can we achieve this?
            result = mid        # this works, try smaller
            hi = mid - 1
        else:
            lo = mid + 1        # doesn't work, need larger
    
    return result

def is_feasible(candidate):
    # Check if 'candidate' satisfies the problem constraints
    # Usually O(n) greedy check
    ...
```

---

### Generic Template — Maximize Answer

```python
def solve():
    lo = minimum_possible_answer
    hi = maximum_possible_answer
    result = lo  # worst case
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if is_feasible(mid):    # can we achieve this?
            result = mid        # this works, try larger
            lo = mid + 1
        else:
            hi = mid - 1        # too large, try smaller
    
    return result
```

---

### Visual Dry Run — Capacity Problem

**Problem:** Ship packages with weights [1,2,3,4,5,6,7,8,9,10] in 5 days. Find minimum ship capacity.

```
Search space: capacity from 10 (max single package) to 55 (all packages)
Condition: can_ship_in_5_days(capacity)

lo=10, hi=55

Step 1: mid=32
        Simulate: [1,2,3,4,5,6,7]=28≤32✓,[8]=8✓,[9]=9✓,[10]=10✓ → 4 days ≤ 5 → FEASIBLE
        result=32, hi=31

Step 2: mid=20
        Simulate: [1,2,3,4,5,6]=21>20, [1,2,3,4,5]=15✓,[6,7]=13✓,[8]=8✓,[9]=9✓,[10]=10✓ → 5 days → FEASIBLE
        result=20, hi=19

Step 3: mid=14
        ...simulate... → 6 days > 5 → NOT FEASIBLE
        lo=15

...continues...

Final answer: 15
```

---

### Key Insight: Designing the Feasibility Function

```
For allocation/capacity problems:
→ Greedily fill as much as possible
→ Count how many units (days/workers/boxes) needed
→ Compare to limit

def is_feasible(capacity, packages, max_days):
    days = 1
    current_load = 0
    for pkg in packages:
        if current_load + pkg > capacity:
            days += 1
            current_load = 0
        current_load += pkg
    return days <= max_days
```

---

### Problems — Pattern 3

#### Easy

```
E1. Find square root of N (integer part) — search space [1, N]
E2. Find cube root of N — search space [1, N]  
E3. Koko eating bananas (875) — speed search space [1, max(pile)]
```

#### Medium

```
M1. Ship packages within D days (1011)
    → Capacity search space [max_weight, sum_weights]
    
M2. Minimize maximum pages (book allocation)
    → Pages search space [max_pages, total_pages]
    
M3. Split array largest sum (410)
    → Sum search space [max_element, total_sum]
```

#### Hard

```
H1. Painter's partition problem
    → Same structure as book allocation, generalized
    
H2. Aggressive cows / Maximum minimum distance (SPOJ)
    → "Maximize the minimum distance between cows"
    → Search on distance, check if K cows can be placed
```

---

## PATTERN 4 — Predicate Binary Search

---

### How It Differs from Pattern 3

Pattern 3: **"What is the optimal value X?"**
Pattern 4: **"Can we achieve X? Is X possible?"**

Pattern 4 focuses on designing the **predicate (feasibility) function** correctly. The search space is given; the challenge is defining what "feasible" means.

---

### The Predicate Design Framework

```
Step 1: What are we testing? (the candidate mid)
Step 2: What does "feasible" mean for this candidate?
Step 3: How to verify feasibility in O(n)?
Step 4: Is the predicate monotonic? 
        (if feasible at X, is it feasible at X+1 or X-1?)
```

---

### Template

```python
def predicate_binary_search(arr, k):
    lo = define_lower_bound()
    hi = define_upper_bound()
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if feasible(arr, mid, k):
            # Feasible: explore for better answer
            lo = mid + 1    # or hi = mid - 1 depending on maximize/minimize
        else:
            hi = mid - 1    # or lo = mid + 1
    
    return hi   # or lo
```

---

### Example: Aggressive Cows

**Problem:** Place C cows in stalls at positions [1,2,4,8,9]. Maximize the minimum distance between any two cows.

```
Predicate: can_place_cows(min_dist) → True/False

Observation: 
- Small min_dist → easier to place → True
- Large min_dist → harder to place → eventually False
- Monotonic: [T,T,T,...,F,F,F]
- We want LAST True → maximize answer

Feasibility check:
def can_place(stalls, C, min_dist):
    count = 1
    last = stalls[0]
    for stall in stalls[1:]:
        if stall - last >= min_dist:
            count += 1
            last = stall
    return count >= C

Search space: [1, max_stall - min_stall]
```

---

### Problems — Pattern 4

#### Easy

```
E1. Can binary string be split into K parts each with equal 1s?
E2. Is it possible to pick K numbers from array with sum ≤ S?
```

#### Medium

```
M1. Kth smallest element in sorted matrix (378)
    Predicate: count of elements ≤ mid
    
M2. Find Kth smallest pair distance (719)
    Predicate: count pairs with distance ≤ mid
```

#### Hard

```
H1. Minimizing maximum of array after K operations (2439)
H2. Swim in rising water (778)
    Predicate: can we reach destination if max water level is mid?
```

---

## PATTERN 5 — Rotated Array

---

### The Problem With Rotation

A rotated sorted array looks like:

```
Original: [1, 2, 3, 4, 5, 6, 7]
Rotated:  [4, 5, 6, 7, 1, 2, 3]
                   ^
              rotation point
```

Binary Search breaks because the array isn't fully sorted. But **one half is always sorted**.

---

### The Key Insight: Detect the Sorted Half

```
At any mid point in a rotated array:
→ Either the LEFT half [lo..mid] is sorted
→ Or the RIGHT half [mid..hi] is sorted
→ ALWAYS exactly one of these is true

How to check:
→ LEFT is sorted if arr[lo] <= arr[mid]
→ RIGHT is sorted if arr[mid] <= arr[hi]
```

Once you know which half is sorted, you can check if the target is in that half. If yes, go there. If no, go to the other half.

---

### Visual Dry Run

```
arr = [4, 5, 6, 7, 0, 1, 2], target = 0

Step 1: lo=0, hi=6, mid=3 → arr[3]=7
        Left half [4,5,6,7]: arr[0]=4 ≤ arr[3]=7 → LEFT IS SORTED
        Is target 0 in [4,7]? NO → go RIGHT
        lo = 4

Step 2: lo=4, hi=6, mid=5 → arr[5]=1
        Left half [0,1]: arr[4]=0 ≤ arr[5]=1 → LEFT IS SORTED
        Is target 0 in [0,1]? YES → go LEFT
        hi = 4

Step 3: lo=4, hi=4, mid=4 → arr[4]=0
        Found! Return 4
```

---

### Template — Search in Rotated Array

```python
def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if arr[mid] == target:
            return mid
        
        # Determine which half is sorted
        if arr[lo] <= arr[mid]:        # LEFT half is sorted
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1          # target in sorted left half
            else:
                lo = mid + 1          # target in right half
        else:                          # RIGHT half is sorted
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1          # target in sorted right half
            else:
                hi = mid - 1          # target in left half
    
    return -1
```

---

### Variant — Find Minimum in Rotated Array

```
Observation: Minimum is at the rotation point.
The minimum is always in the UNSORTED half.

[4, 5, 6, 7, 1, 2, 3]
              ^
           minimum

If arr[mid] > arr[hi]: minimum is in RIGHT half → lo = mid + 1
If arr[mid] < arr[hi]: minimum is in LEFT half (including mid) → hi = mid
```

```python
def find_min_rotated(arr):
    lo, hi = 0, len(arr) - 1
    
    while lo < hi:
        mid = lo + (hi - lo) // 2
        
        if arr[mid] > arr[hi]:
            lo = mid + 1   # min is in right half
        else:
            hi = mid       # mid could be the min
    
    return arr[lo]
```

---

### Problems — Pattern 5

#### Easy

```
E1. Find minimum in rotated sorted array (153)
E2. Determine if array is rotated sorted
```

#### Medium

```
M1. Search in rotated sorted array (33)
M2. Search in rotated sorted array II — with duplicates (81)
    (duplicates break the sorted-half detection, need special case)
```

#### Hard

```
H1. Find rotation count in rotated sorted array
H2. Search in double rotated array
```

---

## PATTERN 6 — Peak / Mountain

---

### Core Idea

A peak element is one that is **greater than its neighbors**.

```
[1, 3, 5, 4, 2]
         ^
       peak = 5
```

**Why Binary Search?**

At any mid, look at neighbors:
- `arr[mid] < arr[mid+1]` → peak is to the RIGHT (ascending, must go up)
- `arr[mid] > arr[mid+1]` → peak is to the LEFT or at mid (descending)

**This is direction-based elimination.**

---

### The Invariant

> If we go toward the higher neighbor, we will always find a peak. A peak must exist in the chosen half because the array can't keep increasing forever.

---

### Template — Find Peak Element

```python
def find_peak(arr):
    lo, hi = 0, len(arr) - 1
    
    while lo < hi:
        mid = lo + (hi - lo) // 2
        
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1   # ascending → peak is right
        else:
            hi = mid       # descending → peak is left (or at mid)
    
    return lo   # lo == hi, this is the peak
```

---

### Variant — Mountain Array Maximum

```
Mountain: increases then decreases
[1, 3, 8, 5, 2]

Same logic: go toward higher neighbor
```

---

### Problems — Pattern 6

#### Easy

```
E1. Find peak element (162) — any peak, not maximum
E2. Mountain array peak index (852)
```

#### Medium

```
M1. Find in mountain array (1095)
    → First find peak, then search both sides
    
M2. Longest mountain in array
```

#### Hard

```
H1. Minimum number of removals to make mountain array (1671)
```

---

## PATTERN 7 — Binary Search on Continuous Values

---

### When Integers Aren't Enough

Some problems require finding a real number answer:

```
"Find square root with precision 1e-6"
"Find optimal probability"
"Find exact split point"
```

The search space is **continuous (real numbers)**, not discrete.

---

### The Key Difference

```
Discrete BS:   lo, hi are integers → converges when lo > hi
Continuous BS: lo, hi are floats → converge when hi - lo < epsilon
```

---

### Template — Floating Point Binary Search

```python
def continuous_binary_search(lo, hi, epsilon=1e-7):
    # Run for fixed iterations to avoid float precision issues
    for _ in range(100):    # 100 iterations → precision of 2^-100
        mid = (lo + hi) / 2
        
        if condition(mid):
            hi = mid
        else:
            lo = mid
    
    return lo   # converged answer
```

**Why 100 iterations instead of `while lo < hi - epsilon`?**

Floating point arithmetic can cause infinite loops. Fixed iterations are safer and always precise enough.

---

### Example — Square Root

```python
def sqrt(n, epsilon=1e-7):
    lo, hi = 0, max(1, n)
    
    for _ in range(100):
        mid = (lo + hi) / 2
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid
    
    return lo
```

---

### Problems — Pattern 7

#### Easy

```
E1. Square root with precision (69 - integer version)
E2. Cube root with precision
```

#### Medium

```
M1. Nth root of a number with precision 1e-6
M2. Find smallest value such that sum of distances ≤ threshold
```

#### Hard

```
H1. Maximum average subarray II (644)
    (Binary search on the average value — requires clever feasibility check)
```

---

## PATTERN 8 — Multi-Dimensional Binary Search

---

### The Mapping Insight

A 2D matrix can be treated as a 1D array:

```
Matrix (m × n):
[1,  3,  5]
[7,  9,  11]
[13, 15, 17]

1D index i → row = i // n, col = i % n
```

---

### Template — Search in Sorted Matrix

```python
def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        # Convert 1D index to 2D
        row, col = mid // n, mid % n
        val = matrix[row][col]
        
        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return False
```

---

### Variant — Row-Wise and Column-Wise Sorted Matrix

When each row is sorted AND each column is sorted, but rows aren't connected:

```
Strategy: Start from top-right corner
- If value > target: move left (col--)
- If value < target: move down (row++)
- This is NOT binary search but similar elimination logic
```

---

### Problems — Pattern 8

#### Easy

```
E1. Search a 2D Matrix (74) — rows are connected
E2. Count negatives in sorted grid (1351)
```

#### Medium

```
M1. Search a 2D Matrix II (240) — rows/cols sorted independently
M2. Kth smallest in sorted matrix (378)
    (Binary search on VALUE, not index)
```

#### Hard

```
H1. Kth smallest product of two sorted arrays (2040)
```

---
---

# PHASE 3 — PATTERN RECOGNITION TRAINING

---

I'll now give you 5 problems. For each one, DO NOT look for the solution. Instead, answer the 5 diagnostic questions.

---

### Training Problem 1

> You have an array of integers. You want to find the minimum number of operations to make all elements equal, where one operation increments or decrements an element by 1. What's the optimal target value?

**Answer these before I respond:**

```
1. What is the search space?
2. Is there monotonicity? What does the cost function look like?
3. Is this exact match or answer search?
4. What invariant would you maintain?
5. Can the search space shrink by half each step?
```

---

### Training Problem 2

> Given a sorted array of distinct integers, find the index i where arr[i] == i. If multiple exist, find the first.

```
1. What is the search space?
2. What is the monotonic property?
3. Exact match or boundary?
4. What condition do you check at mid?
5. What do you return?
```

---

### Training Problem 3

> You have N ropes. Cut them into K pieces of equal length. Maximize the length of each piece.

```
1. What is the search space?
2. What is the feasibility condition?
3. Minimize or maximize the answer?
4. How do you check if length L is achievable?
5. What are the bounds of the search space?
```

---
---

# PHASE 4 — BUILD BINARY SEARCH INSTINCT

---

## Decision Tree

```
┌─────────────────────────────────────────────────────────────┐
│              BINARY SEARCH DECISION TREE                   │
└─────────────────────────────────────────────────────────────┘

Is the problem asking to FIND something?
│
├── YES: Is the data SORTED or can you DEFINE a range?
│        │
│        ├── Sorted Array + Find exact value?
│        │   → PATTERN 1 (Exact Match)
│        │
│        ├── Find FIRST/LAST position where condition holds?
│        │   → PATTERN 2 (Boundary Search)
│        │
│        └── Find INDEX in rotated array?
│            → PATTERN 5 (Rotated Array)
│
└── NO: Is it OPTIMIZE something (min/max)?
         │
         ├── "Minimize maximum" or "Maximize minimum"?
         │   → PATTERN 3 or 4 (Answer Space / Predicate)
         │
         ├── "Can we achieve X?" feasibility?
         │   → PATTERN 4 (Predicate)
         │
         ├── Peak element or mountain?
         │   → PATTERN 6 (Peak/Mountain)
         │
         ├── Precision / real number answer?
         │   → PATTERN 7 (Continuous)
         │
         └── 2D matrix with sorted property?
             → PATTERN 8 (Multi-Dimensional)
```

---

## One-Page Cheat Sheet

```
┌────────────────────────────────────────────────────────────┐
│           BINARY SEARCH CHEAT SHEET                       │
├────────────┬───────────────────┬─────────────────────────┤
│ Pattern    │ Signature         │ Return                  │
├────────────┼───────────────────┼─────────────────────────┤
│ Exact      │ arr[mid]==target  │ mid or -1               │
│ First Occ  │ found → go left  │ result (updated)        │
│ Last Occ   │ found → go right │ result (updated)        │
├────────────┼───────────────────┼─────────────────────────┤
│ Lower Bnd  │ first True       │ lo (after lo<hi loop)   │
│ Upper Bnd  │ last True        │ result                  │
├────────────┼───────────────────┼─────────────────────────┤
│ Ans Space  │ is_feasible(mid) │ lo or result            │
│ Predicate  │ custom feasible  │ lo-1 or result          │
├────────────┼───────────────────┼─────────────────────────┤
│ Rotated    │ detect sorted    │ mid or -1               │
│            │ half, check      │                         │
│ Peak       │ go toward higher │ lo (lo==hi)             │
├────────────┼───────────────────┼─────────────────────────┤
│ Continuous │ float, 100 iters │ lo or hi                │
│ Matrix     │ map to 1D index  │ True/False              │
└────────────┴───────────────────┴─────────────────────────┘

KEY FORMULAS:
mid = lo + (hi - lo) // 2     ← always use this
lo <= hi  → use when exact match possible at single element
lo < hi   → use for boundary/peak (converge to single point)

BOUNDS:
Exact Match:   lo=0, hi=n-1
Lower Bound:   lo=0, hi=n
Answer Space:  lo=min_answer, hi=max_answer
```

---

## Common Mistakes Checklist

```
□ Using mid = (lo+hi)/2 instead of lo + (hi-lo)//2
□ Wrong loop condition (≤ vs <)
□ Using hi = mid-1 when hi = mid is needed (losing answer)
□ Forgetting to handle empty array or single element
□ Not verifying feasibility function is actually monotonic
□ Answer space bounds are too tight (missing edge answers)
□ Off-by-one in feasibility simulation
□ Integer overflow in feasibility multiplication
□ Returning wrong variable (lo vs hi vs result)
□ Infinite loop: lo = mid instead of lo = mid + 1
```

---
---

# PHASE 5 — MASTERY VALIDATION

---

## 50 Binary Search Problems by Pattern

```
PATTERN 1 — Exact Match (10 problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P01 [Easy]   Binary Search (LeetCode 704)
P02 [Easy]   First Bad Version (278)
P03 [Easy]   Sqrt(x) (69)
P04 [Easy]   Count occurrences of target in sorted array
P05 [Easy]   Find floor and ceiling in sorted array
P06 [Medium] Search in 2D Matrix (74)
P07 [Medium] Find target range (34)
P08 [Medium] Random Pick with Weight (528)
P09 [Hard]   Search in unknown-size sorted array
P10 [Hard]   Search in nearly sorted array

PATTERN 2 — Boundary Search (8 problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P11 [Easy]   Lower bound implementation
P12 [Easy]   Upper bound implementation
P13 [Easy]   Insert position (35)
P14 [Medium] First position of element ≥ target
P15 [Medium] Check if N and its double exist (1346)
P16 [Medium] H-Index II (275)
P17 [Hard]   Count of range sum (327)
P18 [Hard]   Find Kth smallest pair distance (719)

PATTERN 3 — Answer Space (10 problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P19 [Easy]   Koko eating bananas (875)
P20 [Easy]   Find square root with precision
P21 [Medium] Ship packages within D days (1011)
P22 [Medium] Split array largest sum (410)
P23 [Medium] Book allocation problem
P24 [Medium] Minimize maximum pages
P25 [Medium] Painter's partition problem
P26 [Hard]   Minimum time to finish all jobs (1723)
P27 [Hard]   Maximum performance of a team (1383)
P28 [Hard]   Find median from data stream (295)

PATTERN 4 — Predicate (6 problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P29 [Medium] Aggressive cows (SPOJ)
P30 [Medium] EKO — woodcutters (SPOJ)
P31 [Medium] Kth smallest in sorted matrix (378)
P32 [Hard]   Kth smallest product of two sorted arrays (2040)
P33 [Hard]   Swim in rising water (778)
P34 [Hard]   Maximum average subarray II (644)

PATTERN 5 — Rotated Array (6 problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P35 [Easy]   Find minimum in rotated sorted array (153)
P36 [Medium] Search in rotated sorted array (33)
P37 [Medium] Search in rotated sorted array II (81)
P38 [Medium] Find rotation count
P39 [Hard]   Find target in rotated and shifted array
P40 [Hard]   Minimum in rotated sorted array with duplicates

PATTERN 6 — Peak/Mountain (4 problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P41 [Easy]   Peak index in mountain array (852)
P42 [Medium] Find peak element (162)
P43 [Medium] Find in mountain array (1095)
P44 [Hard]   Minimum removals to make mountain array (1671)

PATTERN 7 — Continuous Values (3 problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P45 [Easy]   Nth root with 6 decimal precision
P46 [Medium] Minimize largest sum of arithmetic operations
P47 [Hard]   Split array with minimum largest sum (real-valued)

PATTERN 8 — Multi-Dimensional (3 problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P48 [Easy]   Search a 2D Matrix (74)
P49 [Medium] Search a 2D Matrix II (240)
P50 [Hard]   Kth smallest element in sorted matrix (378 — predicate approach)
```

---

## Graduation Test — 10 Unseen Problems

These are your final test. No hints. No pattern labels. You decide everything.

```
G01. You have a list of logs. Each log has a timestamp. 
     Find the first log after time T.

G02. N students, M chocolates. Each student gets a 
     contiguous chunk. Minimize the maximum chocolates 
     any student gets.

G03. An integer array where arr[i] = number of students 
     in class i. Split into exactly 3 groups with minimum 
     imbalance (max_group - min_group minimized).

G04. Find the Kth missing positive integer in a sorted array.

G05. Given sorted array, find the single non-duplicate element.
     (All others appear exactly twice.)

G06. A conveyor belt has packages. Each package weighs 1-100.
     Find minimum weight capacity to ship all in exactly D days.

G07. Array of gas stations with distances. Find minimum 
     tank size so you can travel the entire array adding 
     at most K stations.

G08. Find the median of two sorted arrays of sizes m and n.

G09. Count pairs (i,j) where j-i >= K and arr[j] >= arr[i].

G10. You have intervals [start, end]. Find minimum value X 
     such that X is covered by at least K intervals.
```

---

## How to Proceed

```
┌─────────────────────────────────────────────────────────┐
│  LEARNING SEQUENCE                                      │
│                                                         │
│  1. Answer Checkpoint 1.1 questions                    │
│  2. Work through Pattern 1 problems (E1, E2, E3)       │
│  3. I verify → then Pattern 1 medium/hard              │
│  4. Repeat for each pattern                            │
│  5. Phase 3 training problems → I evaluate reasoning   │
│  6. Phase 5 problems P1-P50 → one group at a time      │
│  7. Graduation test → solve independently              │
└─────────────────────────────────────────────────────────┘
```

---

**Start here:**

> **Answer the 3 questions from Checkpoint 1.1**
> Then tell me which pattern you want to dive into first, or I'll sequence them optimally for you.

The depth of each lesson adjusts to your answers. The goal is derivation, not memorization.