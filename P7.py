"""
n = 122fhgf2343ghj55
"""

s = "122fhgf2343gh!*- j55"
charvar=""
number = 0
for char in s:
    if 65<=ord(char)<=90 or  97<=ord(char)<=122:
        charvar+=char
    elif 48<=ord(char)<=57:
        number = (number*10)+int(char)
    else:
        pass
print("Char var = ",charvar)
print("Number var = ",number)

