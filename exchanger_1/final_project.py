from exchanger_1.currency_pairs_list import *


while True:
    print(f'Hello.\n'
          f'0 - STOP\n'
          f'1 - COURSE USD\n'
          f'2 - COURSE EUR\n'
          f'3 - COURSE BTC\n'
          f'4 - EXCHANGE UAH <-> USD\n'
          f'5 - EXCHANGE UAH <-> UER\n'
          f'6 - EXCHANGE UAH <-> BTC\n'
          f'7 - EXCHANGE USD <-> UAH\n'
          f'8 - EXCHANGE EUR <-> UAH\n'
          f'9 - EXCHANGE BTC <-> UAH')
    client = input('Your choise: ')
    match client:
        case '0':
            break
        case '1':
            print(f'COURSE: {courseUSD.name}')
            print(f'RATE: {courseUSD.privat_course["usd"]}')
            print(f'Available: {courseUSD.available} USD')
            print(f'Available: {courseUSD.available_uah} UAH')
        case '2':
            print(f'COURSE: {courseEUR.name}')
            print(f'RATE: {courseEUR.privat_course["eur"]}')
            print(f'Available: {courseEUR.available} EUR')
            print(f'Available: {courseEUR.available_uah} UAH')
        case '3':
            print(f'COURSE: {courseBTC.name}')
            print(f'RATE: {courseBTC.privat_course["btc"]}')
            print(f'Available: {courseBTC.available}')
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













