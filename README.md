Number Systems Conversion Tool

A command-line tool written in Python for converting numbers between hexadecimal, binary, and decimal systems. This script provides an interactive menu for users to select a conversion type and input a number string.

The conversions are performed manually without using Python's built-in base conversion functions (int(), bin(), hex()).

Features
Hexadecimal to Decimal: Converts hexadecimal strings (e.g., 0x1A or ff) to their decimal equivalent.

Binary to Decimal: Converts binary strings (e.g., 0b1010) to their decimal equivalent.

Binary to Hexadecimal: Converts binary strings to their hexadecimal equivalent.

Interactive Menu: A simple, looping menu to guide the user through the conversion options.

Prefix Handling: Correctly processes strings with or without 0x (for hex) and 0b (for binary) prefixes.

Case-Insensitive: Handles both uppercase (A-F) and lowercase (a-f) hexadecimal characters.

How to Run
Make sure you have Python installed.

Save the code as a Python file (e.g., Lab5.py).

Run the script from your terminal:

python Lab5.py

The program will display a menu. Enter the number corresponding to your desired conversion and follow the prompts.

Example Interaction:

    Decoding Menu
    -------------
    1. Decode hexadecimal
    2. Decode binary
    3. Convert binary to hexadecimal
    4. Quit
    
    Please enter an option: 1
Please enter the numeric string to convert: 0x4321
Result: 17185

Core Functions
hex_char_decode(digit)
Decodes a single hexadecimal character (like 'A' or '7') and returns its integer value (0-15).

hex_string_decode(hex)
Converts an entire string of hexadecimal characters into its decimal (base-10) equivalent. It iterates through the string, converting each character and applying the correct power of 16.

Example:

decimal_value = hex_string_decode("1A")
print(decimal_value)
# Output: 26

binary_string_decode(binary)
Converts a string of binary characters ('0' and '1') into its decimal equivalent by summing the powers of 2 for each '1' in the string.

Example:

decimal_value = binary_string_decode("1101")
print(decimal_value)
# Output: 13

binary_to_hex(binary)
Converts a binary string into a hexadecimal string. This is achieved by first converting the binary string to its decimal form and then converting that decimal number to hexadecimal.

Example:

hex_value = binary_to_hex("111110000001")
print(hex_value)
# Output: F81
