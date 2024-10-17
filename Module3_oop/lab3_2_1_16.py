'''Lab for PCAP 3.2.1.16 @ 2024-10-17'''
class QueueError(IndexError):
    pass

class Queue:
    def __init__(self) -> None:
        self.queue = []
    def put(self, element) -> None:
        self.queue.insert(0, element)
    def get(self):
        if len(self.queue) == 0:
            raise QueueError
        else:
            val = self.queue[-1]
            del self.queue[-1]
            return val

class SuperQueue(Queue):
    def __init__(self):
        super().__init__()
    def isempty(self) -> bool:
        # Child was not able to access self.__q, and self._Queue__q is discouraged.
        return len(self.queue) == 0

def main() -> None:
    que = SuperQueue()
    que.put(1)
    que.put('dog')
    que.put(False)
    for _ in range(4):
        if not que.isempty():
            print(que.get())
        else:
            print('Queue empty')

if __name__ == '__main__':
    main()
