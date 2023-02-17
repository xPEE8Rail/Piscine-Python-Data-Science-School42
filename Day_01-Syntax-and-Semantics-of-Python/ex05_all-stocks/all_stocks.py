import sys


def all_stocks():
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
    list_names = sys.argv[1].replace(' ', '').split(',')
    if '' in list_names:
        exit()
    for i in list_names:
        if i.capitalize() in COMPANIES:
            print(i.capitalize(), "stock price is", STOCKS[COMPANIES[i.capitalize()]])
        elif i.upper() in STOCKS:
            for j in COMPANIES:
                if i.upper() == COMPANIES[j]:
                    print(i.upper(), "is a ticker symbol for", j)
                    break
        else:
            print(i, "is an unknown company or an unknown ticker symbol")


if __name__ == '__main__':
    all_stocks()
