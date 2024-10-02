from multipledispath import dispatch


class num:
    @dispatch
    def add(self, a):
        print(a)

    @dispatch
    def add(self, a, b):
        print(a+b)

    @dispatch
    def add(self, a, b, c):
        print(a+b+c)
n = num()
n.add(20, 30, 40)
n.add(10)