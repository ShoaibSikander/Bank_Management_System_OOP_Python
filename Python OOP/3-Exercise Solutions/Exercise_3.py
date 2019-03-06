class Car:
    def __init__(self):
        self.carsList = {'Hatchback':30, 'Sedan':50, 'SUV':100}

    def displayCars(self):
        print('Hatchback = ', self.carsList['Hatchback'], ' US Dollars')
        print('Sedan = ', self.carsList['Sedan'], ' US Dollars')
        print('SUV = ', self.carsList['SUV'], ' US Dollars')

    def calculateRent(self, carType, Days):
        return self.carsList[carType]*Days


car = Car()
while True:
    print('Enter 1 to check the cars and their rents')
    print('Enter 2 to rent a car')
    print('Enter 3 to exit')
    choice = input('Enter your choice: ')
    if choice is '1':
        car.displayCars()
    elif choice is '2':
        carSelect = input('Which car you want to rent : ')
        noOfDays = int(input('For how many days you want to rent the car : '))
        Rent = car.calculateRent(carSelect, noOfDays)
        print('Total Rent is: ',Rent, ' US Dollars')
    else:
        quit()
