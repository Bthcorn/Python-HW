abbr = {'be': 'b', 'because': 'cuz', 'see': 'c', 'the': 'da', 'okay': 'ok', 'are': 'r', 'you': 'u', 'without': 'w/o', 'why': 'y',
        'see you': 'cu', 'ate': '8', 'great': 'gr8', 'mate': 'm8', 'wait': 'w8', 'later': 'l8r', 'tomorrow': '2mro', 'for': '4',
        'before': 'b4', 'once': '1ce', 'and': '&', 'Your': 'ur', 'You\'re': 'ur', 'as far as I know': 'afaik', 'As soon as possible': 'ASAP',
        'At the moment': 'atm', 'Be right back': 'brb', 'By the way': 'btw', 'For your information': 'FYI', 'In my humble opinion': 'imho',
        'In my opinion': 'imo', 'Laughing out loud': 'lol', 'Oh my god': 'omg', 'Rolling on the floor laughing': 'rofl',
        'Talk to you later': 'ttyl'
        }


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
