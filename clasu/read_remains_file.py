from clasu.currency_pair import *


class ReadingRemains:
    def __init__(self, original_balance, request):
        self.available = original_balance
        self.request = request
        self.final_balance = self.available - self.request

    def operationUAH(self):
        try:
            self.request = int(input('Amount in UAH: '))
            if self.request > 0:
                value = courseUSD
                for item in value:
                    result = self.request / item.rate
                    result1 = 1 / item.rate
                    result2 = item.available - result
                    if item.available >= result:
                        return f'Available balance at the beginning of the operation: {item.available} USD\n' \
                               f'UAH conversion: {round(result, 4)} USD| RATE: {round(result1, 6)}\n' \
                               f'Balance update: {round(result2, 2)} USD\n'
                    else:
                        return f'Sorry, error.The currency balance is not enough\n' \
                               f'To complete the transaction, you must: {result} USD\n' \
                               f'Available balance: {item.available} USD\n'
            else:
                return f'Your exchange request:{self.request} is not correct'
            return self.operationUAH
        except ValueError:
            return 'Your exchange request is not correct,value must be an integer'
        finally:
            return f'Verification done'

    def operationUSD(self):
        try:
            self.request = int(input('Amount in USD: '))
            if self.request > 0:
                value = courseUAH
                for item in value:
                    result = self.request * item.rate
                    result1 = 1 * item.rate
                    result2 = item.available - result
                    if item.available >= result:
                        return f'Available balance at the beginning of the operation: {item.available} UAH\n' \
                               f'USD conversion: {result} UAH| RATE: {result1}\n' \
                               f'Balance update: {result2} UAH\n'
                    else:
                        return f'Sorry, error.The currency balance is not enough\n' \
                               f'To complete the transaction, you must: {result} UAH\n' \
                               f'Available balance: {item.available} UAH\n'
            else:
                return f'Your exchange request:{self.request} is not correct'
            return self.operationUSD
        except ValueError:
            return f'Your exchange request is not correct,value must be an integer'
        finally:
            return 'Verification done'

    def __str__(self):
        return self.operationUAH(), self.operationUSD()






