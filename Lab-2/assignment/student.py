
class Student:
	def __init__(self,name,age,marks):
		self.name = name
		self.age = age
		self.marks = marks

s1 = Student("aaa",20,[70,76,73])
s2 = Student("bbb",20,[77,73,76])

def display(s):
	print("Name is ",s.name)
	print("Age is ",s.age)
	for i in s.marks:
		print("Marks ",i)
def accept(s):
	s.name = input("Enter name")
	s.age = input("Enter the age")
	s.marks = input("Enter marks of 3 subjects")
	
	

display(s1)
print("\n")
display(s2)

accept(s2)
display(s2)
