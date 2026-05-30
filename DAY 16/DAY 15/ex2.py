class employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary
    def calculate_annual_salary(self):
        return self.base_salary * 12
print("annual salary of employee is : ",employee("chaithanya",50000).calculate_annual_salary())