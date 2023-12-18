text = input("Enter some text: ")
letter_count = {}

for char in text:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

print("-- Character Frequency Table --\nchar\tpercentage (character count / string length)")       
for letter, count in letter_count.items():
    print(f"{letter}\t{count*100/len(text):.2f} %")