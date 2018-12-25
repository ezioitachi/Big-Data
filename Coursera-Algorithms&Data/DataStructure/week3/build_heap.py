# python3


class HeapBuilder:

    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def left(self, i ):
      return i*2+1
    def right(self, i):
      return i*2+2

    def SiftDown(self, i):
      size = len(self._data) - 1
      idx = i
      l = self.left(i)
      if l <= size and self._data[l] < self._data[idx]:
        idx = l
      r = self.right(i)
      if r <= size and self._data[r] < self._data[idx]:
        idx = r
      if i != idx:
        self._swaps.append((i, idx))
        self._data[i], self._data[idx] = self._data[idx], self._data[i]
        self.SiftDown(idx)

    def GenerateSwaps(self):
        for i in reversed(range(0, len(self._data))):
          self.SiftDown(i)


    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()