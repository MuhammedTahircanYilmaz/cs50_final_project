import csv

class Personnel:
    positions = ["employee", "admin"]
    departments =  ["HR", "SoftwareDev", "Marketing", "Design", "IT", "QualityAssurance", "ProductManager", "Accounting"]

    def __init__(self, name=None, position=None, department=None, wage=0):
        self.name = name
        self.position = position
        self.department = department
        self.wage = wage
    
    def __str__(self):
        return f"{self.name}, {self.position}, {self.department}, {self.wage}"

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if position not in Personnel.positions and position != None:
            print("You have entered a wrong position, try again")
        else:
            self._position = position


    @property
    def wage(self):
        return self._wage
    
    @wage.setter
    def wage(self, wage):
        if wage < 0:
            raise ValueError
        else:
            self._wage = wage


    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, department):
        if department not in Personnel.departments and department != None:
            print("You have entered an incorrect department. Please try again")
        else: 
            self._department = department


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name.isalpha() and name != None:
            print("You have entered an invalid name")
        else:
            self._name = name


def main():
    while True:
        action = (input("Please enter the action you want to conduct: ")).lower()

        if action == "add":
            add_personnel()
        elif action == "remove":
            remove_personnel()
        elif action == "update":
            update_personnel()


def add_personnel():
    while True:
        name = input("Please enter the name of the personnel: ")
        person = Personnel(name)
        if person.name == name:
            break
    while True:
        position = (input("Please enter the position of the personnel: ")).lower()
        if position == "admin":
            person.position = position
            break 
        else:
            person.position = position
            if person.position == position:
                while True:    
                    department = input("Please enter the department of the personnel: ")
                    person.department = department
                    if person.department == department:
                        break
            break
    while True:
        wage = int(input("Please enter the wage of the personnel: "))
        person.wage = wage
        if person.wage == wage:
            break       
    print (person)
def remove_personnel():
    ...


def update_personnel():
    ...


if __name__ == "__main__":
    main()


# personel registration program
# create general class of staff
# create classes of admin and employees
# ask for input of personel type
# according to input, run function
# create object using function
# save the personel into a csv file
# if the object already exists, ask if they want to update values
# update the values