num = int(input("Enter a number: "))

one_to_10 = ["zero", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine"]
ten_to_19 = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen","eighteen", "nineteen"]
more_or_20 = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]

ten = ""
word = []
if num < 0:
    raise ValueError("Please input a number in range 1-999")
 
if 0 <= num < 10:
    ten += one_to_10[num]
    word.append(ten)
elif 10 <= num <= 19:
    ten += ten_to_19[num % 10]
    word.append(ten)
elif 19 < num < 100:
    ten += more_or_20[num % 100 // 10 - 2]
    ten += "-"
    ten += one_to_10[num % 10]
    word.append(ten)
elif num >= 100 and num <= 999:
    word.append(one_to_10[num // 100])
    word.append("hundred")
    if 0 < num % 100 < 10:
        ten += "and "
        ten += one_to_10[num % 10]
    elif 10 <= num % 100 < 20:
        ten += "and "
        ten += ten_to_19[num % 10]
    elif num % 100 >= 20:
        ten += "and "
        ten += more_or_20[num % 100 // 10 - 2]
        if num % 10 >= 1:
            ten += "-"
            ten += one_to_10[num % 10]
    word.append(ten)
else:
    word.append("I don't know")

print(" ".join(word))

# def number_to_words(n):
#     if n < 0 or n > 999:
#         raise ValueError("Please input a number in the range 0-999")

#     ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
#     tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#     if n == 0:
#         return "zero"
#     elif 1 <= n <= 9:
#         return ones[n]
#     elif 11 <= n <= 19:
#         return teens[n - 10]
#     elif 21 <= n <= 99:
#         return tens[n // 10] + ("-" + ones[n % 10] if n % 10 != 0 else "")
#     else:
#         hundred_part = ones[n // 100] + " hundred"
#         if n % 100 == 0:
#             return hundred_part
#         else:
#             return hundred_part + " and " + number_to_words(n % 100)

# num = int(input("Enter a number: "))
# print(number_to_words(num))
