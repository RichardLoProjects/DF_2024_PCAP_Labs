'''Lab for PCAP 3.2.1.14 @ 2024-10-17'''
class Stack:
    def __init__(self):
        self.__stk = []
    def push(self, val):
        self.__stk.append(val)
    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self) -> None:
        self.__counter = 0
        super().__init__()
    def get_counter(self) -> int:
        return self.__counter
    def pop(self):
        super().pop()
        self.__counter += 1

def main() -> None:
    stk = CountingStack()
    for i in range(100):
        stk.push(i)
        stk.pop()
    print(stk.get_counter())

if __name__ == '__main__':
    main()
