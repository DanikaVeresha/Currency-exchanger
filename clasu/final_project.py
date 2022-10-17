from clasu.currency_pairs_list import *


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
            courseUSD.enter()
        case '2':
            courseUAH.enter()
        case '3':
            courseBCH.enter()
        case '4':
            courseUSD.operationUAH()
        case '5':
            courseUAH.operationUSD()
        case _:
            print('Wrong choice, look in the program menu "Exchanger"')

print('SERVICE STOPPED')













