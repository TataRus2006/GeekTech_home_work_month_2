"""
написать валидацию на Номера Транспартов
будет класс ValidCarNumber —> будет метод is_valid(self, number)
который принимает 1 аргумент number и проверяет на валидность то есть:
Input:

    01KG777BAD
    hhh777hhh

Output:

    Номер валидный!
    Номер не валидный!
"""

import re

number_car = input("car number: ")


class ValidCarNumber:

    def __init__(self, number):
        self.number = number

    def is_valid(self):
        is_valid_number = re.search(r"(0[1-9]{1})KG([0-9]{3}[A-Z]{3})", self)
        try:
            if is_valid_number.end() == len(number_car):
                print("Номер валидный!")
            else:
                raise ValueError
        except:
            print("Номер не валидный!")


ValidCarNumber.is_valid(number_car)
