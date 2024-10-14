'''Lab for PCAP 2.5.1.7 @ 2024-10-14'''
def is_palindrome(sample_string:str) -> bool:
    s = sample_string.lower().replace(' ','')
    return s==s[::-1] and len(s)>0

def main() -> None:
    sample = input('Enter string: ')
    maybe_ = '' if is_palindrome(sample) else 'NOT '
    print(f'Your string is {maybe_}a palindrome!')

if __name__ == '__main__':
    main()
