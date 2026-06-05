### Jose Ortiz Eastman and Justin Barton
# Period 1

'''
 If you are in fact reading this, theres a simple change.
 We are trying to create a machine that is too complicated for-
Even us to understand ( don't worry in already are suffeing doing the bloody register and login page :) because I wanted to do it with the most affective security for what we have) . several moving parts could take far longer
Than a week, possibly even a month, so I had a change.
 Instead of making moving values, make it a fixed value.
 reflector will stay the same with plugboard
 Rotors will have to move though

The key to unscrambling text is to subtract instead of add, but do it on the already scrambled word


Alphabet = ABCDEFGHIJKLMNOPQRSTUVWXYZ
All the rotors have 26 letters in a cetain order
RotorI = E K M F L G D Q V Z N T O W Y H X U S P A I B R C J

RotorII = A J D K S I R U X B L H W T M C Q G Z N P Y F V O E

RotorIII = B D F H J L C P R T X V Z N Y E I W G A K M U S Q O

for the plugboard
'''

'''
#the plugs
dictionary = {
    "A": "B",
    "B": "A",
    "D": "E",
    "F": "G",
    "H": "I",
    "J": "K",
    "L": "M",
    "N": "O",
    "P": "Q",
    "R": "S",
    "T": "U",
    "V": "W",
    "X": "Y"
}

# The plug board works
def plugboard(letter, swap):
    return swap.get(letter, letter)



print(plugboard("Z", dictionary))
'''


def Enigma_machine():
    while True:
        option = None

        # Gives you the option to want to encrypt or decrypt
        try:
            question = input("Do you want to encrypt/decrypt?: ")
            if question == "":
                break
            elif question != "encrypt" or "decrypt":
                raise ValueError

        except ValueError:
            print("You got to put only encrypt or decrypt into it")


        # This is the messsage that will be encrypted
        message = input(f'Enter what you want to encrypt (enter nothing as the message and press enter to exit the code): ')
        if message == "":
            break

        # Enigma machine only has upper case letters
        uppercase = message.upper()

        # The amount the rotor is shifted by, aka, its offset
        rotor = 3

        # This right here is where the encrypted message will go
        encrypted_message = ""


        for letter in uppercase:
            if letter.isalpha():
                # New_letter is just letter but as a unicode number
                new_letter = ord(letter) - 65

                # This sets your option to encrypt or decrypt into motion
                if question == "encrypt":
                    option = (new_letter + rotor) % 26
                elif question == "decrypt":
                    option = (new_letter - rotor) % 26



                # New_letter gets shifted by the rotor's offset
                shifted_number = option

                #Encrypted_letter is now the scrambled up letter
                encrypted_letter = chr(shifted_number + 65)

                # Encrypted_message is the encrypted letters placed in order
                encrypted_message += encrypted_letter

                # This keeps the rotor moving so it's not a simple cipher
                rotor += 1
            else:

                # If it is something like a "" . , [] : ; -
                # It will pass through without being encrypted
                encrypted_message += letter



        print(f'The original message: {uppercase}')

        print(f'The encrypted message: {encrypted_message}')


Enigma_machine()
