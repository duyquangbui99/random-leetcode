def rotateString(s, goal):  #beat 100% in time complexity
    if len(s) != len(goal):
        return False

    for i in range(len(s)):
        newString = s[i:] + s[:i]
        if newString == goal:
            return True

    return False
