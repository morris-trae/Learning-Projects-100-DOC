# file names should be lowercase with an underscore joining the words. no spaces allowed. 

# If it's a global variable, we usually capitalize the whole thing.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '] # adding a space 


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction.lower().strip() == "decode":
            shift_amount *= -1
    for char in start_text.lower(): # if the whole alphabet is lowercase, we can only use strings with lowercase. Could be cool to have an uppercase alphabet option too.
        if char in ALPHABET:
            position = ALPHABET.index(char)
            # Reverse the shift direction if the character is less than zero or greater than 26.
            if 0 > position + shift_amount > len(ALPHABET) - 1:
                new_position = position - (len(ALPHABET) - shift_amount)
            else:
                new_position = position + shift_amount
            end_text += ALPHABET[new_position]
        else:
         end_text += char
    return end_text # better to have functions return values than have them print from within the function

should_continue = True
while should_continue: # Very smart way to do this!
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n")) # TODO error checking. What happens if I put in 'p100' accidentally?
    shift = shift % 26 # Amazing! 
    end_text = caesar(start_text=text, shift_amount=shift, cipher_direction=direction) # great job with the placeholders. Very readable
    print(f'The {direction}d text is "{end_text}"') # I Love this "d" haha


    restart = input("\nWould you like to use the cipher again? [yes/no]  ") # updating to a more common format just so you can see.
    if restart.lower().strip() == "no": # without the .strip() it would throw an error with  'no ' and without .lower() would not match if they entered 'No'
        should_continue = False
        print("Goodbye")