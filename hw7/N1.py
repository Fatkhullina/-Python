x = [[1, 2], [1, 2, 3]]
y = [[1, 1], [1, 1]]
class Matrix:
    def __init__(self, list1):
        self.list1 = list1

    def __str__(self):
        for row in self.list1:
            print(' '.join((map(str, row))))

    def __add__(self, other):
        return list([map(sum, zip(*i)) for i in zip(self.list1, other.list1)])


a = Matrix(x)
b = Matrix(y)
a.__str__()
print(a + b)