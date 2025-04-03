
# 2. Add constructor in the above class to initialize student details of n students and implement following methods:
# a)	Display() student details
# b)	Find Marks_percentage() of each student
# c)	 Display result() [Note: if marks in each subject >40% than Pass else Fail]

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks:", self.marks)

    def find_marks_percentage(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / (len(self.marks) * 100)) * 100
        return percentage

    def display_result(self):
        if all(mark > 40 for mark in self.marks):
            result = "Pass"
        else:
            result = "Fail"
        return result
def main():
    students = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter name of student {}: ".format(i + 1))
        sap_id = input("Enter SAP ID of student {}: ".format(i + 1))
        marks = list(map(int, input("Enter marks (phy, chem, maths) of student {}: ".format(i + 1)).split()))
        student = Student(name, sap_id, marks)
        students.append(student)

    print("\nDetails of all students:")
    for student in students:
        student.display()
        print("Marks Percentage:", student.find_marks_percentage())
        print("Result:", student.display_result())
        print()
main()
