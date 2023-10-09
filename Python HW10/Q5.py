def isAnagram(text1, text2):
    if len(text1) != len(text2):
        return False
    
    for i in text1:
        anagram = False
        if i in text2:
            anagram = True
        if anagram == False:
            return anagram
    return anagram

print(isAnagram("silent", "listen"))
print(isAnagram("recital", "article"))
print(isAnagram("note", "notice"))
print(isAnagram("letter", "better"))
print(isAnagram("flower", "flour"))