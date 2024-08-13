class Students:
    def __init__(self, student_name, Roll_no, Grade):
        self.student_name = student_name
        self.Roll_no = int(Roll_no)
        self.Grade = Grade

    def student_info(self):
        print(f"Student Name: {self.student_name}")
        print(f"Roll No: {self.Roll_no}")
        print(f"Grade: {self.Grade}")
    def change_RollNo(self,new_Roll_No):
        print(f"change Roll No {self.Roll_no} to {new_Roll_No}")
        self.Roll_no = int(new_Roll_No)

stu1=Students("Ronak", 21, "A")
#print(stu1.student_info())

stu1.change_RollNo(18)
print(stu1.student_info())