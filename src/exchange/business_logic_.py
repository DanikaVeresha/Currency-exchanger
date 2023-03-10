
from object.exchange_block_ import *

while True:
    print(f'Hello.\n'
          f'0 - STOP\n'
          f'1 - COURSE USD\n'
          f'2 - COURSE UAH\n'
          f'3 - COURSE BCH\n'
          f'4 - EXCHANGE UAH\n'
          f'5 -  EXCHANGE USD')
    client = input('Your choise: ')
    match client:
        case '0':
            break
        case '1':
            usd()
        case '2':
            uah()
        case '3':
            bch()
        case '4':
            operationUAH()
        case '5':
            operationUSD()
        case _:
            print('Wrong choice, look in the program menu "Exchanger"')

print('SERVICE STOPPED')
