# # Question:

# # You are given an array of strings products and a string searchWord.

# # Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# # Return a list of lists of the suggested products after each character of searchWord is typed.

 
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
products.sort()
n = len(products)
indices = [i for i in range(n)]
res = []
for idx, c in enumerate(searchWord):
    indices = [i for i in indices if len(products[i])> idx and products[i][idx] == c]
    res.append(products[i] for i in indices[:3])
res