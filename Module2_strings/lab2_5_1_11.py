'''Lab for PCAP 2.5.1.11 @ 2024-10-14'''

_b1 = '''
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
'''

_b2 = '''
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
'''

def unnest(nested_list:list) -> list:
    lst = []
    for e in nested_list:
        lst += e
    return lst

def subsq_aux(board:list, row:int, col:int) -> bool:
    numbers = set([str(i+1) for i in range(9)])
    subsq = [[board[3*row+r][3*col+c] for c in range(3)] for r in range(3)]
    return set(unnest(subsq))==numbers

def validate_subsq(board:list) -> bool:
    return all(unnest([[subsq_aux(board,r,c) for c in range(3)] for r in range(3)]))

def validate_rows(board:list) -> bool:
    numbers = set([str(i+1) for i in range(9)])
    return all([set(row)==numbers for row in board])

def validate_cols(board:list) -> bool:
    numbers = set([str(i+1) for i in range(9)])
    return all([set([board[r][c] for r in range(9)])==numbers for c in range(9)])

def valid_sudoku_board(board:str) -> bool:
    board = board.replace('\n','').replace(' ','')
    _b = [list(board[9*row:9*(row+1)]) for row in range(9)]
    return validate_rows(_b) and validate_cols(_b) and validate_subsq(_b)

def run_tests() -> None:
    assert valid_sudoku_board(_b1)
    assert not valid_sudoku_board(_b2)
    print('Passed tests!!')

def main() -> None:
    run_tests()

if __name__ == '__main__':
    main()
