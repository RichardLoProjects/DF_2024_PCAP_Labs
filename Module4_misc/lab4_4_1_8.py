'''Lab for PCAP 4.4.1.8 @ 2024-10-31'''
import os

def _helper(path:str, dir:str, data:list, print_result:bool, accum:str='..') -> None:
    new_path = accum + ('' if accum == '..' else '/') + path
    if dir in path:
        if print_result:
            print(new_path)
        else:
            data.append(new_path)
    else:
        for p in os.listdir(new_path[4:]):
            _helper(p, dir, data, print_result, new_path)

def find(path:str, dir:str, print_result:bool=False) -> list:
    valid_paths = []
    _helper(path, dir, valid_paths, print_result)
    return valid_paths if not print_result else None

def main() -> None:
    try:
        find('./tree', 'python')
    except:
        print('Function was tested in Google Colab')

if __name__ == '__main__':
    main()



'''
helper notes


_NOTE 0 proposed output
find('tree','python') --> [
    '.../tree/python'
    , '.../tree/cpp/other_courses/python'
    , '.../tree/c/other_courses/python'
]


_NOTE 1: pseudocode
example shows bredth first search
pseudocode find(path, dir):
    if dir in path:
        return path
    else:
        if listdir not empty:
            return find(new_path, dir)
        else:
            return no-path


_NOTE 2: tangible dictionary to avoid unfamiliarity with os module
my_tree = {'tree':[
    {'c':[
        {'other_courses':[
            'cpp',
            'python'
        ]}
    ]},
    {'cpp':[
        {'other_courses':[
            'c',
            'python'
        ]}
    ]},
    {'python':[
        {'other_courses':[
            'cpp',
            'c'
        ]}
    ]}
]}


_NOTE 3: function attempt for dictionary structure
def p(t,q,accum=''):
    if isinstance(t,str):
        if q in t:
            print(accum+t)
    elif q in list(t.keys())[0]:
        print(accum+list(t.keys())[0])
    else:
        for s in list(t.values())[0]:
            p(s,q,accum+list(t.keys())[0]+'/')
p(my_tree,'python')
'''
