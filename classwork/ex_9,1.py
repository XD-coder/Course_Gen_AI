#experiment 9.1

# 1.Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by taking inputs from the user and display details of all students.

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks:", self.marks)

def main():
    students = []
    for i in range(3):
        name = input("Enter name of student {}: ".format(i + 1))
        sap_id = input("Enter SAP ID of student {}: ".format(i + 1))
        marks = list(map(int, input("Enter marks (phy, chem, maths) of student {}: ".format(i + 1)).split()))
        student = Student(name, sap_id, marks)
        students.append(student)

    print("\nDetails of all students:")
    for student in students:
        student.display()
        print()
if __name__ == "__main__":
    main()
