# importing the exit function from the sys package, and the textwrap function to wrap the text of my program greeting
# paragraph.
from sys import exit
import textwrap

# Declaring global variables that will be used to control flow between the different modules.
go_to_encode = False
go_to_decode = False
invalid_message = False
invalid_shift_value = False


# Function that will convert the string that is passed into it into an integer if possible, and if not,
# it just returns the original string.
def convert_if_integer(test_input):
    try:
        return int(test_input)
    except ValueError:
        return test_input


# This function is an encoder that encodes messages from A -> Z. What that means is that the bigger the shift,
# the farther a letter goes up the alphabet to later letters. It takes the desired shift amount, and the message the
# user wants to encode, as parameters, and it returns an encoded message.
def caesar_cipher_encoder(int_shift_value, message_to_encode):
    # Need to announce use of global variable so that I am not initializing a new one.
    global invalid_message
    encoded_message = ""
    # For loop to go through each letter of the user's inputted message, gradually shifting the values of the
    # characters to different ASCII codes for other characters in the alphabet. Encoding and recording the encoded
    # message.
    for char in message_to_encode:
        code_value = ord(char)
        if code_value == 32:
            pass
        elif 64 < code_value < 91:
            code_value += int_shift_value
            if code_value > 90:
                overflow_value = code_value - 90
                code_value = 64 + overflow_value
        elif 96 < code_value < 123:
            code_value += int_shift_value
            if code_value > 122:
                overflow_value = code_value - 122
                code_value = 96 + overflow_value
        else:
            invalid_message = True
            print(
                "\n\033[31mYour message contained invalid characters. It should only include the 26 main letters of "
                "the latin alphabet.\033[0m")
            return

        encoded_char = chr(code_value)
        encoded_message += encoded_char
    return encoded_message


# This function is a decoder that decodes message from Z -> A. What that means is that the bigger the shift,
# the farther a letter goes down the alphabet to earlier letters. It takes the desired shift amount, and the message
# the user wants to decode as parameters, and it returns a decoded message.
def caesar_cipher_decoder(int_shift_value, encoded_message):
    # Need to announce use of global variable so that I am not initializing a new one.
    global invalid_message
    decoded_message = ""
    # For loop to go through each letter of the user's inputted message, gradually shifting all the values of the
    # characters to different ASCII codes for other characters in the alphabet. Decoding and recording the decoded
    # message.
    for char in encoded_message:
        code_value = ord(char)
        if code_value == 32:
            pass
        elif 64 < code_value < 91:
            code_value -= int_shift_value
            if code_value < 65:
                overflow_value = 65 - code_value
                code_value = 91 - overflow_value
        elif 96 < code_value < 123:
            code_value -= int_shift_value
            if code_value < 97:
                overflow_value = 97 - code_value
                code_value = 123 - overflow_value
        else:
            invalid_message = True
            print(
                "\n\033[31mYour message contained invalid characters. It should only include the 26 main letters of "
                "the latin alphabet.\033[0m")
            return
        decoded_char = chr(code_value)
        decoded_message += decoded_char
    return decoded_message


