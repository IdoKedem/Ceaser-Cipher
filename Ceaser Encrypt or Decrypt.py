
def encrypt():
    clear = input("Enter text to encrypt: \n")
    key = int(input("Enter key for ceaser code: \n"))

    cipher = (applyKey(clear, key))

    for i in range(len(cipher)):
        print(cipher[i], end="")
    print()

def decrypt():
    cipher = input("Enter text for decryption: \n")

    for i in range(-1, -26, -1):
        clear = applyKey(cipher, i)

        print("Using key", -i)
        for j in range(len(clear)):
            print(clear[j], end="")
        print("\n")


def applyKey(text, key): # Adds key to each char in string
    lst = []

    for i in range(len(text)):

        if(inAlphabet(text[i])): # if english letters
            
            lst.append(cycle(text[i], key)) # add key
        else:
            lst.append(text[i])

    return lst

def inAlphabet(char): # is char in the English alphabet
    if((char >= 'a' and char <= 'z') or (char >='A' and char <= 'Z')):
        return True
    return False

def cycle(char, key): # cycles back to alphabet (z + 2 --> b). Char is in the english alphabet

    new = chr(ord(char) + key)

    if (char >='a' and char <='z'):
        capital = False
    else:
        capital = True

    if(not inAlphabet(new)):

        if(capital):
            if(new < 'A'):
                new = chr(ord(new) + 26)
            else:
                new = chr(ord(new) - 26)
        else:
            if(new < 'a'):
                new = chr(ord(new) + 26)
            else:
                new = chr(ord(new) - 26)
    else:
        if((not capital) and new >='A' and new <='Z'):
            new = chr(ord(new) + 26)
    return new



selection = int(input("Enter: \n1 for encryption \n2 for decryption\n"))
if(selection == 1):
    encrypt()
else:
    decrypt()