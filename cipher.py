#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:38:57 2018

@author: kengo
"""
import sys
from colored import fg, bg, attr
#import DecryptingTranspositionCipher,BruteforceCeaserCipher,CeaserCipher,detectenglish,ReverseCeaserCipher,typewriter,TranspositionCipher
def main():
    header=""" 
              _________     ___    _______     __     __    _______    _______
             /         \   |   |  |   __  \   |  |   |  |  |       |  |   __  \
            |    ______/   |   |  |  |__|  |  |  |   |  |  |   ____|  |  |__|  | 
            |   |          |   |  |    ___/   |  |___|  |  |   |___   |    ___/    
            |   |          |   |  |   |       |         |  |       |  |  |  \
            |   |          |   |  |   |       |   ___   |  |    ___|  |  |\  \
            |   |______    |   |  |   |       |  |   |  |  |   |___   |  | \  \
            |          \   |   |  |   |       |  |   |  |  |       |  |  |  |  |
            \__________/   |___|  |___|       |__|   |__|  |_______|  |__|  |__|  
            
                                                              WELCOME TO CIPHER
                                                              WORLD"""
            
    print("%s%s"% (fg(11),header))
    options= """


            select an option below
            1. CEASER CIPHER
            2. TRANSPOSITION CIPHER
            3. DECRYPT TRANSPOSITION CIPHER
            4. BRUTEFORCE CEASER CIPHER
            5. REVERSE CIPHER
            """

    print ("%s%s"%(fg(11),options))

    select = int(input(':>'))

    while select>5:
        print('incorrect option')
        select = int(input(':>'))
        
    
    if select==1:
        import CeaserCipher
    if select==2:
        import TranspositionCipher
    elif select==3:
        import DecryptingTranspositionCipher
    elif select==4:
        import BruteforceCeaserCipher
    elif select==5:
        import ReverseCeaserCipher
        
main()
back=input("press 'b' for back:>")
while back == 'b':
    main()
    back=input("press 'b' for back:>")
else:
    sys.exit('good bye')
    