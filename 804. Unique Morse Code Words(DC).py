# Question:

# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = dict(zip(
            [chr(97+i) for i in range(26)], 
            [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
        
		# convert string into Morse code with the help of previous hashmap
        def str2mos(string):
            res = ''
            for c in string:
                res += d[c]
            return res
        
        # Create Morse code list from word list, and convert the list into a set to reduce duplicated items.
        set_mos_words = set([str2mos(s) for s in words])
		# The length of the set gives the number of different transformation of input word list
        return len(set_mos_words)
        