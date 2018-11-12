s1 = "fairy tales"
s2 = "road safety"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# Requires n log n time (since any comparison 
# based sorting algorithm requires at least 
# n log n time to sort).
print(sorted(s1) == sorted(s2))
