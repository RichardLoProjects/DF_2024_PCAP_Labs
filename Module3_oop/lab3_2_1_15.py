'''Lab for PCAP 3.2.1.15 @ 2024-10-17'''
class QueueError(IndexError):
    pass

class Queue:
    def __init__(self) -> None:
        self.__q = []
    def put(self, element) -> None:
        self.__q.insert(0, element)
    def get(self):
        if len(self.__q) == 0:
            raise QueueError
        else:
            val = self.__q[-1]
            del self.__q[-1]
            return val

def main() -> None:
    que = Queue()
    que.put(1)
    que.put('dog')
    que.put(False)
    try:
        for _ in range(4):
            print(que.get())
    except:
        print('Queue error')

if __name__ == '__main__':
    main()
