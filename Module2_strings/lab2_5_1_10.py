'''Lab for PCAP 2.5.1.10 @ 2024-10-14'''
def is_substring(string1:str, string2:str) -> bool:
    _s1 = string1.upper()
    _s2 = string2.upper()
    ##return set(_s1).issubset(set(_s2))
    _position = 0
    while len(_s1)>0 and _position!=-1:
        _position = _s2.find(_s1[0])
        _s1 = _s1[1:]
        _s2 = _s2[1+_position:]
    return _position != -1

def main() -> None:
    prompt = 'Enter string: '
    s1 = input(prompt)
    s2 = input(prompt)
    result = 'Yes' if is_substring(s1, s2) else 'No'
    print(result)

if __name__ == '__main__':
    main()
