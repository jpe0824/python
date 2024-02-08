import abc

class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, data):
        pass

class AverageObserver(Observer):
    # Implement logic to calculate average price and write to Average.dat

    def __init__(self):
        self.data = []

    def update(self, data):
        self.data.append(data)
        print(f'Average: {sum(self.data)/len(self.data)}')

class HighLowObserver(Observer):
    # Implement logic to find stocks close to 52-week high/low and write to HighLow.dat

    def __init__(self):
        self.data = []

    def update(self, data):
        self.data.append(data)
        print(f'High: {max(self.data)}, Low: {min(self.data)}')

class SelectionObserver(Observer):
    # Implement logic to display fields for specific companies and write to Selections.dat

    def __init__(self):
        self.data = []

    def update(self, data):
        self.data.append(data)
        print(f'Selection: {data}')