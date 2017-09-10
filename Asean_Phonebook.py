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
	students = []
	validMainMenu = ['1', '2', '3', '4']
	validStudSex = ['M', 'm', 'F', 'f']
	validStudCodeCountry = ['60', '62', '63', '65', '66']
	validIsAnotherEntry = ['N', 'n', 'Y', 'y']
	validNo = ['N', 'n']

	def run(self):
		self.handleShowMenuMain();

	def handleShowMenuMain(self):
		selected = self.showMenuMain()
		if selected == 1: self.storeStudent()
		elif selected == 2: self.editStudent()
		elif selected == 3: self.searchStudent()
		else: self.exit()

	def showMenuMain(self):
		response = 0
		while True:
			if str(response) in self.validMainMenu: break
			print("\n")
			print("[1] Store to ASEAN phonebook")
			print("[2] Edit Entry in ASEAN phonebook") 
			print("[3] Search ASEAN phonebook by country")
			print("[4] Exit");
			response = raw_input("Choose a number from the list: ")
		return int(response)

	def storeStudent(self):
		while True:
			print("\n")
			studNumber = raw_input("Enter a student number: ")
			studNameSur = raw_input("Enter surname: ")
			studNameFirst = raw_input("Enter first name: ")
			studOccupation = raw_input("Enter occupation: ")
			while True:
				studSex = raw_input("M for male, F for Female : ")
				if studSex in self.validStudSex: break
				else: self.inputInvalid()
			while True:
				studCodeCountry = raw_input("Enter country code: ")
				if studCodeCountry in self.validStudCodeCountry: break
				else: self.inputInvalid()
			studCodeArea = raw_input("Enter area code: ")
			studNumber = raw_input("Enter number: ")
			student = Student(studNumber, studNameSur, studNameFirst, studOccupation, studSex, studCodeCountry, studCodeArea, studNumber)
			self.students.append(student)
			while True:
				isAnotherEntry = raw_input("Do you want to enter another entry [Y/N]?: ")
				if isAnotherEntry in self.validIsAnotherEntry: break
				else: self.inputInvalid()
			if isAnotherEntry in self.validNo: break
		self.handleShowMenuMain();

	def editStudent(self):
		print("\n")
		response = raw_input("Enter student number: ")
		print("Here is the existing information about 2004-56:")
		print("Sukarno Lee is a Doctor. His number is 63-2-4567890")
		print("Which of the following information do you wish to change?")
		print("[1] Student number [2] Surname [3] Gender [4] Occupation")
		print("[5] Country code [6] Area code [7] Phone number")
		print("[8] None - Go back to main menu")
		response = raw_input("Enter choice: ")
		response = raw_input("Enter new student number: ")
		self.handleShowMenuMain();

	def searchStudent(self):
		print("\n")
		print("From which country:")
		print("[1] Philippines [2] Thailand [3] Singapore [4] Indonesia")
		print("[5] Malaysia [6] ALL [0] No More")
		response = raw_input("Enter choice 1: ")
		self.handleShowMenuMain();

	def inputInvalid(self):
		print("Invalid input!")

	def exit(self):
		print("\nBye!")

aseanPhonebook = Phonebook()
aseanPhonebook.run()

