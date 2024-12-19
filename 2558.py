import heapq

# Convert the gifts array into a max heap by negating the values
# Negation is necessary because heapq in Python is a min-heap by default

def pickGifts(gifts, k):  # beat 95.46% using max heap
    maxHeap = [-x for x in gifts]
    heapq.heapify(maxHeap)

    for i in range(k):
        value = int((-maxHeap[0]) ** 0.5)   # Floor of the square root of the largest gift
        # Replace the root of the heap (largest value) with the new value
        # heapreplace() efficiently removes the root and adds the new value in O(log n) time
        heapq.heapreplace(maxHeap, -value)
    sum = 0
    for num in maxHeap:
        sum += -num

    return sum
