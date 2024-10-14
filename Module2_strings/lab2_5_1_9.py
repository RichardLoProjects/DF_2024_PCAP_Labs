'''Lab for PCAP 2.5.1.9 @ 2024-10-14'''
def digit_of_life(date_of_birth:str) -> int:
    s = date_of_birth
    d = -1
    while d not in set(range(10)):
        d = sum([int(c) for c in s])
        s = str(d)
    return d

def main() -> None:
    valid = False
    prompt = 'Enter dob in format YYYYMMDD or YYYYDDMM or MMDDYYYY: '
    while not valid:
        dob = input(prompt)
        valid = dob.isdigit() and len(dob)==8
    print(digit_of_life(dob))

if __name__ == '__main__':
    main()
