"""
stringjumble.py
Author: Meg
Credit: Noah

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
text = input('Please enter a string of text (the bigger the better): ')
print('You entered "' + text + '". Now jumble it:')
letter = list(text)
spaceb = " " + text
spacee = text + " "
num = len(text)
reverse = (letter[num::-1])
if letter[num-1] != " ":
    letter1 = list(spacee)
if letter[0] != " ":
    letter2 = list(spaceb)

first = ""

third = ""
fourth = ""

sixth = ""
seventh = ""
a = 0
b = 0
for i in reverse:
    first += i
print(first)

for i in reverse:
    a+=1
    if i == " ":
        well = letter1[num-(a):num-(b):]
        b+=len(well)
        for i in well:
            third += i
fine = letter1[0:num-(b):]
for i in fine:
    fourth += i
print(third + " " + fourth)

c = 0
d = 0
for i in letter:
    c+=1
    if i == " ":
        okay = letter2[c:d:-1]
        d+=len(okay)
        for i in okay:
            sixth += i
sure = letter2[num:d:-1]
for i in sure:
    seventh += i
print(sixth + " " + seventh)
