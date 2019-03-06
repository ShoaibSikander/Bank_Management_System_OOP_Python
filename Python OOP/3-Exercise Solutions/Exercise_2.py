class PreciousStone:
    noOfStones = 0
    stoneCollection = []
    def __init__(self):
        print("Class initiated!!!")
    def addNewStone(self, newStone):
        if self.noOfStones<5:
            self.noOfStones += 1
            self.stoneCollection.append(newStone)
        else:
            del self.stoneCollection[0]
            self.stoneCollection.append(newStone)
    def availableStone(self):
        print(self.stoneCollection)

stone = PreciousStone()
while True:
    print("Enter 1 if you want to add a new Precious Stone")
    print("Enter 2 if you want to see already present Precious Stones")
    print("Enter 3 to Exit")
    a = input('Enter your input:')
    print("You Entered : ", a)
    if a=='1':
        print("A new stone will be added!!!")
        stn = input('Enter the name of stone: ')
        stone.addNewStone(stn)
    elif a=='2':
        print("List of available stones will be shown!!!")
        stone.availableStone()
    else:
        break
