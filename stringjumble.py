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
print('You entered ''. Now jumble it:')
letter = list(text)
num = len(text)
reverse = (letter[num::-1])
word = (letter[:num:1])
first = ""

third = ""
fourth = ""

sixth = ""
seventh = ""
a = 0
b = -1
for i in reverse:
    first += i
print(first)
for i in reverse:
    a+=1
    if i == " ":
        well = letter[num-(a):num-(b):]
        b+=len(well)
        for i in well:
            third += i
fine = letter[0:num-(b):]
for i in fine:
    fourth += i
print(third + " " + fourth)
c = -1
d = 0
for i in word:
    c+=1
    if i == " ":
        okay = letter[c:d:-1]
        d+=len(okay)
        for i in okay:
            sixth += i
sure = letter[num:d:-1]
for i in sure:
    seventh += i
print(sixth + " " + seventh)
