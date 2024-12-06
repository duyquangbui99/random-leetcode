def checkIfExist(arr):
    hashTable = {}
    for num in arr:
        hashTable[num] = hashTable.get(num, 0) + 1
    if 0 in hashTable:
        if hashTable[0] >=2:
            return True
    for num in arr:
        if num == 0:
            continue
        if num*2 in hashTable:
            print(num)
            return True

    return False
# Time complexity: O(n) loop through n elements in the arr
# Space complexity: O(n) create hashmap with n elements of the arr

#Alternative better version:
def checkIfExist(arr):
    seen = set()
    for num in arr:
        if num*2 in seen or num == 0 and num in seen:
            return True
        seen.add(num)
    for num in arr:
        if num == 0:
            continue
        if num*2 in seen:
            return True
    return False
#Time complexity: O(n)
#Space complexity: O(n)

# The set-based function is more efficient because it handles the case of duplicate 0s 
# directly and checks for the existence of a double in the first loop. This eliminates 
# the need to use a hashmap to store all elements before performing the check.



