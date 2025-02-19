class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit
        self.conversions = {
            'inches': 1,
            'feet': 12,
            'yards': 36,
            'miles': 63360,
            'kilometers': 39370.1,
            'meters': 39.3701,
            'centimeters': 0.393701,
            'millimeters': 0.0393701
        }
    
    def to_inches(self):
        return self.length * self.conversions[self.unit]
    
    def inches(self):
        return self.to_inches()
    
    def feet(self):
        return self.to_inches() / self.conversions['feet']
    
    def yards(self):
        return self.to_inches() / self.conversions['yards']
    
    def miles(self):
        return self.to_inches() / self.conversions['miles']
    
    def kilometers(self):
        return self.to_inches() / self.conversions['kilometers']
    
    def meters(self):
        return self.to_inches() / self.conversions['meters']
    
    def centimeters(self):
        return self.to_inches() / self.conversions['centimeters']
    
    def millimeters(self):
        return self.to_inches() / self.conversions['millimeters']
