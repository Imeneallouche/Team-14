#encoded flag
encodedflag = "67c5645ot4vo56b6t06gh5tr5cj6kf19x4qh19164f5kj6nx"

letter_to_hex = {
    'o': '0', 't': '1', 'v': '2', 'g': '3', 'h': '4', 'r': '5',
    'c': '6', 'j': '7', 'k': '8', 'f': '9', 'x': 'a', 'q': 'b',
    'b': 'c', 'n': 'd'  
}
pairs = [encodedflag[i:i+2] for i in range(0, len(encodedflag), 2)]

# pair to hexa convertion
hex_string = ""
for pair in pairs:
    hex_pair = ""
    for char in pair:
        if char.isdigit():
            hex_pair = char + hex_pair
        else:
            hex_pair = letter_to_hex[char] + hex_pair 
    hex_string = hex_pair + hex_string
print("hexa code:", hex_string)
decoded_message = bytes.fromhex(hex_string).decode('utf-8', errors='ignore')

print("decoded message:", decoded_message)


