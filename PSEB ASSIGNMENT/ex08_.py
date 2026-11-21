char =input ("Enter a character: ")
if char.lower() in "aeiou":
    print("Vowel")
elif char .isdigit():
 print("digit")
elif char .isalpha():
   print("consonant")
else:
   print("Special character")