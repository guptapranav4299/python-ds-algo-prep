class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
            return True
        else:
            return False

    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
            return True
        else:
            return False

    def pop1(self):
        if self.top1 > 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            return None

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            return None

    def size1(self):
        return self.top1 + 1

    def size2(self):
        return self.size - self.top2

    def get_stack(self):
        return self.arr


if __name__ == "__main__":
    n = 5
    obj = TwoStacks(n)
    obj.push1(10)
    obj.push1(20)
    obj.push2(30)
    print(obj.size2())
    print(obj.size1())
    obj.pop1()
    print(obj.size1())
    obj.pop2()
    print(obj.size2())