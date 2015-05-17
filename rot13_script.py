#libraries
import sys
from rot13_lib import crypt_word

#two-way table initialisation

alpha_lc = [chr(x) for x in range(97, 123)]
alpha_uc = [chr(x) for x in range(65, 91)]

#input&output

def input_output(crypt, offset):
    crypt_string = input("Input string to be %sd: " % (crypt))
    new_crypt= ""
    for i in crypt_string:
        if i.isupper():
            new_crypt += crypt_word(i, crypt, offset, alpha_uc)
        elif i.islower():
            new_crypt += crypt_word(i, crypt, offset, alpha_lc)
        else:
            new_crypt += i
    print("Your %sd string is %s." % (crypt, new_crypt))
    retry_crypt()
                
#inputs and error handling

def retry_crypt():
    retry = input("Would you like to run this script again? [Y/N] ").lower()
    if retry == "y" or retry == "yes":
        crypt_choice()
    elif retry == "n" or retry == "no":
        sys.exit()
    else:
        print("Please select either 'yes' or 'no'.")
        retry_crypt()   
    
def offset_choice(crypt):
    offset = input("By how much (a positive integer) would you like to offset your string? ")
    while True:
        if ((offset.isdigit() == False) or (int(offset) < 0)) and (offset !=''):
            print("Please input a positive integer.")
            offset_choice(crypt)
            break
        elif offset == '':
            offset = 13
            print("A default value of 13 has been selected for your offset.")
            input_output(crypt, offset)
            break
        else:
            offset = (int(offset) % 26)
            input_output(crypt, offset)
            break

def crypt_choice():
    crypt = (input("Would you like to encode or decode a string? ")).lower()
    while True:
        if crypt not in ["encode", "decode"]:
            print("'Encode' and 'decode' are the only valid entries.")
            crypt_choice()
            break
        else:
            offset_choice(crypt)
            break
      
if __name__ == "__main__":
    crypt_choice()
