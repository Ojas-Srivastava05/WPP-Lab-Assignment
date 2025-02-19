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

length = float(input("Enter the length: "))
unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").strip().lower()
converter = Converter(length, unit)

target_unit = input("Convert to (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").strip().lower()
if hasattr(converter, target_unit):
    print(getattr(converter, target_unit)())
else:
    print("Invalid target unit.")