# type = smartphone
# brand = motorola
# series = Edge 50 Pro
# Memory = 8GB
# Display = 6.5 inches
class Mobile:

    def __init__(self,type,brand,series,Memory,Display):
        self.type = type
        self.brand = brand
        self.series = series
        self.Memory = Memory
        self.Display = Display
    
    def display_details(self):
        print(self.type)
        print(self.brand)
        print(self.series)
        print(self.Memory)
        print(self.Display)


mobile_1 = Mobile("Smart Phone","Sony","edge","12GB","5 inches")
mobile_1.display_details()
mobile_2 = Mobile("BarPhone","Nokia","1100","2GB","2 inch")
mobile_2.display_details()