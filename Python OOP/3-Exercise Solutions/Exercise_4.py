class Furniture:
    def __init__(self):
        self._TypeOfWood = 'Teakwood'

class Chair(Furniture):
    def __init__(self):
        super().__init__()
        self.__Legs = 4

    def setWoodType(self):
        self._TypeOfWood = input('Which materials chair do you need? : ')

    def dispChair(self):
        print("You chair is made of {} and it has {} legs".format(self._TypeOfWood, self.__Legs))

print('Welcome')
while True:
    chair = Chair()
    ans = input('Enter 1 to select chair and 2 to quit : ')
    if ans is '1':
        print('By default, chair is made of Teakwood. Do you want to changes the material?')
        choice = input('Type y for Yes or n for No: ')
        if choice is 'y':
            chair.setWoodType()
            chair.dispChair()
        else:
            chair.dispChair()
    else:

        quit()
