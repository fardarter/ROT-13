#libraries
import argparse
from rot13_lib import crypt_word

#two-way table initialisation
alpha_lc = [chr(x) for x in range(97, 123)]
alpha_uc = [chr(x) for x in range(65, 91)]

#positive integer test
def pos_int(x):
    if (x.isdigit() == True) and (x < 0):
            msg = "Argument must be a positive integer or zero (no effect)."
            raise argparse.ArgumentTypeError(msg)
    elif (x.isdigit() == False) and (x.isalnum() == False):
            msg = "Argument may only include positive integers or zero."
            raise argparse.ArgumentTypeError(msg)
    elif (x.isdigit() == True) and (x >= 0):
        return int(x)
 
#casing fork
def crypt(string, crypt_choice, offset):
    new_crypt = ""
    for i in string:
        if i.isupper():
            new_crypt += crypt_word(i, crypt_choice, offset, alpha_uc)
        elif i.islower():
            new_crypt += crypt_word(i, crypt_choice, offset, alpha_lc)
        else:
            new_crypt += i
    return new_crypt
        
#command-line interaction
def main():
    parser = argparse.ArgumentParser(description="This program is a ROT-X (rotation by X) encoder and decoder. \
                                                  The X in ROT-X is an offset selected by argument. \
                                                  Please see Wikipedia entry 'ROT-13' for the original method. \
                                                  Arguments are accepted in the following order: \
                                                  ['string'] [['decode']/['encode']] [-offset (value)]. If an offset is not specified, \
                                                  a default of 13 will be used. See -h/--help for arugment restrictions.")
    parser.add_argument("string", help="A string (only alphabetical characters will be changed) to be encoded or decoded. \
                                        (Ubuntu treats spaces as breaks; therefore, to encode or decode a string with spaces (multiword), \
                                        the string must be placed between quotes.)")
    parser.add_argument("crypt_choice", choices=["encode", "decode"], help="Select either 'encode' or 'decode'.")
    parser.add_argument("-offset", type=pos_int, nargs='?',  default=13, help="A positive integer or zero (no effect) only.\
                                                                               If not specified, a default of 13 will be used.")
    args = parser.parse_args()
    result = crypt(args.string, args.crypt_choice, (args.offset % 26))
    print("Your output is: "+str(result))

#initialisation
if __name__ == "__main__":
    main()
