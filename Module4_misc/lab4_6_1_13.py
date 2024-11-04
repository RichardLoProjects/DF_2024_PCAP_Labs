'''Lab for PCAP 4.6.1.13 @ 2024-11-04'''
from calendar import Calendar

class MyCalendar(Calendar):
    def __init__(self) -> None:
        super().__init__()
    def count_weekday_in_year(self, year:int, weekday:int) -> int:
        assert weekday in range(7), 'Weekday is not in 0-6'
        result = 0
        for month in range(1, 1+12):
            for week in self.monthdays2calendar(year, month):
                for date, day_of_week in week:
                    if date != 0 and day_of_week == weekday:
                        result += 1
        return result

def main() -> None:
    try:
        x = MyCalendar()
        assert 52 == x.count_weekday_in_year(2019, 0)
        assert 53 == x.count_weekday_in_year(2000, 6)
        print('Passed!!')
    except:
        print('Failed :(')

if __name__ == '__main__':
    main()
