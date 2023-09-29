import string
import argparse

ALPHABET = list(string.ascii_letters) # all letters lowercase and caps
# uncomment below and comment above if you just want lowercase letters
# ALPHABET = list(string.ascii_lowercase)

def _shift_amount_per_character(character, shift_amount):
    '''
    this adjusts for shifts past the beginning/end of the list
    '''
    alphabet_length = len(ALPHABET) - 1
    if shift_amount >= 0:
        shift_amount = shift_amount % alphabet_length
    else:
        shift_amount = (abs(shift_amount) % alphabet_length) * -1
    position_after_shift = _position_in_alphabet(character) + shift_amount
    if position_after_shift > alphabet_length:
        return alphabet_length - shift_amount
    elif position_after_shift < 0:
        return alphabet_length + shift_amount
    else:
        return shift_amount

def _position_in_alphabet(char) -> int:
    '''
    what position is the character in the alphabet
    '''
    return ALPHABET.index(char)

def _get_char_by_position(position) -> int:
    '''
    get the character at the provided position
    '''
    return ALPHABET[position]

def _is_char_in_alphabet(char) -> bool:
    '''
    Is the character in the Alphabet?
    '''
    return char in ALPHABET
           
def encrypt_message(message, shift_amount):
    '''
    used to encrypt or decrypt the message
    '''
    encrypted_message = ''
    for char in message:
        if _is_char_in_alphabet(char):
            new_shift_amount = _shift_amount_per_character(char, shift_amount)
            position = _position_in_alphabet(char)
            encrypted_message += _get_char_by_position(position + new_shift_amount)
        elif char == ' ':
            encrypted_message += ' '
    return encrypted_message 

def configure_parser():
    '''
    simply configures the argument parser so that this can be used from the command line
    '''
    parser = argparse.ArgumentParser(description='Process arguments for Caesar Cipher',)
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-e', '--encrypt', action='store_true', help="Encrypt the message")
    group.add_argument('-d', '--decrypt', action='store_true', help="Decrypt the message")
    parser.add_argument('-m', '--message', required=True, help="The message to encrypt or decrypt")
    parser.add_argument('-o', '--offset', type=int, required=True, help="The offset for encryption/decryption")
    
    return parser.parse_args()

def main():  
    '''
    This ensures that the code inside main() only runs when the script is executed directly as the main program, 
    not when it's imported as a module into another script. 
    This is good for scalability, but not really necessary if you aren't using it as a module.
    
    usage: caesar_cipher.py [-h] (-e | -d) -m MESSAGE -o OFFSET
    '''  
    
    args = configure_parser()

    if args.encrypt:
        encrypted_message = encrypt_message(args.message, args.offset)
        print(f'Your encrypted message: "{encrypted_message}"')

    elif args.decrypt:
        # decryption is just encryption in reverse :D
        decrypted_message = encrypt_message(args.message, -1 * args.offset)
        print(f'Your decrypted message: "{decrypted_message}')


if __name__ == "__main__":    
    main()