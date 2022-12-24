# Telephone Directory Management System
class Telephone_Diectory():
	"""docstring for Telephone_Diectory"""
	def __init__(self):

		def addRecord(self):
			self.user_choice = int(input("""
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
			if self.user_choice == 10:
				again(self)

		def again(self):
			self.choice = input("Do you want to enter more record? Please enter y for yes and n for no: ")
			if self.choice.upper()=='Y':
				addRecord(self)
			elif self.choice.upper()=='N':
				print("See you later!")
			else:
				addRecord(self)
		print("\t================= Main Menu ======================\t")

		while True:
			self.main_choice = int(input("""
			1.Enter to login as a User : \n
			2.Enter to exit your porgram. \n"""))

			if self.main_choice==1:
				addRecord(self)
			if self.main_choice==2:
				break
# creating object of the class
Object1 = Telephone_Diectory()