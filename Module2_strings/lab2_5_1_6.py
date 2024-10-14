'''Lab for PCAP 2.5.1.6 @ 2024-10-14'''
def get_message() -> str:
    return input('Enter message: ')

def get_shiftvalue() -> int:
    n = -1
    while n == -1:
        try:
            n = int(input('Enter shift value (1-25 inclusive): '))
            if n not in {i+1 for i in range(25)}:
                n = -1
        except ValueError:
            n = -1
    return n

def is_letter(char:str) -> bool:
    ascii_numbers = set(list(range(65,65+26)) + list(range(97,97+26)))
    return char.isalpha() and ord(char) in ascii_numbers

def encode(msg:str, shift:int) -> str:
    msg_out = ''
    for c in msg:
        if not is_letter(c):
            msg_out += c
        elif c.isupper():
            code_pt_offset = (ord(c)-ord('A')+shift)%26
            msg_out += chr(65 + code_pt_offset)
        else:
            code_pt_offset = (ord(c)-ord('a')+shift)%26
            msg_out += chr(97 + code_pt_offset)
    return msg_out

def decode(msg:str, shift:int) -> str:
    msg_out = ''
    for c in msg:
        if not is_letter(c):
            msg_out += c
        elif c.isupper():
            code_pt_offset = (ord(c)-ord('A')-shift)%26
            msg_out += chr(65 + code_pt_offset)
        else:
            code_pt_offset = (ord(c)-ord('a')-shift)%26
            msg_out += chr(97 + code_pt_offset)
    return msg_out

def main() -> None:
    message = get_message()
    shiftvalue = get_shiftvalue()
    encryption = encode(message, shiftvalue)
    decryption = decode(encryption, shiftvalue)
    print(encryption)
    print(decryption)

if __name__ == '__main__':
    main()
