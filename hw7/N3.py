class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
        #self.result = result

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')


    def __mul__(self, other):

        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):

        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(5)
cells2 = Cell(2)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(4))
print(cells1.make_order(8))
print(cells1 / cells2)
