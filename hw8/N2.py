class Zerroerror(Exception):
    def __init__(self, text):
        self.text = text

class Division:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        try:
            if self.b == 0:
                raise Zerroerror("На ноль делить нельзя!")
        except ValueError:
            print("Вы ввели не число")
        except Zerroerror as err:
            print(err)
        else:
            return self.a / self.b


s = Division(10, 1)
d = s.div()
print(d)





