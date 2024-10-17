'''Lab for PCAP 3.4.1.12 @ 2024-10-17'''
class Timer:
    __hrange = range(24)
    __mrange = range(60)
    __srange = range(60)
    def __init__(self, hour:int=0, minute:int=0, second:int=0) -> None:
        self.__h = hour
        self.__m = minute
        self.__s = second
    def __str__(self) -> str:
        return f'{pad(self.__h)}:{pad(self.__m)}:{pad(self.__s)}'
    def next_second(self) -> None:
        self.__s += 1
        if self.__s > max(Timer.__srange):
            self.__s -= len(Timer.__srange)
            self.__m += 1
            if self.__m > max(Timer.__mrange):
                self.__m -= len(Timer.__mrange)
                self.__h += 1
                if self.__h > max(Timer.__hrange):
                    self.__h -= len(Timer.__hrange)
    def prev_second(self) -> None:
        self.__s -= 1
        if self.__s < min(Timer.__srange):
            self.__s += len(Timer.__srange)
            self.__m -= 1
            if self.__m < min(Timer.__mrange):
                self.__m += len(Timer.__mrange)
                self.__h -= 1
                if self.__h < min(Timer.__hrange):
                    self.__h += len(Timer.__hrange)

def pad(number:int) -> str:
    assert number in range(60), 'Could not pad number outside range 0-59.'
    _p = '0' if number in range(10) else ''
    return _p + str(number)

def main() -> None:
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)

if __name__ == '__main__':
    main()
