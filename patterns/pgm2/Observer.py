import abc

class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, snapshot, timestamp):
        pass

class AverageObserver(Observer):
    def update(self, snapshot, timestamp):
        avg_price = sum(stock['current_price'] for stock in snapshot) / len(snapshot)
        with open('data/Average.dat', 'a') as f:
            f.write(f'{timestamp}, Average price: {avg_price}\n')

class HighLowObserver(Observer):
    def update(self, snapshot, timestamp):
        with open('data/HighLow.dat', 'a') as f:
            f.write(f'Last updated {timestamp}\n')
            for stock in snapshot:
                try:
                    if abs(stock['current_price'] - stock['52_week_high']) / stock['52_week_high'] <= 0.01 or \
                    abs(stock['current_price'] - stock['52_week_low']) / stock['52_week_low'] <= 0.01:
                        f.write(f'{stock["ticker"]}: {stock["current_price"]}, {stock["52_week_high"]}, {stock["52_week_low"]}\n')
                except ZeroDivisionError:
                    """
                    Normally I would assume this is not intended behavior and would pass this stock,
                    but example output did include a stock with 0 52 week high or low
                    """
                    f.write(f'{stock["ticker"]}: {stock["current_price"]}, {stock["52_week_high"]}, {stock["52_week_low"]}\n')
            f.write('\n')


class SelectionObserver(Observer):
    def update(self, snapshot, timestamp):
        selected_tickers = ['ALL', 'BA', 'BC', 'GBEL', 'KFT', 'MCD', 'TR', 'WAG']
        with open('data/Selections.dat', 'a') as f:
            f.write(f'Last updated {timestamp}\n')
            for stock in snapshot:
                if stock['ticker'] in selected_tickers:
                    f.write(f"{stock['company']} {stock['ticker']} {stock['current_price']} {stock['dollar_change']} {stock['percent_change']} {stock['ytd_percent_change']} {stock['52_week_high']} {stock['52_week_low']} {stock['pe_ratio']}\n")
            f.write('\n')
