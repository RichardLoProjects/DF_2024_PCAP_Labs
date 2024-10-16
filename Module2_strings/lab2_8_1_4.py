'''Lab for PCAP 2.8.1.4 @ 2024-10-16'''
def read_int(prompt:str, min_limit:int, max_limit:int) -> int:
    result = None
    ass_err_range = f'({min_limit}..{max_limit})'
    while result is None:
        try:
            result = int(input(prompt))
            assert result in range(min_limit, 1+max_limit)
        except ValueError:
            print('Error: wrong input')
            result = None
        except AssertionError:
            print(f'Error: the value is not within the range {ass_err_range}')
            result = None
    return result

def main() -> None:
    v = read_int('Enter a number from -10 to 10: ', -10, 10)
    print(f'The number is: {v}')

if __name__ == '__main__':
    main()
