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
    pass # file auto closes when exiting the "with" statement


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

