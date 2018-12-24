#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 18:23:29 2018

@author: kengo
"""
import detectenglish

# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)
message = input('enter the encrypted message to bruteforce attack:>')
message=message.upper()
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
def main():
    for key in range(len(LETTERS)):
        
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num=LETTERS.find(symbol)
                num=num-key
                if num<0:
                    num=num+len(LETTERS)
                translated+=LETTERS[num]
            else:
                translated=translated+symbol
        print('Key #%s: %s' % (key, translated))
                    
        if detectenglish.isEnglish(translated):
            print("\n")
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, translated))
            print("\n")
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
                
            if response.strip().upper().startswith('D'):
                return translated
    return None
main()
    
        
            
            
            
    #print('Key #%s: %s' % (key, translated))