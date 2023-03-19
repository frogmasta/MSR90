# ==========================================
# Title:  hid_converter.py
# Author: Eric Roth
# Date:   March 14th, 2023
# ==========================================

# https://stackoverflow.com/questions/27075328/list-of-hex-keyboard-scan-codes-and-usb-hid-keyboard-documentation
# Byte 0: Keyboard modifier bits (SHIFT, ALT, CTRL etc)
# Byte 1: reserved
# Byte 2-7: Up to six keyboard usage indexes representing the keys that are 
#           currently "pressed". 
#           Order is not important, a key is either pressed (present in the 
#           buffer) or not pressed.

from hid_keys import hid_modifers, hid_number_to_key

def hid_shift_hold(characters: list) -> list:
    new_characters = []
    for character in characters:
        prev_length = len(new_characters)
        empty_found = False 

        if character >= "a" and character <= "z":
            new_characters += character.upper()

        match character:
            case "":
                new_characters += ""
                empty_found = True
            case " ":
                new_characters += " "
            case "1": 
                new_characters += "!"
            case "2":
                new_characters += "@"
            case "3":
                new_characters += "#"
            case "4":
                new_characters += "$"
            case "5":
                new_characters += "%"
            case "6":
                new_characters += "^"
            case "7":
                new_characters += "&"
            case "8":
                new_characters += "*"
            case "9":
                new_characters += "("
            case "0":
                new_characters += ")"
            case "-":
                new_characters += "_"
            case "=":
                new_characters += "+"
            case "[":
                new_characters += "{"
            case "]":
                new_characters += "}"
            case ";":
                new_characters += ":"
            case "\'":
                new_characters += "\""
            case ",":
                new_characters += "<"
            case ".":
                new_characters += ">"
            case "/":
                new_characters += "?"
            case "`":
                new_characters += "~"

        # TODO: Put this into a map data structure so it's more readable

        # No conversion implemented and/or possible
        if prev_length >= len(new_characters) and not empty_found:
            print("WARNING: No conversion found for character {}".format(character))
            new_characters += character

    return new_characters


# Converts a single 8-byte buffer into one or more keypresses as a string
def hid_buf_to_keypresses(buf: list) -> str:
    if len(buf) != 8:
        raise ValueError
    
    # Refer to top of file
    modifier_code = buf[0]
    key_codes = buf[2:]

    try:
        mod = hid_modifers[modifier_code]
    except KeyError:
        print("Found unsupported HID Keyboard modifer with code: {}".format(hex(modifier_code)))
        raise KeyError
    
    try:
        chars = [hid_number_to_key[key] for key in key_codes]
    except KeyError:
        print("Found unsupported keyboard input: {}".format([hex(key) for key in key_codes]))
        raise KeyError

    if mod == "LSHIFT" or mod == "RSHIFT":
        chars = hid_shift_hold(chars)
    
    return ''.join(chars)
