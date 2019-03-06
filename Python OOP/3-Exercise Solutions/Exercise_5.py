class Square:
    def __init__(self, side):
        self.side = side

    def __pow__(squareOne, squareTwo):
        return squareOne.side ** squareTwo.side

print('Welcome!!!')
while True:
    choice = input('Enter 1 for calculation and anyother key to quit: ')
    if choice is '1':
        sideOne = int(input('Enter the side of First Square : '))
        sideTwo = int(input('Enter the side of Second Square : '))
        squareOne = Square(sideOne)
        squareTwo = Square(sideTwo)
        print('squareOne to the Power of squareTwo is : ', squareOne ** squareTwo)
    else:
        quit()
