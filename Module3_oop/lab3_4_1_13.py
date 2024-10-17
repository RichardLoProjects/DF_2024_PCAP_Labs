'''Lab for PCAP 3.4.1.13 @ 2024-10-17'''
class WeekDayError(Exception):
    pass

class Weeker:
    __decode = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
    __encode = {v:k for k,v in __decode.items()}
    def __init__(self, day:str) -> None:
        if day not in Weeker.__decode.values():
            raise WeekDayError
        else:
            self.__day = Weeker.__encode[day]
    def __str__(self) -> str:
        return Weeker.__decode[self.__day]
    def add_days(self, n:int) -> None:
        self.__day = (self.__day + n) % len(Weeker.__decode)
    def subtract_days(self, n:int) -> None:
        self.__day = (self.__day - n) % len(Weeker.__decode)

def main() -> None:
    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print('Sorry, I can\'t serve your request.')

if __name__ == '__main__':
    main()
