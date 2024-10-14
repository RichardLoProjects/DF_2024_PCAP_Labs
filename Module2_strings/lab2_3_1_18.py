def mysplit(input_string):
    '''Lab for PCAP 2.3.1.18 @ 2024-10-11'''
    lst = []
    position = 0
    white_space = {'', ' ', '\n'}
    input_string += ' '
    while len(input_string)>0 and position!=-1:
        position = input_string.find(' ')
        word = input_string[:position]
        if word not in white_space:
            lst.append(word)
        input_string = input_string[1+position:]
    return lst
