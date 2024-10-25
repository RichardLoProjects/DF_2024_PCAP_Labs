def mysplit(input_string):
    '''Lab for PCAP 2.3.1.18 @ 2024-10-11, updated 2024-10-25'''
    lst = []
    position = 0
    white_space = {'', ' ', '\n', '\t'}
    input_string += ' '
    while len(input_string)>0 and position!=-1:
        position = input_string.find(' ')
        word = input_string[:position]
        if word not in white_space:
            lst.append(word)
        input_string = input_string[1+position:]
    return lst

def mysplit2(input_string:str) -> list:
    white_space = {'', ' ', '\n', '\t'}
    words = []
    left = ''
    right = input_string + ' '
    while len(right) > 0:
        char = right[0]
        right = right[1:]
        if char in white_space:
            if left != '':
                words.append(left)
                left = ''
        else:
            left += char
    return words
