# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

address = "255.100.50.0"
for i in address:
    if i == ".":
        x = address.replace(".","[.]")
        
x