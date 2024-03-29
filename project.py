import csv
import json
import os


class Personnel:
    positions = ["employee", "admin"]
    departments = ["Accounting", "Admin", "Design", "HR", "IT", "Marketing", "ProductManager", "QualityAssurance", "SoftwareDev" ]

    def __init__(self, id_number=None, name=None, position=None, department=None, wage=0):
        self._id_number = id_number
        self._name = name
        self._position = position
        self._department = department
        self._wage = wage

    def __str__(self):
        return f"{self.id_number}, {self.name}, {self.position}, {self.department}, {self.wage}"

    def id_number(self):
        return self.id_number

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, wage):
        self._wage = wage

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not name.isalpha() and name is not None:
            print("You have entered an invalid name")
        else:
            self._name = name


def main():
    db_file = "personnel_database.csv"
    id_file = "id_count.json"

    if not os.path.exists(db_file) or os.path.getsize(db_file) == 0:
        with open(db_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Position", "Department", "Wage"])
            writer.writeheader()

    if not os.path.exists(id_file) or os.path.getsize(db_file) == 0:
        with open(id_file, "w") as j:
            id_dict = {"current_id": 0}
            json.dump(id_dict, j, indent=4)

    while True:
        action = (input("Please enter the action you want to conduct: ")).lower()

        if action == "add":
            add_personnel(id_file)
        elif action == "find":
            find_personnel()
        elif action == "remove":
            remove_personnel()
        elif action == "update":
            update_personnel()


def add_personnel(id_file):
    with open(id_file, "r") as j:
        data = json.load(j)
        last_id_number = data["current_id"]

    id_number = last_id_number + 1
    person = Personnel()

    while True:
        name = input("Please enter the name of the personnel: ")
        person.name = name
        if person.name == name:
            break

    position = (input("Please enter the position of the personnel: ")).lower()

    if position not in Personnel.positions:
        print("You have entered and invalid position, please try again.")
        return

    person.position = position

    if position == "admin":
        person.department = "Admin"
    else:
        department = input("Please enter the department of the personnel: ")
        if department not in Personnel.departments:
            print("You have entered an invalid department, please try again")
            return
        person.department = department

    while True:
        wage = int(input("Please enter the wage of the personnel: "))

        if wage <= 0:
            print("You have entered an invalid Wage. Please try again.")
            return 0

        person.wage = wage
        if int(person.wage) == int(wage):
            break
    person.id_number = id_number

    with open("personnel_database.csv", "r") as db:
        reader = csv.DictReader(db,fieldnames=["ID", "Name", "Position", "Department", "Wage"])
        database = list(reader)
        for row in database:
            if row["Name"] == person.name and row["Position"] == person.position \
                    and row["Department"] == person.department and int(row["Wage"]) == person.wage:
                print("The employee already exists in the Database")
                return

    with open("personnel_database.csv", "a") as db:
        writer = csv.DictWriter(db, fieldnames=["ID", "Name", "Position", "Department", "Wage"])
        person_dict = {"ID": person.id_number, "Name": person.name, "Position": person.position,
                       "Department": person.department, "Wage": person.wage}

        writer.writerow(person_dict)

    with open("id_count.json", "w") as j:
        id_dict = {"current_id": id_number}
        json.dump(id_dict, j, indent=4)


def find_personnel():
    ...

def remove_personnel():
    ...


def update_personnel():
    ...


if __name__ == "__main__":
    main()

# personnel registration program
# create general class of staff
# create classes of admin and employees
# ask for input of personnel type
# according to input, run function
# create object using function
# save the personnel into a csv file
# if the object already exists, ask if they want to update values
# update the values
