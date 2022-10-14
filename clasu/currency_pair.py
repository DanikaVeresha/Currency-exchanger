from clasu.currency_pairs_list import *


class Course:

    def __init__(self, course, rate, available):
        self.course = course
        self.rate = rate
        self.available = available

    def usd(self):
        for item in courseUSD:
            return f'\n Course: {item.curse} | Rate: {item.rate}\n' \
                   f'Available: {item.available} USD\n'

    def uah(self):
        for item in courseUAH:
            return f'\n Course: {item.curse} | Rate: {item.rate}\n' \
                   f'Available: {item.available} UAH\n'

    def bch(self):
        for item in courseBCH:
            return f'\n Course: {item.curse} | Rate: {item.rate}\n' \
                   f'Available: {item.available}\n'

    def __str__(self):
        return self.usd(), self.uah(), self.bch()







