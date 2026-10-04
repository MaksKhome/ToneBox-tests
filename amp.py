class Amp:
    def __init__(self, name):
        self.name = name
        self.gain = 5
        self.bypass = False

    def set_gain(self, value):
        self.gain = value

    def describe(self):
        return f"{self.name}: gain={self.gain}, bypass={self.bypass}"