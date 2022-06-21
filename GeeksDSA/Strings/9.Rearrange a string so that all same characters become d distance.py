#9.Rearrange a string so that all same characters become d distance away

MAX = 256
 
# A structure to store a character 'c' and its frequency 'f' in input string
 
class charFreq(object):
    def __init__(self, c, f):
        self.c = c
        self.f = f
# A utility function to swap two charFreq items.
 
def swap(x, y):
    return y, x
 
# A utility function
 
def toList(string):
    t = []
    for x in string:
        t.append(x)
 
    return t
 
# A utility function
 
def toString(l):
    return ''.join(l)
 
# A utility function to maxheapify the node freq[i] of a heap
# stored in freq[]
 
def maxHeapify(freq, i, heap_size):
    l = i*2 + 1
    r = i*2 + 2
    largest = i
    if l < heap_size and freq[l].f > freq[i].f:
        largest = l
    if r < heap_size and freq[r].f > freq[largest].f:
        largest = r
    if largest != i:
        freq[i], freq[largest] = swap(freq[i], freq[largest])
        maxHeapify(freq, largest, heap_size)
 # A utility function to convert the array freq[] to a max heap
 
def buildHeap(freq, n):
    i = (n - 1)//2
    while i >= 0:
        maxHeapify(freq, i, n)
        i -= 1
# A utility function to remove the max item or root from max heap
 
def extractMax(freq, heap_size):
    root = freq[0]
    if heap_size > 1:
        freq[0] = freq[heap_size-1]
        maxHeapify(freq, 0, heap_size-1)
 
    return root
 
# The main function that rearranges input string 'str' such that
# two same characters become d distance away
 
def rearrange(string, d):
    # Find length of input string
    n = len(string)
 
    # Create an array to store all characters and their
    # frequencies in str[]
    freq = []
    for x in range(MAX):
        freq.append(charFreq(0, 0))
 
    m = 0
 
    # Traverse the input string and store frequencies of all
    # characters in freq[] array.
    for i in range(n):
        x = ord(string[i])
 
        # If this character has occurred first time, increment m
        if freq[x].c == 0:
            freq[x].c = chr(x)
            m += 1
 
        freq[x].f += 1
        string[i] = '\0'
 
    # Build a max heap of all characters
    buildHeap(freq, MAX)
 
    # Now one by one extract all distinct characters from max heap
    # and put them back in str[] with the d distance constraint
    for i in range(m):
        x = extractMax(freq, MAX-i)
 
        # Find the first available position in str[]
        p = i
        while string[p] != '\0':
            p += 1
 
        # Fill x.c at p, p+d, p+2d, .. p+(f-1)d
        for k in range(x.f):
 
            # If the index goes beyond size, then string cannot
            # be rearranged.
            if p + d*k >= n:
                print ("Cannot be rearranged")
                return
 
            string[p + d*k] = x.c
 
    return toString(string)
 
# Driver program
string = "aabbcc"
print (rearrange(toList(string), 3))