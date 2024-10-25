'''Lab for PCAP 4.3.1.15 @ 2024-10-25'''
from os import strerror

def generate_testfile(file_name:str, test_string:str) -> None:
    with open(file_name, mode='wt') as file_stream:
        file_stream.write(test_string)

def extract_string(file_name:str) -> str:
    with open(file_name, mode='rt') as file_stream:
        file_contents = file_stream.read()
    return file_contents

def count_letters(input_string:str) -> dict:
    alphabet = {chr(ord('a')+i) for i in range(26)}
    return {c:input_string.lower().count(c) for c in alphabet}

def generate_histogram(letter_counts:dict) -> str:
    histogram = ''
    alphabet = sorted(letter_counts.keys())
    for letter in alphabet:
        count = letter_counts[letter]
        if count > 0:
            histogram += f'{letter} -> {count}\n'
    return histogram

def get_histogram() -> str:
    while True:
        try:
            file_name = input('Enter filename: ')
            file_data = extract_string(file_name)
            dict_data = count_letters(file_data)
            return generate_histogram(dict_data)
        except IOError as e:
            print(f'I/O error occurred: {strerror(e.errno)}')

def main() -> None:
    try:
        generate_testfile('testfile.txt', 'aBc')
        print(get_histogram())
    except IOError as e:
        print(f'I/O error occurred: {strerror(e.errno)}')

if __name__ == '__main__':
    main()
