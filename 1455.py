#1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence (easy)
def isPrefixOfWord(sentence, searchWord):
    words = sentence.split(' ')
    searchWordLenght = len(searchWord)
    for i, word in enumerate(words):
        if searchWord == word[:searchWordLenght]:
            return i + 1

    return -1

# Time complexity: O(n*m) n is the length of the string, m is the prefix lenght
# Space complexity : O(n) where is number of words in the string

#Alternative method:
def isPrefixOfWord(sentence, searchWord):
    words = sentence.split(' ')
    for i, word in enumerate(words):
        if word.startswith(searchWord):
            return i + 1
    return -1
# Avoid unnecessary slicing: startswith() checks the prefix directly, making it slightly more efficient in practice.
