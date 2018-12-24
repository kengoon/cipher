#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:48:28 2018

@author: kengo
"""


def main():
    myMessage = input('enter message to encrypt:>')
    myKey =int(input('enter key:>'))
    ciphertext = encryptMessage(myKey, myMessage)
    # Print the encrypted string in ciphertext to the screen, with
# a | (called "pipe" character) after it in case there are spaces at
# the end of the encrypted message.
    print('\n')
    print('here is your fucking encrypted text:')
    print(ciphertext)
# Copy the encrypted string in ciphertext to the clipboard.
    
def encryptMessage(key, message):
    print('hey i am not pleading be with you but be patient')
    print('encryptin.......')
# Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key
    
# Loop through each column in ciphertext.
    for col in range(key):
        pointer = col
    # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
# Place the character at pointer in message at the end of the
# current column in the ciphertext list.
            ciphertext[col] += message[pointer]
# move pointer over
            pointer += key
# Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)
# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.

main()
