'''Lab for PCAP 2.5.1.8 @ 2024-10-14'''
def is_anagram(string1:str, string2:str) -> bool:
    _s1 = string1.upper().replace(' ','')
    _s2 = string2.upper().replace(' ','')
    _set = set(list(_s1)+list(_s2))
    return all([_s1.count(c)==_s2.count(c) for c in _set]) and len(_set)>0

def main() -> None:
    s1 = input('Enter 1st string: ')
    s2 = input('Enter 2nd string: ')
    maybe_ = '' if is_anagram(s1, s2) else 'NOT '
    print(f'These are {maybe_}an anagram!')

if __name__ == '__main__':
    main()
