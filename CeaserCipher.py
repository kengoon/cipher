# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
#import pyperclip
# the string to be encrypted/decrypted
from colored import fg, bg, attr
print("%smind you i dont encrypt numbers and special characters"%(fg(1)))
message = input("enter your message here:>")
# the encryption/decryption key
key = int(input('enter the key to be used eg:1-25:>'))
while key<0 or key>25:
    print('%sI THINK YOU WANNA ENCRYPT YOUR ASS'%(fg(11)))
    print('try again')
    key = int(input('enter the key to be used eg:1-25:>'))
# tells the program to encrypt or decrypt
mode = int(input("enter mode eg(press (1) for encrypt or (2)for decrypt):>")) # set to 'encrypt' or 'decrypt'
while mode<1 or mode>2:
    print('%sYOU MUST BE AN ASS JUNK WOULD YOU FUKINGLY TRY AGAIN%s'%(fg(1),attr(0)))
    mode = int(input("enter mode eg(press (1) for encrypt or (2)for decrypt):>"))
# every possible symbol that can be encrypted
if mode==1:
    mode="encrypt"
if mode==2:
    mode="decrypt"
    
    
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# stores the encrypted/decrypted form of the message
translated = ''
# capitalize the string in message
message = message.upper()
# run the encryption/decryption code on each symbol in the message string
for symbol in message:
	if symbol in LETTERS:
		
		# get the encrypted (or decrypted) number for this symbol
		num = LETTERS.find(symbol) # get the number of the symbol
		
		    
		if mode =="encrypt":
			num = num + key
		elif mode =="decrypt":
			num = num - key
	# handle the wrap-around if num is larger than the length of


	# LETTERS or less than 0
		if num >= len(LETTERS):
			num = num - len(LETTERS)
		elif num < 0:
			num = num + len(LETTERS)
	# add encrypted/decrypted number's symbol at the end of translated
		translated = translated + LETTERS[num]
	else:
	# just add the symbol without encrypting/decrypting
		translated = translated + symbol
# print the encrypted/decrypted string to the screen
print("%s%sing>>>>>>>>>>> "%(fg(82),mode))
print("%syour message has been %sed" %(fg(82),mode))
print(translated)
# copy the encrypted/decrypted string to the clipboard
#pyperclip.copy(translated)