# This function is the encoding half of the program, that the user enters whenever they choose the #'encode' mode.
# This function calls the cipher encoder function for an encoded message once the user works their way through the
# interface.
def encode_mode():
    # Need to announce use of global variables so that I am not initializing new ones.
    global go_to_decode
    global invalid_message
    global invalid_shift_value
    # Greeting to the encode mode of the program
    print("\nYou are in 'Encode' Mode")
    # while loop to keep user in encode mode until they want to exit.
    while True:
        # Three tests to check if things went awry on the previous run. If something did go awry, the invalid_message
        # or invalid_shift_value variable might have been switched to True
        if invalid_message == False and invalid_shift_value == False:
            print("\nHow many alphabet places would you like the Caesar cipher to shift your message to the right?")
            shift_value = input("Please input an integer value between 1 and 25: ")
        elif invalid_message == False and invalid_shift_value == True:
            invalid_shift_value = False
            shift_value = input("\nPlease input an integer value between 1 and 25: ")
        elif invalid_message:
            invalid_message == False
        # Converts inputted shift_value into an int if possible
        converted_shift_value = convert_if_integer(shift_value)
        # Condition to test if shift value entered is an int or not, because it needs to be an int for the present
        # feature of the program.
        if isinstance(converted_shift_value, int):
            # If shift_value was an int, then it is first checked to see if it's in the valid range (1-25),
            # and then if it is, ask the user to input their message that they would like to encode.
            if 0 < converted_shift_value < 26:
                message_to_encode = input(
                    "\n\nYou can now go ahead and input your message for encoding. Press 'Enter' after typing in your "
                    "message:\n\n")
                # Message input by user is sent to the caesar_cipher_encoder function to encode the message with the
                # requested caesar cipher shift amount, and the encoded message is returned this method call and then
                # printed.
                encoded_message = caesar_cipher_encoder(converted_shift_value, message_to_encode)
                if invalid_message:
                    continue
                else:
                    print("\n\n\nHere is your encoded message!:\n")
                    print("\033[32m" + encoded_message + "\033[0m")
            else:
                print("\n\033[31mThat shift value is not within valid range.\033[0m")
                invalid_shift_value = True
                continue
        # A final check on the shift_value variable since it can't be an integer, it must be a string. If it's a
        # string, it could be a variety of my global commands, like "exit", "home", "encode", and "decode",
        # and these should be tested for. If it is none of these, the user is told that their input is not valid.
        else:
            lowercase_shift_value = shift_value.lower()
            if lowercase_shift_value in ["exit", "quit"]:
                print("\nExiting program...")
                quit()
            elif lowercase_shift_value == "home":
                return
            elif lowercase_shift_value == "encode":
                continue
            elif lowercase_shift_value == "decode":
                go_to_decode = True
                return
            else:
                print(
                    "\n\033[31mInput must be a valid shift integer value, or one of the program-wide commands.\033[0m")
                continue

        # This while loop is for a segment at the end of the function that allows the program to loop while the user
        # answers the question of if they would like to encode an additional message. The user is also still able to
        # input program-wide commands that work.
        while True:
            go_again = input("\n\n\nWould you like to encode another message? ")
            lowercase_go_again = go_again.lower()
            if lowercase_go_again in ["true", "t", "yes", "y", "encode"]:
                break
            elif lowercase_go_again in ["false", "f", "no", "n", "home"]:
                return
            elif lowercase_go_again in ["exit", "quit"]:
                print("\nExiting program...")
                exit()
            elif lowercase_go_again == "decode":
                go_to_decode = True
                return
            else:
                print("\n\033[31mInvalid input, try again.\033[0m")


# This function is the decoding half of the program, that the user enters whenever they choose the #'decode' mode.
# This function calls the cipher decoder function for a decoded message once the user #works their way through the
# interface.
def decode_mode():
    # Need to announce use of global variables so that I am not initializing new ones.
    global go_to_encode
    global invalid_message
    global invalid_shift_value
    # Greeting to the decode mode of the program
    print("\nYou are in 'Decode' Mode")
    # while loop to keep user in encode mode until they want to exit.
    while True:
        # Three tests to check if things went awry on the previous run. If something did go awry, the invalid_message
        # or invalid_shift_value variable might have been switched to True
        if invalid_message == False and invalid_shift_value == False:
            print(
                "\nHow many alphabet places would you like the Caesar cipher to use to shift your message to the left?")
            shift_value = input("Please input an integer value between 1 and 25: ")
        elif invalid_message == False and invalid_shift_value == True:
            invalid_shift_value = False
            shift_value = input("\nPlease input an integer value between 1 and 25: ")
        elif invalid_message:
            invalid_message == False
        # Converts inputted shift_value into an int if possible
        converted_shift_value = convert_if_integer(shift_value)
        # Condition to test if shift value entered is an int or not, because it needs to be an int for the present
        # feature of the program.
        if isinstance(converted_shift_value, int):
            # If shift_value was an int, then it is first checked to see if it's in the valid range (1-25),
            # and then if it is, ask the user to input their message that they would like to encode.
            if 0 < converted_shift_value < 26:
                encoded_message = input(
                    "\n\nYou can now go ahead and input your message for decoding. Press 'Enter' after typing in your "
                    "message.:\n\n")
                # Message input by user is sent to the caesar_cipher_decoder function to decode the message with the
                # requested caesar cipher shift amount, and the decoded message is returned this method call and then
                # printed.
                decoded_message = caesar_cipher_decoder(converted_shift_value, encoded_message)
                if invalid_message:
                    continue
                else:
                    print("\n\n\nHere is your decoded message!:\n")
                    print("\033[32m" + decoded_message + "\033[0m")
            else:
                print("\n\033[31mThat shift value is not within the valid integer range.\033[0m")
                invalid_shift_value = True
                continue
                # A final check on the shift_value variable since it can't be an integer, it must be a string. If
                # it's a string, it could be a variety of my global commands, like "exit", "home", "encode",
                # and "decode", and these should be tested for. If it is none of these, the user is told that their
                # input is not valid.
        elif isinstance(shift_value, str):
            lowercase_shift_value = shift_value.lower()
            if lowercase_shift_value in ["exit", "quit"]:
                print("\nExiting program...")
                quit()
            elif lowercase_shift_value == "home":
                return
            elif lowercase_shift_value == "encode":
                go_to_encode = True
                return
            elif lowercase_shift_value == "decode":
                continue
            else:
                print(
                    "\n\033[31mInput must be a valid shift integer value, or one of the program-wide commands.\033[0m")
                continue
        # This while loop is for a segment at the end of the function that allows the program to loop while the user
        # answers the question of if they would like to encode an additional message. The user is also still able to
        # input program-wide commands that work.
        while True:
            go_again = input("\n\n\nWould you like to decode another message? ")
            lowercase_go_again = go_again.lower()
            if lowercase_go_again in ["true", "t", "yes", "y", "decode"]:
                break
            elif lowercase_go_again in ["false", "f", "no", "n", "home"]:
                return
            elif lowercase_go_again in ["exit", "quit"]:
                print("\nExiting program...")
                exit()
            elif lowercase_go_again == "encode":
                go_to_encode = True
                return
            else:
                print("\n\033[31mInvalid input, try again.\033[0m")


