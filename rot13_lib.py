#numerical encryption          
def crypt_word(char, crypt_choice, offset, case):
    originalIndex = case.index(char)
    if crypt_choice == "encode":
        if (originalIndex + offset) > 25:
            newIndex = (originalIndex + offset - 26)
            output = case[newIndex]
            return output
        elif (originalIndex + offset) <= 25:
            newIndex = (originalIndex + offset)
            output = case[newIndex]
            return output
    if crypt_choice == "decode":
        if (originalIndex - offset) < 0:
            newIndex = (originalIndex - offset + 26)
            output = case[newIndex]
            return output
        elif (originalIndex - offset) >= 0:
            newIndex = (originalIndex - offset)
            output = case[newIndex]
            return output
