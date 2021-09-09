"""
Lab 1:     Problem 1/2(Unique)
Author:    Wesley Torrez
Professor: Healey
Class:     CS 320
Date:      June 13th, 2019

This program is written in Python. It
identifies the unique tokens in a given
file. It then extracts the unique tokens
and writes them to an output file, separated
by the white-space character.
"""

user_input = input("Enter file name: ")
myFile = open(user_input)
token_list = []

for line in myFile:
    line = line.split()
    for word in line:
        found = False
        token = word
        for unique_word in token_list:
            if unique_word == token:
                found = True
                break
        if not found:
            token_list.append(token)

my_list = ' '.join(token_list)
output = open('output.txt', 'a')
output.write(my_list)
print(my_list)
myFile.close()
