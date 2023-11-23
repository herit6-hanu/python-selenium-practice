class Employee:
	def __init__(self, name, age, salary, phn_number, location, work_mode):
		self.name = name
		self.age = age
		self.salary = salary
		self.phn_number = phn_number
		self.location = location
		self.work_mode = work_mode
	
	def print_name(self):
		return f'Name of the employee is {self.name}'
	
	def print_age(self):
		return f'Age of the employee is {self.age}'
	
	def print_salary(self):
		return f'Salary of the employee is {self.salary}'
	
	def print_phn_number(self):
		return f'Phone number of the employee is {self.phn_number}'
	
	def print_location(self):
		return f'Location of the employee is {self.location}'
	
	def print_work_mode(self):
		return f'Work mode of the employee is {self.work_mode}'


emp = Employee(name='Hanumantha Reddy Moola', age=24, salary=47000.00, phn_number=9100412870, location='Hyderabad',
               work_mode='Hybrid mode')
print(emp.print_name())
print(emp.print_age())
print(emp.print_salary())
print(emp.print_phn_number())
print(emp.print_location())
print(emp.print_work_mode())
