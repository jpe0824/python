from Observer import AverageObserver, HighLowObserver, SelectionObserver

class LocalStock:
    def __init__(self):
        self.observers = []
        self.data = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.data)

    def read_data(self, filename):
        pass

    def process_data(self):
        self.read_data('.dat')
        self.notify_observers()

if __name__ == '__main__':
    stock = LocalStock()
    stock.add_observer(AverageObserver())
    stock.add_observer(HighLowObserver())
    stock.add_observer(SelectionObserver())
    stock.process_data()