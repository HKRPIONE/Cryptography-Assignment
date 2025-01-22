# Caesar Cipher

# Define list of alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def encryption(plain_text, shift_key):
    cipher_text = "" # define string
    for char in plain_text: # give each char in plain text
        if char in alphabet:    
            position = alphabet.index(char) # position of char in alphabet list
            new_position = (position + shift_key) % 52 
            #  Position of char in alphabet list added by shift key and % 52 to keep it in range of 0-51 (52 letters)
            cipher_text += alphabet[new_position] 
            # add new position of char to cipher text string
            # same as cipher_text = cipher_text + alphabet[new_position] 
        else:
            cipher_text += char # jf char is not in alphabet list, add it to cipher text string as it is
    print(f"The encrypted text is {cipher_text}")

def decryption(cipher_text, shift_key):
    plan_text = "" # define string
    for char in cipher_text: # give each char in cipher text
        if char in alphabet:
            position = alphabet.index(char) # position of char in alphabet list
            new_position = (position - shift_key) % 52
            #  Position of char in alphabet list subtracted by shift key and % 52 to keep it in range of 0-51 (52 letters)
            plan_text += alphabet[new_position]
            # add new position of char to plan text string
            # same as plan_text = plan_text + alphabet[new_position]
        else:
            plan_text += char # jf char is not in alphabet list, add it to plan text string as it is
    print(f"The decrypted text is {plan_text}")

wanna_end = False # if we want to end the program then set wants_end to True
while not wanna_end: # untill the end of the program will execute below commands 

    what_to_do = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt the text\n")
    text = input("Enter the text: \n") 
    shift = int(input("Enter the shift: \n")) # take shift_key from the user and convert it to integer

    if what_to_do == "encrypt": 
        encryption(plain_text=text, shift_key=shift) # provide 2 arguments 
    elif what_to_do == "decrypt":
        decryption(text, shift) # provide 2 arguments

    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") # asking to user if he/she wants to go again
    if play_again == "no":
        wanna_end = True # if user wants to end the program then user type no then wanna_end will be true and program will end
        print("Goodbye! Thanks for using Caesar Cipher")

