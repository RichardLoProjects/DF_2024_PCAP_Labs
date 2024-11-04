func = None
data = None

############################################ 4.1

# iterator objects
# __iter__, __next__, StopIteration
# generators
# yield keyword
# list comprehension [asdf], generator (asdf)
# len(generator) raises TypeError
map(func, data), filter(func, data)
# functions inside functions (closure)

## PEP8 style recommends
def f(x): return 3*x # recommended
f = lambda x: 3*x # not recommended

############################################ 4.2
# 4.2.1 ... 8,10,11,12

# r,w,a,r+,w+,x (rt,rb)
'''
with open(filename, mode = 'rt', encoding = None) as f:
    ## f.read() -> str, f.read(n) -> str, f.readline() -> str, f.readlines(n) -> list[str]
    ## f.read() reads the whole file while f.read(1) reads one char at a time
    ## WARNING: reading a terabyte-long file using this method may corrupt your OS
    pass # file auto closes when exiting the "with" statement


# open() is an instance of the iterable class: its __next__ method just
# returns the next line read in from the file
# Moreover, you can expect that the object automatically
# invokes close() when any of the file reads reaches the end of the file.


try:
    stream = open(filename, 'rt')
    # Processing goes here.
    stream.close()
except Exception as exc:
    print('Cannot open the file:', exc)

    
try:
    # Some stream operations.
except IOError as exc:
    print(exc.errno)

    
from os import strerror
try:
    s = open(filename, "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))


'''

