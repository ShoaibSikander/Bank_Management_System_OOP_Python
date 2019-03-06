class Employee:
    name = "Shoaib"
    def __init__(self):
        print("Welcome!!!")
    def changeName(self, Name):
        Employee.name = Name

employee = Employee()
print("Before changing, the name is : ", employee.name)
employee.changeName('Sikander')
print("After changing, the name is : ", employee.name)
