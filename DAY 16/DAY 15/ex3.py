class student:
    def __init__(self,name,marks):

        self.name = name
        self.grade = self.calculate_grade(marks)
    def calculate_grade(self, marks):
        if marks >= 90:
            return "pass"
        elif marks <= 30:
            return "fail"

print(student("enter name : ",int(input("enter marks : "))).grade)