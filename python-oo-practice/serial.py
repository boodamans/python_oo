"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """starts generator"""
        self.start = start
        self.start_num = self.start

    def generate(self):
        """adds 1 to previous number"""
        self.start = self.start + 1
        return self.start -1

    def reset(self):
        """resets serial number back to starting number"""
        self.start = self.start_num

    