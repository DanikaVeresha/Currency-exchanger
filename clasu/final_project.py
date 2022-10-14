from clasu.read_remains_file import *


def main(i):
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
                print(i.usd())
            case '2':
                print(i.uah())
            case '3':
                print(i.bch())
            case '4':
                print(i.operationUAH())
            case '5':
                print(i.operationUSD())
            case _:
                print('Wrong choice, look in the program menu "Exchanger"')

    print('SERVICE STOPPED')


if __name__ == "__main__":
    i = ReadingRemains(courseUAH, courseUSD, courseBCH)
    main(i)




