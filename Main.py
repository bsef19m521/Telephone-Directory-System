# Telephone Directory Management System
class Telephone_Directory():
	"""docstring for Telephone_Diectory"""

	def __init__(self):
		self.name = "Ehtisham Sadiq"
		self.age = 21
		self.blood_group = "O+"
		def addRecord(self):
			user_choice = int(input("""
			1. Enter to Add your Record : \n
			2. Enter to View Record : \n
			3. Enter to Update your record : \n
			4: Enter to Delete Your Record : \n
			5: Enter to Block your Record : \n
			6: Enter to Unblock your Record : \n
			7: Enter to Search by Alphabets : \n
			8: Enter to Search by Blood Group : \n
			9: Enter to search by City : \n
			10: Enter more records: \n"""))


			if user_choice == 1:
				user_record(self)

			if user_choice==3:
				update_record(self)
			
			if user_choice == 10:
				again(self)

		def user_record(self):
			while True:
				user_input = int(input("""
                1. Enter Your Name : \n
                2. Enter your age : \n 
                3. Enter your phone number : \n 
                4. Enter your City Name: \n
                5. Enter your Blood Group :\n 
                6. Enter to exit your program.\n"""))
				if user_input == 6 :
					break
		def update_record(self):
			while True:
				user_input = int(input("""
                1. Enter Your New Name : \n
                2. Enter your New age : \n 
                3. Enter your New phone number : \n 
                4. Enter your New City Name: \n
                5. Enter your Blood Group :\n 
                6. Enter to exit your program.\n"""))
				if user_input == 6 :
					break
        
		def again(self):
			choice = input("Do you want to enter more record? Please enter y for yes and n for no: ")
			if choice.upper()=='Y':
				addRecord(self)
			elif choice.upper()=='N':
				print("See you later!")
			else:
				addRecord(self)
			print("\t================= Main Menu ======================\t")
			while True:
				main_choice = int(input("""
			1.Enter to login as a User : \n
			2.Enter to exit your porgram. \n"""))

				if main_choice==1:
					addRecord(self)
				if main_choice==2:
					break
# creating object of the class
Object1 = Telephone_Directory()
# Object.addRecord()