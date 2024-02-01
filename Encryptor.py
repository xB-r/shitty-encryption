import random

characters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
              "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# 63 characters supported (including SPACE)
# 0 doesn't get rebound

calc_key_int = []
final_char_pos = []
cipher = []

print("Encryptor")

def keygen():
    global key, final_key
    key_var = str(input("Generate an encryption key? (Y/N): "))
    if key_var == "Y" or key_var == "y":
        key = random.randint(10000000, 99999999)
        final_key = str(key)
        print("This is the generated encryption key:", key)
    elif key_var == "N" or key_var == "n":
        try:
            key = int(input("Enter your encryption key (8 digits only): "))  # number check
        except ValueError:
            print("Please enter an 8 digit number only")
            keygen()

        key1 = str(key)

        if len(key1) > 8 or len(key1) < 8:  # length check
            print("Invalid key length, try again")
            keygen()
        else:
            final_key = str(key1)
    else:
        print("Invalid input, try again")
        keygen()

    calc_key = (list(final_key))

    for keys in calc_key:
        calc_key_int.append(int(keys))

    encrypt()


def encrypt():
    counter = 0
    char_count = 0

    plain_text = str(input("Enter the text you wish to encrypt: "))
    plain_list = list(plain_text)

    for words in plain_list:
        if words in characters:
            counter += 1
        else:
            print("Invalid character (Only Numbers and Alphabets supported)")
            keygen()

    for letters in plain_list:  # scrambling
        letter_place = calc_key_int[char_count]
        letter_pos = characters.index(letters)
        final_pos = letter_pos + letter_place

        if final_pos > 63:  # rebound
            final_pos = final_pos - (letter_place * 2)
            final_char_pos.append(final_pos)
        else:
            final_char_pos.append(final_pos)

        char_count += 1

        if char_count == 8:
            char_count = 0

    for final_positions in final_char_pos:
        cipher_word = characters[final_positions]
        cipher.append(cipher_word)

    cipher_text = str(["".join(cipher)])
    print("This is the encrypted text:", cipher_text)
    input("Press ENTER to exit ")
    exit()


keygen()