# This is the main method, where the outer framework of the program has been assembled. The main method is the home
# portion of the program, where the user can access both of the different, more specific functions.
def main():
    # Need to announce use of global variables so that I am not initializing new ones.
    global go_to_encode
    global go_to_decode
    global invalid_message
    global invalid_shift_value
    # Storing large paragraphs program greetings, to the use with the textwrap function, to more easily format the
    # large paragraphs explaining my program when launched.
    program_greeting_body = """A Caesar cipher is a simple and widely known encryption technique, where each letter 
    in the alphabet is shifted a fixed number of positions. Each letter in the message to be encoded or decoded are 
    replaced by another letter that is a specific amount of places away in the alphabet. If a letter has to shift 
    past A or Z during the encryption, it will wrap around to the other sided of the alphabet."""
    program_greeting_conclusion = """This program allows you to provide your own messages for encoding or decoding. 
    You get to choose the amount of alphabet spaces that your cipher will shift when encoding or decoding. You can 
    also use the commands 'home', 'encode', 'decode', or 'exit'/'quit' anywhere throughout the program. 'home' will 
    bring you back to the beginning of the program, 'encode' or 'decode' will allow you to switch modes, and 'exit' 
    or 'quit' will end the program entirely."""
    wrapped_greeting_body = textwrap.fill(program_greeting_body, 89)
    wrapped_greeting_conclusion = textwrap.fill(program_greeting_conclusion, 89)
    mode_selection = ""
    # Two tests for if these two global flag variables weren't switched to True, in which case, the user doesn't need
    # to be asked about what mode they would like to user.
    if go_to_encode:
        go_to_encode = False
        mode_selection = "encode"
    elif go_to_decode:
        go_to_decode = False
        mode_selection = "decode"
    # This conditional tests if the mode is blank, indicating that neither of those two previous tests were triggered.
    if mode_selection == "":
        valid_input = False
        print("\n                        \033[1m\033[4mWelcome to Offline Caesar Cipher Tool!\033[0m\n")
        print("------------------------------------------------------------------------------------------\n")
        print("This tool allows you to encode or decode your own secret messages, using a Caesar cipher.\n")
        print(wrapped_greeting_body + "\n")
        print(wrapped_greeting_conclusion + "\n")
        print("--------------------------------------------------------------------------------------------\n")
        # while loop to retain the user in the post-greeting main menu of the program, until the user inputs
        # something that will restart the entire program, like the "home" command.
        while not valid_input:
            mode_selection = input("Would you like to encode or decode? (encoding from A -> Z, decoding from Z -> A): ")
            if isinstance(mode_selection, str):
                lowercase_mode_selection = mode_selection.lower()
                if lowercase_mode_selection in ["exit", "quit"]:
                    print("\nExiting program...")
                    exit()
                elif lowercase_mode_selection == "home":
                    valid_input = True
                elif lowercase_mode_selection == "encode":
                    encode_mode()
                    valid_input = True
                elif lowercase_mode_selection == "decode":
                    decode_mode()
                    valid_input = True
                else:
                    print("\033[31mYour input was invalid, please try again.\033[0m")
            else:
                print("\033[31mYour input was invalid, please try again.\033[0m")
    elif mode_selection == "encode":
        encode_mode()
    elif mode_selection == "decode":
        decode_mode()


# While true loop nested around a call to my main method, so that anytime the function is exited, especially by means
# of intention returning, I want the while loop to continue to restart the program and have it constantly be working
# until the user explicitly exits/quits the program.
while True:
    main()
