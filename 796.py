def rotateString(s, goal):  #beat 100% in time complexity, however it still slow time: O(n^2)
    if len(s) != len(goal):
        return False

    for i in range(len(s)):
        newString = s[i:] + s[:i]
        if newString == goal:
            return True

    return False

#Optimal solution:
def rotateString(self, s, goal):
    return len(s) == len(goal) and goal in (s + s)

#Time complexity: O(n)
#Concatenating s + s takes O(n), where n is the length of s.
#Checking if goal is a substring takes O(n).
#Thus, the overall time complexity is O(n).

