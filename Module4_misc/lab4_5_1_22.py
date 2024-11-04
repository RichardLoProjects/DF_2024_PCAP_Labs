'''Lab for PCAP 4.5.1.22 @ 2024-11-04'''
from datetime import datetime

_ = '''https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes'''

def main() -> None:
    x = datetime(2020,11,4,14,53)
    print(x.strftime('%Y/%m/%d %H:%M:%S'))
    print(x.strftime('%y/%B/%d %H:%M:%S %p'))
    print(x.strftime('%a, %Y %b %d'))
    print(x.strftime('%A, %Y %B %d'))
    print('Weekday:', x.strftime('%w'))
    print('Day of the year:', x.strftime('%j'))
    print('Week number of the year:', x.strftime('%W'))

if __name__ == '__main__':
    main()



_ = '''
pcap 4.5

.strftime()
.strptime()

datetime module
date.today()
date.fromtimestamp()
time
datetime subclass of date
timedelta

time module
time.time()
time.sleep()
'''

