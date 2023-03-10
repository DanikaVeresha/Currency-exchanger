
from exchanger_1.currency_pairs_list import *


while True:
    print(f'Hello.\n'
          f'Enter 0 -> STOP\n'
          f'Enter 1 -> COURSE USD\n'
          f'Enter 2 -> COURSE EUR\n'
          f'Enter 3 -> COURSE BTC\n'
          f'Enter 4 -> EXCHANGE UAH -> USD\n'
          f'Enter 5 -> EXCHANGE UAH -> UER\n'
          f'Enter 6 -> EXCHANGE UAH -> BTC\n'
          f'Enter 7 -> EXCHANGE USD -> UAH\n'
          f'Enter 8 -> EXCHANGE EUR -> UAH\n'
          f'Enter 9 -> EXCHANGE BTC -> UAH')
    client = input('\nYour choise: ')
    match client:
        case '0':
            break
        case '1':
            print(f'\nCOURSE: {courseUSD.name}')
            print(f'RATE: {courseUSD.privat_course["usd"]}')
            print(f'Available_USD: {courseUSD.available}')
            print(f'Available_UAH: {courseUSD.available_uah}\n')
        case '2':
            print(f'\nCOURSE: {courseEUR.name}')
            print(f'RATE: {courseEUR.privat_course["eur"]}')
            print(f'Available_EUR: {courseEUR.available}')
            print(f'Available_UAH: {courseEUR.available_uah}\n')
        case '3':
            print(f'\nCOURSE: {courseBTC.name}')
            print(f'RATE: {courseBTC.privat_course["btc"]}')
            print(f'Available_BTC: {courseBTC.available}')
            print(f'Available_UAH: {courseBTC.available_uah}\n')
        case '4':
            courseUSD.operationUAH_USD()
        case '5':
            courseEUR.operationUAH_UER()
        case '6':
            courseBTC.operationUAH_BTC()
        case '7':
            courseUSD.operationUSD_UAH()
        case '8':
            courseEUR.operationEUR_UAH()
        case '9':
            courseBTC.operationBTC_UAH()
        case _:
            print('Wrong choice, look in the program menu "Exchanger"')

print('SERVICE STOPPED')















