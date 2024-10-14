'''Lab for PCAP 2.4.1.6 @ 2024-10-11'''
def get_number() -> int:
    number = -1
    while number < 0:
        number = input('Enter a valid non-negative integer: ')
        try:
            number = int(number)
        except ValueError:
            number = -1
    return number

def display_led(number) -> None:
    assert (type(number) is int) and number>=0, 'Invalid number.'
    digit_dict = {
        '1': '  # -  # -  # -  # -  # '.split('-'),
        '2': '### -  # -### -#   -### '.split('-'),
        '3': '### -  # -### -  # -### '.split('-'),
        '4': '# # -# # -### -  # -  # '.split('-'),
        '5': '### -#   -### -  # -### '.split('-'),
        '6': '### -#   -### -# # -### '.split('-'),
        '7': '### -  # -  # -  # -  # '.split('-'),
        '8': '### -# # -### -# # -### '.split('-'),
        '9': '### -# # -### -  # -### '.split('-'),
        '0': '### -# # -# # -# # -### '.split('-')
    }
    number = str(number)
    for row in range(5):
        for digit in number:
            print(digit_dict[digit][row], end='')
        print('')

def main() -> None:
    number = get_number()
    print()
    display_led(number)

if __name__ == '__main__':
    main()
