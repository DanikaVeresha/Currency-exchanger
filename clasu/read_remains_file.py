from clasu.currency_pair import *


class ReadingRemains(Course):
    '''атрибуты операции обмена'''
    def __init__(self, name, rate, available):
        super().__init__(self, rate, available)
        self.name = name
        self.rate = rate
        self.available = available

    def operationUAH(self):
        '''операция обмен'''
        try:
            client = int(input('Amount in UAH: '))
            if client > 0:
                result = client / self.rate
                result1 = 1 / self.rate
                result2 = self.available - result
                if self.available >= result:
                    print(f'Available balance at the beginning of the operation: {self.available} USD\n'
                          f'UAH conversion: {round(result, 4)} USD| RATE: {round(result1, 6)}\n'
                          f'Balance update: {round(result2, 2)} USD\n')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {round(result, 2)} USD\n'
                          f'Available balance: {self.available} USD\n')
            else:
                print(f'Your exchange request:{client} is not correct')
        except ValueError:
            print('Your exchange request is not correct,value must be an integer')
        finally:
            print('Verification done')

    def operationUSD(self):
        try:
            client = int(input('Amount in USD: '))
            if client > 0:
                result = client * self.rate
                result1 = 1 * self.rate
                result2 = self.available - result
                if self.available >= result:
                    print(f'Available balance at the beginning of the operation: {self.available} UAH\n'
                          f'USD conversion: {result} UAH| RATE: {result1}\n'
                          f'Balance update: {result2} UAH\n')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {result} UAH\n'
                          f'Available balance: {self.available} UAH\n')
            else:
                print(f'Your exchange request:{client} is not correct')
        except ValueError:
            print(f'Your exchange request is not correct,value must be an integer')
        finally:
            print('Verification done')








