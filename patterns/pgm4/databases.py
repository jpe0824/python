class Database:
    """
    Simple database implementation
    """
    def __init__(self, id) -> None:
        self.id = id
        self.data = {}

    def get_id(self):
        return self.id

    def add(self, key, value):
        if key in self.data:
            raise ValueError(f'Key {key} already exists')
        self.data[key] = value

    def get(self, key):
        return self.data.get(key, None)

    def update(self, key, value):
        if key not in self.data:
            raise ValueError(f'Key {key} does not exist')
        self.data[key] = value

    def remove(self, key):
        if key not in self.data:
            raise ValueError(f'Key {key} does not exist')
        del self.data[key]

    def display(self, show_db_id=False):
        if show_db_id:
            print(f'Database {self.id}:')
        for key, value in self.data.items():
            print(f'{key}| {value}')