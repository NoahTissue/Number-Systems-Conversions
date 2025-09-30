def hex_char_decode(dig):
    if dig in ['a', 'b', 'c', 'd', 'e', 'f']:
        dig = dig.lower()
        if dig == 'a':
            return 10
        elif dig == 'b':
            return 11
        elif dig == 'c':
            return 12
        elif dig == 'd':
            return 13
        elif dig == 'e':
            return 14
        elif dig == 'f':
            return 15
    elif dig in ['1','2','3','4','5','6','7','8','9']:
        return int(dig)
    else: return 0

def hex_string_decode(hex):
    hex = hex.lower()
    if hex.startswith('0x'):
        hex = hex[2:]
    value = 0
    power = len(hex)-1
    for digit in hex:
        value += (hex_char_decode(digit) * (16 ** power))
        power -= 1
    return value

def binary_string_decode(binary):
    if binary.startswith('0b'):
        binary = binary[2:]
    power = len(binary)-1
    value = 0
    for dig in binary:
       if dig == '1':
            value += (int(dig) * (2 ** power))
            power -= 1
            continue
       elif dig == '0':
           power -= 1
           continue
    return value


def binary_to_hex(binary):
    bDec = binary_string_decode(binary)
    if bDec == 0:
        return 0
    store = 0
    final = ''
    while bDec > 0:
        store = bDec % 16
        if store == 10:
            hex_char = 'A'
        elif store == 11:
            hex_char = 'B'
        elif store == 12:
            hex_char = 'C'
        elif store == 13:
            hex_char = 'D'
        elif store == 14:
            hex_char = 'E'
        elif store == 15:
            hex_char = 'F'
        else:
            hex_char = str(store)
        final += hex_char
        bDec = bDec // 16
    return final[::-1]

if __name__ == "__main__":
    menu = """
    Decoding Menu
    -------------
    1. Decode hexadecimal
    2. Decode binary
    3. Convert binary to hexadecimal
    4. Quit
    
    Please enter an option: """
    outer_loop = True
    while outer_loop == True:
        choice = input(menu)
        if choice == '1':
            inputHex = input('Please enter the numeric string to convert: ')
            print(f'Result: {hex_string_decode(inputHex)}')
        elif choice == '2':
            dog = input('Please enter the numeric string to convert: ')
            print(f'Result: {binary_string_decode(dog)}')
        elif choice == '3':
            cat = input('Please enter the numeric string to convert: ')
            print(f'Result: {binary_to_hex(cat)}')

        elif choice == '4':
            print('Goodbye!')
            outer_loop = False

