#!/C:/Users/Lloyd/Desktop/Asean_Phonebook
# Filename: Asean_Phonanebook.py

# Class Scheme for the phonebook record
class Student:
	# Declase paramenters for one record
	studentNumber = ""
	nameSur = ""
	nameFirst = ""
	occupation = ""
	gender = ""
	codeCountry = ""
	codeArea = ""
	number = ""

	# Initialize a record of student
	def __init__(self, studentNumber, nameSur, nameFirst, occupation, gender, codeCountry, codeArea, number):
		self.studentNumber = studentNumber
		self.nameSur = nameSur
		self.nameFirst = nameFirst
		self.occupation = occupation
		self.gender = gender
		self.codeCountry = codeCountry
		self.codeArea = codeArea
		self.number = number

class Phonebook:
	name = ""

	def __init__(self, name):
		self.name = name

	def showMenuMain(self):
		response = 0
		while self.isSelectedMenuInvalid(response) :
			print("\n")
			print("[1] Store ASEAN phonebook")
			print("[2] Edit Entry in ASEAN phonebook") 
			print("[3] Search ASEAN phonebook by country")
			print("[4] Exit");
			response = raw_input("Choose a number from the list: ")
		return response

	def isSelectedMenuInvalid(self, entry):
		if int(entry) in [1, 2, 3, 4]:
			return False
		else:
			return True

	def storeStudent(self):
		response = raw_input("Enter a student number: ")
		response = raw_input("Enter surname: ")
		response = raw_input("Enter first name: ")
		response = raw_input("Enter occupation: ")
		response = raw_input("M for male, F for Female : ")
		response = raw_input("Enter country code: ")
		response = raw_input("Enter area code: ")
		response = raw_input("Enter number: ")
		response = raw_input("Do you want to enter another entry [Y/N]? ")

	def editStudent(self):
		response = raw_input("Enter student number: ")
		print("Here is the existing information about 2004-56:")
		print("Sukarno Lee is a Doctor. His number is 63-2-4567890")
		print("Which of the fllowing information do you wish to change?")
		print("[1] Student number [2] Surname [3] Gender [4] Occupation")
		print("[5] Country code [6] Area code [7] Phone number")
		print("[8] None - Go back to main menu")
		response = raw_input("Enter choice: ")
		response = raw_input("Enter new student number: ")

	def searchStudent(self):
		print("From which country:")
		print("[1] Philippines [2] Thailand [3] Singapore [4] Indonesia")
		print("[5] Malaysia [6] ALL [0] No More")
		response = raw_input("Enter choice 1: ")

	def exit(self):
		pass

aseanPhonebook = Phonebook("Name")
aseanPhonebook.showMenuMain()
