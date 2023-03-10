

class Course:

    def __init__(self, name, rate, available):
        '''атрибуты валютной пары'''
        self.name = name
        self.rate = rate
        self.available = available

    def enter(self):
        '''выводит курс валюты на екран'''
        print(f'Course: {self.name} | Rate: {self.rate}\n'
              f'Available: {self.available}\n')










