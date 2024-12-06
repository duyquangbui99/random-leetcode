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


