
from collections import namedtuple

curs = namedtuple('curs', ['curse', 'rate', 'available'])


def usd():
    for item in courseUSD:
        print(f'\n Course: {item.curse} | Rate: {item.rate}'
              f'\n Available: {item.available} USD\n')


def uah():
    for item in courseUAH:
        print(f'\n Course: {item.curse} | Rate: {item.rate}'
              f'\n Available: {item.available} UAH\n')


def bch():
    for item in courseBCH:
        print(f'\n Course: {item.curse} | Rate: {item.rate}'
              f'\n Available: {item.available}\n')


def dec_1(func):
    def inner():
        print('----------------------------------------------------------------')
        func()
        print('----------------------------------------------------------------')
    return inner


@dec_1
def operationUAH():
    try:
        client = int(input('Amount in UAH: '))
        if client > 0:
            value = courseUSD
            for item in value:
                result = client / item.rate
                result1 = 1 / item.rate
                result2 = item.available - result
                if item.available >= result:
                    print(f'Available balance at the beginning of the operation: {item.available} USD\n'
                          f'UAH conversion: {round(result, 4)} USD| RATE: {round(result1, 6)}\n'
                          f'Balance update: {round(result2, 2)} USD\n')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {round(result, 2)} USD\n'
                          f'Available balance: {item.available} USD\n')
        else:
            print(f'Your exchange request:{client} is not correct')
        return operationUAH
    except ValueError:
        print('Your exchange request is not correct,value must be an integer')
    finally:
        print('Verification done')


@dec_1
def operationUSD():
    try:
        client = int(input('Amount in USD: '))
        if client > 0:
            value = courseUAH
            for item in value:
                result = client * item.rate
                result1 = 1 * item.rate
                result2 = item.available - result
                if item.available >= result:
                    print(f'Available balance at the beginning of the operation: {item.available} UAH\n'
                          f'USD conversion: {result} UAH| RATE: {result1}\n'
                          f'Balance update: {result2} UAH\n')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {result} UAH\n'
                          f'Available balance: {item.available} UAH\n')
        else:
            print(f'Your exchange request:{client} is not correct')
        return operationUSD
    except ValueError:
        print(f'Your exchange request is not correct,value must be an integer')
    finally:
        print('Verification done')


courseUSD = [curs('USD', 27.5, 13500.98)]
courseUAH = [curs('UAH', 27.3, 39345.5)]
courseBCH = [curs('BCH', 0.00, 'INVALID CURRENCY BCH')]
