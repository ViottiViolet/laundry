class LaundryMachine(object):
    def __init__(self, company, cost):
        self.company = company
        self.cost = cost
        self.laundry = []
        self.wetOrDry = ''
        self.temp = ''
        self.speed = 0

    def inputLaundry(self, laundry):
        self.laundry = laundry
        print('youve placed')
        print(self.laundry)
        print('into your laundry machine')

    def settings(self, wetOrDry, temp, speed):
        self.wetOrDry = wetOrDry
        self.temp = temp
        self.speed = speed

        print("your settings are now: ")
        print(self.wetOrDry)
        print(self.temp)
        print(self.speed)

    def startMachine(self):
        if self.wetOrDry == 'wet':
            print('washing starts now!')
            for cloth in self.laundry:
                cloth = 'wet ' + cloth
            print(self.laundry)
        elif self.wetOrDry == 'dry':
            print('drying starts now!')
            for cloth in self.laundry:
                cloth = 'clean ' + cloth
            print(self.laundry)

pile = ['shirt', 'pant', 'pant', 'sock', 'shirt', 'sock', 'shirt', 'jeans']
mach = LaundryMachine('eugh', 200)
mach.inputLaundry(pile)
mach.settings('dry', 'warm', 5)
mach.startMachine()