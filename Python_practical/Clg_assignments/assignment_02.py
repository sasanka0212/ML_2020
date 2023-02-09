# Assignment 02

"""
Write a program to take a string as input -
1. count ans print frequencies of each character in the string.
2. print the lowest frequency with corresponding character.
3. count and print no of words in the string.
4. reverse all the words and print.
5. remove duplicate characters and print string.
6. change lowercase characters to uppercase and vice versa.
"""

string = input("enter a string : ")

print("total no of words in the given string:", len(string.split(" ")))

frequency = {}
for s in string:
    if s in frequency:
        frequency[s] = frequency[s] + 1
    else:
        frequency[s] = 1
print("frequency of characters :\n", frequency)

low_freq = min(frequency.values())
char = [i for i in frequency.keys() if frequency[i] == low_freq]

print("lowest frequency :", low_freq)
print("characters with lowest frequency :\n", char)

print("reverse of the given string :", string[::-1])

p = ""
for s in string:
    if s not in p:
        p = p + s
print("after removing duplicate characters :", p)

s1 = ""
for s in string:
    if s.isupper():
        s1 += s.lower()
    else:
        s1 += s.upper()
print("case vice versa :", s1)