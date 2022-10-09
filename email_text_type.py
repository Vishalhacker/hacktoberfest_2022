# Email Address Character Count - Python Program
# Contributed by Ujjwal Acharya


mail = input("Enter Your Email-Id: ")
mail=mail.lower()
vowels = consonants = num = whitespaces = spcharacters = 0
for i in mail:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowels += 1  # vowel = vowel + 1
    elif i in ['1','2','3','4','5','6','7','8','9','0']:
        num += 1
    elif i == " ":
        whitespaces += 1
    elif i == "@":
        spcharacters += 1
    else:
        consonants += 1
print("No. of vowels = ", vowels)
print("No. of Consonants = ", consonants)
print("No. of numbers = ", num)
print("No. of White Spaces = ", whitespaces)
print("No. of Special Character = ", spcharacters)
