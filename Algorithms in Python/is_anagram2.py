s1 = "fairy tales"
s2 = "rail safety"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

def is_anagram(s1, s2):
    ht = dict()  #get an empty dictionary
    #put all the characters of s1 in the dictionary
    for i in s1:
        if i in ht: #if the character is present in the dictionary increase the value by 1
            ht[i] += 1
        else:   #if the character is not present then set the value is 1
            ht[i] = 1

    #find all the characters of s2 in the dictionary
    for i in s1:
        if i in ht: #if the character is present in the dictionary decrease the value by 1
            ht[i] -= 1
        else:   #if the character is not present then set the value is 1
            ht[i] = 1

    for i in ht:
        if ht[i] != 0: #if the length of the dictionary is not 0 then it is not anagram
            return False
    #the length of the dictionary is 0 so         
    return True

print(is_anagram(s1, s2))

