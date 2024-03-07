from Observer import AverageObserver, HighLowObserver, SelectionObserver
class LocalStock:
    def __init__(self):
        self.observers = []
        self.data = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, timestamp):
        for observer in self.observers:
            observer.update(self.data, timestamp)

    def read_data(self, filename):
        with open(filename, 'r') as f:
            content = f.read()
        snapshots = content.strip().split('\n\n')
        for snapshot in snapshots:
            lines = snapshot.split('\n')
            timestamp = lines[0].replace('Last updated ', '')
            self.data = []
            for line in lines[1:]:
                # Split the line by spaces and grab the last 8 fields as numeric data
                parts = line.split()
                numeric_fields = parts[-8:] # numeric and ticker
                company_name = " ".join(parts[:-8])  # Everything else is the company name

                # Extract numeric fields
                ticker, current_price, dollar_change, percent_change, ytd_percent_change, week_high, week_low, pe_ratio = numeric_fields
                if week_high == '0' or week_low == '0':
                    print('stock with 0 52 week high or low', line)
                # Convert numeric strings to appropriate types, handling '-' for P/E Ratio
                pe_ratio = pe_ratio if pe_ratio != '-' else '0'

                self.data.append({
                    'company': company_name,
                    'ticker': ticker,
                    'current_price': float(current_price),
                    'dollar_change': float(dollar_change),
                    'percent_change': float(percent_change),
                    'ytd_percent_change': float(ytd_percent_change),
                    '52_week_high': float(week_high),
                    '52_week_low': float(week_low),
                    'pe_ratio': float(pe_ratio)
                })
            self.notify_observers(timestamp)

if __name__ == '__main__':
    stock = LocalStock()
    stock.add_observer(AverageObserver())
    stock.add_observer(HighLowObserver())
    stock.add_observer(SelectionObserver())
    stock.read_data('data/Ticker.dat')