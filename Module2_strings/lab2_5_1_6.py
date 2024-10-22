'''Lab for PCAP 2.5.1.6 @ 2024-10-14, updated 2024-10-22'''
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

def transform(msg:str, shift:int, decode:bool=False) -> str:
    _sgn = -1 if decode else 1
    msg_out = ''
    for c in msg:
        if is_letter(c):
            ord_a = ord('A') if c.isupper() else ord('a')
            code_pt_offset = (ord(c) - ord_a + _sgn*shift)%26
            msg_out += chr(ord_a + code_pt_offset)
        else:
            msg_out += c
    return msg_out

def main() -> None:
    my_message = get_message()
    shiftvalue = get_shiftvalue()
    encryption = transform(my_message, shiftvalue)
    decryption = transform(encryption, shiftvalue, True)
    print(f'encryption: {encryption}')
    print(f'decryption: {decryption}')

if __name__ == '__main__':
    main()
