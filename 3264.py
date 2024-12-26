#Initial Solution:

import heapq
def getFinalState(nums, k, multiplier):  # only beat 9.14% in time complexity O(K * log(N)) 
    newArray = [x for x in nums]
    heapq.heapify(nums)
    for i in range(k):
        for j in range(len(newArray)):
            if newArray[j] == nums[0]:
                newArray[j] = nums[0] * multiplier
                heapq.heapreplace(nums, newArray[j])
                break

    return newArray
