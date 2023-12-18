# Question 1 
abbr = {'be': 'b', 'because': 'cuz', 'see': 'c', 'the': 'da', 'okay': 'ok', 'are': 'r', 'you': 'u', 'without': 'w/o', 'why': 'y',
        'see you': 'cu', 'ate': '8', 'great': 'gr8', 'mate': 'm8', 'wait': 'w8', 'later': 'l8r', 'tomorrow': '2mro', 'for': '4',
        'before': 'b4', 'once': '1ce', 'and': '&', 'Your': 'ur', 'You\'re': 'ur', 'as far as I know': 'afaik', 'As soon as possible': 'ASAP',
        'At the moment': 'atm', 'Be right back': 'brb', 'By the way': 'btw', 'For your information': 'FYI', 'In my humble opinion': 'imho',
        'In my opinion': 'imo', 'Laughing out loud': 'lol', 'Oh my god': 'omg', 'Rolling on the floor laughing': 'rofl',
        'Talk to you later': 'ttyl'
        }

def textese(s):
    words = s
    for key, value in abbr.items():
        if key in words:
            words = words.replace(key, value)
    return words

print(textese("you have to wait until tomorrow. As soon as possible, I will come to see you, okay?"))

def untextese(s):
    words = s.split(" ")
    newtext = []
    for word in words:
        if word in abbr.values():
            for key, value in abbr.items():
                if value == word:       
                    newtext.append(key)
        else:
            newtext.append(word)
    return " ".join(newtext)

print(untextese("u have to w8 until 2mro ASAP I will come to cu ok"))

# ==========================================

# Question 2
dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p':'1', 'q':'2', 'r':'3'}

def composite(dict1, dict2):
    new_dict = {}
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if value1 == key2:
                new_dict[key1] = value2
    return new_dict

print(composite(dict1, dict2))
# ==========================================

# Question 3
def product(*args):
    new_set = []
    for i in args[0]:
        new_set.append((i,))
        
    for k in args[1:]:
        another_set = [] 
        for j in new_set:
            for m in k:
                another_set.append(j + (m,))
        new_set = another_set
    return new_set

s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

set(product(s1, s2, s3))
set(product(s1, s2))
set(product(s1))

# ==========================================
