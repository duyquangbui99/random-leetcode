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
