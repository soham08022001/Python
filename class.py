class Employess:
    def __init__(self,employee_id, Name, department):
        self.employee_id = employee_id
        self.Name = Name
        self.department = department

    def employee_info(self):
        print(f"employee id is {self.employee_id}")
        print(f"Name is {self.Name}")
        print(f"Department is {self.department}")

    def change_department(self, new_department):
        print(f'changed department from {self.department} to {new_department}')
        self.department = new_department

    def change_id(self, new_id):
        print(f"{self.employee_id} changed to {new_id}")
        self.employee_id = int(new_id)

#Obejects
employee1=Employess(101,'soham','coding')
print(employee1.employee_info())

employee2=Employess(102, "raju", "Test")
print(employee2.employee_info())

# Changed Department
print(employee1.change_department("DevOps"))
print(employee1.employee_info())

# Changed Employee ID
print(employee1.change_id(808))
print(employee1.employee_info())