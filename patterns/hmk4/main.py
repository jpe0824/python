class DisplayDriver:
    def draw(self):
        pass

class PrintDriver:
    def print(self):
        pass

class DriverFactory:
    def get_display_driver(self):
        pass
    def get_print_driver(self):
        pass

class LowResDisplayDriver(DisplayDriver):
    def draw(self):
        return "Drawing a widget using a LowResDisplayDriver"

class HighResDisplayDriver(DisplayDriver):
    def draw(self):
        return "Drawing a widget using a HighResDisplayDriver"

class LowResPrintDriver(PrintDriver):
    def print(self):
        return "Printing a widget using a LowResPrintDriver"

class HighResPrintDriver(PrintDriver):
    def print(self):
        return "Printing a widget using a HighResPrintDriver"

class LowResDriverFactory(DriverFactory):
    def get_display_driver(self):
        return LowResDisplayDriver()
    def get_print_driver(self):
        return LowResPrintDriver()

class HighResDriverFactory(DriverFactory):
    def get_display_driver(self):
        return HighResDisplayDriver()
    def get_print_driver(self):
        return HighResPrintDriver()

class Widget:
    def __init__(self, display_driver):
        self.display_driver = display_driver

    def draw(self):
        print(self.display_driver.draw())

class Document:
    def __init__(self, print_driver):
        self.print_driver = print_driver

    def print(self):
        print(self.print_driver.print())

def main(resolution="low"):
    if resolution == "low":
        factory = LowResDriverFactory()
    else:
        factory = HighResDriverFactory()

    widget = Widget(factory.get_display_driver())
    document = Document(factory.get_print_driver())

    widget.draw()
    document.print()

if __name__ == "__main__":
    # main('high')
    main()