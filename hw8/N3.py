class ValueError(Exception):
    def __init__(self, text):
        self.text = text

my_list = []
number = []
while number != 'Stop':
    try:
        number = input("Введите число и нажмите Enter или Stop для остановки: ")

        if number.isdigit() == False:
           raise ValueError("ВЫ ввели не число")

        else:
            number = int(number)
            my_list.append(number)
            print(my_list)
    except ValueError as err:
        print(err)



