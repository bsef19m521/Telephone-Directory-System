#### Details Description
# 1. User 
#    Add, update, view, delete, block, unblock, search by [alphabets, city, blood group],
# 	Add(First Name, Last Name, Age, Phone Number, city, blood group, DOB, )
# 2. Admin
# 3. Exit
# We can to store these results into file .

# {"User1 ":{"Name":[],
# "Age":[],
# "Phone Number":[],
# "City":[],
# "Blood Group":[],
# "DoB":[],}

# "User2" : {"Name":[],}}

Main_dict = dict()

def Telephone_Directory():
	while True:
		user_dict = dict()
		phone = ""
		user_input = int(input("""
			1. Enter Your Name : \n
			2. Enter your age : \n 
			3. Enter your phone number : \n 
			4. Enter your City Name: \n
			5. Enter your Blood Group :\n 
			6. Enter to exit your program.\n"""))
		if user_input == 1:
			name = input("Enter your name : ")
			user_dict["name"] = name
			print("Your name is : ", name)
		
		if  user_input == 2:
			age = input("Enter your age : ")
			user_dict['age'] = age
			print("Your age is : ", age)

		if user_input == 3:
			phone = input("Enter your phone number : ")
			user_dict['phone'] = phone
			print("Your phone number is : ", phone)

		if user_input == 4:
			city = input("Enter your city name : ")
			user_dict['city'] = city
			print("Your city name is : ", city)

		if user_input == 5:
			blood_group = input("Enter your blood group name : ")
			user_dict['blood_group'] = blood_group
			print("Your blood group name is : ", blood_group)

		if user_input ==6:
			Main_dict[phone] = user_dict
			break



Telephone_Directory()
# print("User Dictionary is :", user_dict)
print("Main Dictionary is :", Main_dict)


