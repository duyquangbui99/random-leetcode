#1957. Delete Characters to Make Fancy String
#Initial method
def makeFancyString(s):   # beat only 46.65% in time complexity
    newString = s[0]
    count = 1
    for c in s[1:]:
        if c == newString[-1] and count < 2:
            newString += c
            count += 1
        elif c != newString[-1]:
            newString += c
            count = 1
        else:
            continue

    return newString
#Time complexity O(n^2) since string concatenation take O(n)


#Alternative method: using array instead of string concatenation making time complexity from O(n^2) to O(n)
def makeFancyString(s):  # beat 86%, much better
    newString = [s[0]]
    count = 1
    for i in range(1, len(s)):
        c = s[i]
        if c == newString[-1] and count < 2:
            newString.append(c)
            count += 1
        elif c != newString[-1]:
            newString.append(c)
            count = 1
        else:
            continue

    return "".join(newString)


