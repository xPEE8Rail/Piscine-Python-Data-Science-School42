import sys


def stocks_prices():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    n = len(sys.argv)
    if n != 2:
        exit()
    for i in COMPANIES:
        if sys.argv[1].upper() == COMPANIES[i].upper():
            print(i, STOCKS[sys.argv[1].upper()])
            exit()
    print("Unknown company")


if __name__ == '__main__':
    stocks_prices()
