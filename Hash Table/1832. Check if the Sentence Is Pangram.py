# Question:

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true

sentence = "thequickbrownfoxjumpsoverthelazydog"
def pangram(sentence):
    a = []
    for i in range(ord('a'),ord('z')+1):
        a.append(chr(i))
    atoz = "".join(a)
    for j in atoz:
        if j not in sentence:
            return False
    return True
pangram(sentence)