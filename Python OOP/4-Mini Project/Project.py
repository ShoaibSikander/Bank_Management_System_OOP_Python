from random import randint

class BankAccount:
    def __init__(self):
        self.bankRecord = {}

    def createNewAccount(self, name, initialDeposit):
        self.randomNumber = randint(10000, 99999)
        self.accountNumber = self.randomNumber
        self.bankRecord[self.accountNumber] = [name, initialDeposit]
        return self.accountNumber

    def authenticate(self, customerName, customerAccountNumber):
        print()
        if customerAccountNumber in self.bankRecord.keys():
            if self.bankRecord[customerAccountNumber][0] == customerName:
                print("Authentication Successful")
                self.accountNumber = customerAccountNumber
                print()
                return 1
            else:
                print("Authentication Failed")
                print()
                return 0
        else:
            print("Authentication Failed")
            print()
            return 0

    def withdrawMoney(self, customerAccountNumber):
        while True:
            try:
                withdrawlAmount = int(input('Enter the amount you want to withdraw: '))
                if withdrawlAmount > 0:
                    break
                else:
                    print("Amount can't be negative, try again")
            except:
                print("Amount must be a number, try again")
        availableAmount = int(self.bankRecord[customerAccountNumber][1])
        if withdrawlAmount > availableAmount:
            print('Withdrawl amount is more than available balance.')
            print('Available Balance is ', availableAmount)
            return 'y','z'
        else:
            remainingAmount = availableAmount - withdrawlAmount
            self.bankRecord[customerAccountNumber][1] = remainingAmount
            print('Withdrawl Successful.')
            remainingAmount = self.bankRecord[customerAccountNumber][1]
            return availableAmount, remainingAmount

    def depositMoney(self, customerAccountNumber):
        while True:
            try:
                depositedAmount = int(input('Enter the amount you want to deposit: '))
                if depositedAmount > 0:
                    break
                else:
                    print("Amount can't be negative, try again")
            except:
                print("Amount must be a number, try again")
        alreadyAmount = int(self.bankRecord[customerAccountNumber][1])
        updatedBalance = alreadyAmount + depositedAmount
        self.bankRecord[customerAccountNumber][1] = updatedBalance
        updatedBalance = int(self.bankRecord[customerAccountNumber][1])
        return alreadyAmount, updatedBalance

    def displayBalance(self, customerAccountNumber):
        availableBalance = self.bankRecord[customerAccountNumber][1]
        return availableBalance

account = BankAccount()
while True:
    print('**********************************************************')
    print('Welcome to Python3 Bank!!!')
    print()
    print("Enter 1 to create a new bank account")
    print("Enter 2 to access an existing bank account")
    print("Enter q to quit")
    print()
    choiceFirst = input('Enter your choice: ')
    print()
    if choiceFirst is '1':
        name = input('Enter your Full Name: ')
        while True:
            try:
                initialDeposit = int(input('Enter your Initial Deposit: '))
                if initialDeposit > 0:
                    break
                else:
                    print("Amount can't be negative, try again")
            except:
                print("Amount must be a number, try again")
        accountNumber = account.createNewAccount(name, initialDeposit)
        print('Your Account Number is : ', accountNumber)
    elif choiceFirst is '2':
        customerName = input('Enter your Full Name: ')
        while True:
            try:
                customerAccountNumber = int(input('Enter your 5 digits account number: '))
                if customerAccountNumber > 0:
                    break
                else:
                    print("Amount can't be negative, try again")
            except:
                print("Amount must be a number, try again")
        status = account.authenticate(customerName, customerAccountNumber)
        print()
        if status is 1:
            while True:
                print('Enter 3 to withdraw money')
                print('Enter 4 to deposit money')
                print('Enter 5 to display available balance')
                print('Enter 6 to go back to previous menu')
                print()
                choiceSecond = input('Enter your choice: ')
                print()
                if choiceSecond is '3':
                    availableAmount, remainingAmount = account.withdrawMoney(customerAccountNumber)
                    if availableAmount == 'y' or remainingAmount == 'z':
                        continue
                    else:
                        print('Previous Account Balance: ', availableAmount)
                        print('Current Account Balance: ', remainingAmount)
                        print()
                elif choiceSecond is '4':
                    alreadyAmount, updatedBalance = account.depositMoney(customerAccountNumber)
                    print('Previous Account Balance: ', alreadyAmount)
                    print('New Account Balance: ', updatedBalance)
                    print()
                elif choiceSecond is '5':
                    availableBalance= account.displayBalance(customerAccountNumber)
                    print('Current Account Balance: ', availableBalance)
                    print()
                elif choiceSecond is '6':
                    break
                else:
                    print('Invalid Entry')
                    print()
    elif choiceFirst is 'q':
        quit()
    else:
        print('Invalid Entry')
        print()
