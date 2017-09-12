# Filename: Asean_Phonanebook.py

# Class Phonebook record

class Phonebook:
	students = []
	searchCountryList = ["Philippines", "Thailand", "Singapore", "Indonesia", "Malaysia"]
	editStudInfoList = ["Student number", "Surname", "Gender",  "Occupation" , "Country code", "Area code", "Phone number"]
	validMenuMain = ['1', '2', '3', '4']
	validMenuCountry = ['1', '2', '3', '4', '5', '6', '0']
	validMenuStudEdit = ['1', '2', '3', '4', '5', '6', '7', '8']
	validStudSex = ['M', 'm', 'F', 'f']
	validStudCodeCountry = ['60', '62', '63', '65', '66']
	validIsAnotherEntry = ['N', 'n', 'Y', 'y']
	validNo = ['N', 'n']

	def run(self):
		self.handleShowMenuMain()

	def handleShowMenuMain(self):
		selected = self.showMenuMain()
		if selected == 1: self.storeStudent()
		elif selected == 2: self.editStudent()
		elif selected == 3: self.searchStudent()
		elif selected == 4: self.exit()

	def showMenuMain(self):
		response = 0
		while True:
			if str(response) in self.validMenuMain: break
			print("\n")
			print("[1] Store to ASEAN phonebook")
			print("[2] Edit entry in ASEAN phonebook") 
			print("[3] Search ASEAN phonebook by country")
			print("[4] Exit");
			response = raw_input("Choose a number from the list: ")
		return int(response)

	def storeStudent(self):
			while True:
				print("\n")
				studNumber = ""
				while True:
					valid = True
					studNumber = str(raw_input("Enter a student number: "))
					for student in self.students:
						if student[0] == studNumber:
							valid = False
							break
					if studNumber == "":
						valid = False
					if valid: break
					self.inputInvalid()
				while True:
					studNameSur = str(raw_input("Enter surname: "))
					if studNameSur != "": break
					self.inputInvalid()
				while True:
					studNameFirst = str(raw_input("Enter first name: "))
					if studNameFirst != "": break
					self.inputInvalid()
				while True:
					studOccupation = raw_input("Enter occupation: ")
					if studOccupation != "": break
					self.inputInvalid()
				while True:
					studSex = str(raw_input("M for male, F for Female : ")).upper()
					if studSex in self.validStudSex: break
					self.inputInvalid()
				while True:
					studCodeCountry = str(raw_input("Enter country code: "))
					if studCodeCountry in self.validStudCodeCountry: break
					self.inputInvalid()
				while True:
					studCodeArea = str(raw_input("Enter area code: "))
					if studCodeArea.isdigit(): break
					self.inputInvalid()
				while True:
					studCellNumber = str(raw_input("Enter number: "))
					if studCellNumber.isdigit(): break
					self.inputInvalid()
				student = [studNumber, studNameSur, studNameFirst, studOccupation, studSex, studCodeCountry, studCodeArea, studCellNumber]
				self.students.append(student)
				response = ""
				while True:
					isAnotherEntry = str(raw_input("Do you want to enter another entry [Y/N]?: "))
					if isAnotherEntry in self.validIsAnotherEntry:
						response = isAnotherEntry
						break
					else: self.inputInvalid()
				if response in self.validNo: break
			self.handleShowMenuMain()

	def editStudent(self):
		print("\n")
		response = str(raw_input("Enter student number: "))
		editStudInfo  = []
		record = 0
		valid = False
		for student in self.students:
			if student[0] == response:
				valid = True
				editStudInfo = student
				break
			else: record = record + 1
		if valid:
			while True:
				sex = ""
				if editStudInfo[4] == 'M':
					sex = 'His'
				elif editStudInfo[4] == 'F':
					sex = 'Her'
				print(" ")
				print("Here is the existing information about " + editStudInfo[0] +":")
				print( editStudInfo[2]+ " " + editStudInfo[1] + " is a " + editStudInfo[3] + ". " + sex + " number is " + editStudInfo[5] + "-" + editStudInfo[6] + "-" + editStudInfo[7] )
				print("Which of the following information do you wish to change?")
				print("[1] Student number [2] Surname [3] Gender [4] Occupation")
				print("[5] Country code [6] Area code [7] Phone number")
				print("[8] None - Go back to main menu")
				while True:
					editInfo = str(raw_input("Enter choice: "))
					if editInfo in self.validMenuStudEdit: break
					else:
						self.inputInvalid()
				if editInfo != '8':
					msg = "Enter new " + (self.editStudInfoList[int(editInfo)-1]).lower() + ": "
					value = str(raw_input(msg))
					if editInfo == '1':
						while True:
							valid = True
							for student in self.students:
								if student[0] == value:
									valid = False
									break
							if value == "":
								valid = False
							if valid: break
							self.inputInvalid()
							value = str(raw_input(msg))
						editStudInfo[0] = value
						self.students[record] = editStudInfo
					elif editInfo == '2':
						while True:
							if value == "":
								self.inputInvalid()
								value = str(raw_input(msg))
							else: break
						editStudInfo[1] = value
						self.students[record] = editStudInfo
					elif editInfo == '3':
						while True:
							if value in self.validStudSex: break
							self.inputInvalid()
							value = str(raw_input(msg))
						editStudInfo[4] = value.upper()
						self.students[record] = editStudInfo
					elif editInfo == '4':
						while True:
							if value == "":
								self.inputInvalid()
								value = str(raw_input(msg))
							else: break
						editStudInfo[3] = value
						self.students[record] = editStudInfo
					elif editInfo == '5':
						while True:
							if value in self.validStudCodeCountry: break
							self.inputInvalid()
							value = str(raw_input(msg))
						editStudInfo[5] = value
						self.students[record] = editStudInfo
					elif editInfo == '6':
						while True:
							if value.isdigit(): break
							self.inputInvalid()
							value = str(raw_input(msg))
						editStudInfo[6] = value
						self.students[record] = editStudInfo
					elif editInfo == '7':
						while True:
							if value.isdigit(): break
							self.inputInvalid()
							value = str(raw_input(msg))
						editStudInfo[7] = value
						self.students[record] = editStudInfo
				else: break
		else:
			print("Student not found.")
		self.handleShowMenuMain();

	def searchStudent(self):
		countries = []
		print("\n")
		print("From which country:")
		print("[1] Philippines [2] Thailand [3] Singapore [4] Indonesia")
		print("[5] Malaysia [6] ALL [0] No More")
		country = ""
		while True:
			country = raw_input("Enter choice " + str(len(countries) + 1) + ": ")
			if country in self.validMenuCountry:
				if country == '0': break
				elif int(country) in countries:
					print("Already selected")
				elif country == '6':
					countries = [6]
					print("All countries selected")
				elif countries == [6]:
					countries = [int(country)]
					print("All countries deselected")
				else: countries.append(int(country))
			else: self.inputInvalid()
		if countries != []:
			selectedCountries = ""
			if countries == [6]:
				countries = [1, 2, 3, 4, 5]
			for index in range(len(countries)):
				if index == 0:
					selectedCountries = str(self.searchCountryList[int(countries[index]-1)])
				elif index == int(len(countries)-1):
					selectedCountries = selectedCountries + " and " + str(self.searchCountryList[int(countries[index]-1)])
				else:
					selectedCountries = selectedCountries + ", " + str(self.searchCountryList[int(countries[index]-1)])	
			print("Here are the students from " + str(selectedCountries))
			searchCodeCountry = ['63', '66', '65', '62', '60']
			for country in countries:
				for student in self.students:
					if student[5] == searchCodeCountry[int(country)-1]:
						sex = ""
						if student[4] == 'M':
							sex = 'His'
						elif student[4] == 'F':
							sex = 'Her'
						print(student[1] + ", " + student[2] + ", with student number " + student[0] + ", is a " + student[3] + ". " + sex + " phone number is " + student[5] + "-" + student[6] + "-" + student[7])
		else:
			print("No countries selected.")
		self.handleShowMenuMain();

	def inputInvalid(self):
		print("Invalid input!")

	def exit(self):
		print("\nBye!")

aseanPhonebook = Phonebook()
aseanPhonebook.run()