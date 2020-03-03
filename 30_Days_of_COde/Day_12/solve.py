class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #   
    def calculate(self):
        ave = sum(self.scores) // len(self.scores)

        print("Name: {}, {}".format(self.firstName,self.lastName))
        print("ID: {}".format(self.idNumber))
        print("Grade: {}")

line = input().split()