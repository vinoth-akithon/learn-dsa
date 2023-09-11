from heapq import *


heap = []

# To push an item into heap
heappush(heap, 6)
heappush(heap, 3)
heappush(heap, 4)
heappush(heap, 5)
# To pop an item from heap
# heappop(heap)

# To perform push followed by pop (Efficient one for this)
# heappushpop(heap, 6)

# To perform pop followed by push (Efficient one for this)
# heapreplace(heap, 6)

# To merge the sorted iterables
# print(list(merge([1,3,5,7], [0,2,4,8,2], [5,10,15,20], [], [25])))

# To find n largest elements
# print(nlargest(2, heap))

# To find n smallest elements
# print(nsmallest(2, heap))

print(heap)