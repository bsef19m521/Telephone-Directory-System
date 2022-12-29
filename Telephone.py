class Telephone_directory:
    def __init__(self):
        def user_menu(self):
            self.user_choice=int(input(""" 
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
            if self.user_choice==1:
                add_record(self)

            if self.user_choice==2:
                view_record(self)

            if self.user_choice == 3:
                update_record(self)

            if self.user_choice==4:
                delete_record(self)

            if self.user_choice==5:
                block_record(self)

            if self.user_choice ==6:
                unblock_record(self)

            if self.user_choice==7:
                searchRecord_Alpha(self)

            if self.user_choice==8:
                searchRecord_blood(self)

            if self.user_choice==9:
                searchRecord_city(self)

        def add_record(self):
            while True:
                self.user_input = int(input("""
                1. Enter Your Name : \n
                2. Enter your age : \n 
                3. Enter your phone number : \n 
                4. Enter your City Name: \n
                5. Enter your Blood Group :\n 
                6. Enter to exit your program.\n"""))
                if self.user_input == 6 :
                    break

        def view_record(self):
            while True:
                self.user_input = int(input("Please enter user's phone number to view Record : "))
                self.number = 35637434
                self.name = "Ehtisham"
                self.age = 21
                self.blood_group = 'O+'
                self.city = 'Okara'
                print(f"""User with {self.number} has following details/records : 
                          User's Name : {self.name}
                          User's Age : {self.age}
                          User's Blood Group : {self.blood_group} 
                          User's City : {self.city} """)
                user_menu(self)
                

        def update_record(self):
            self.list1 = [ ] 
            self.user_input = int(input("Please Enter user Phone Number: "))
            if self.user_input in self.list1:
                i = 1
                while i<2:
                    self.name = input("Enter your name : ")
                    self.age = input("Enter your age : ")
                    i = i+1
            else:
                print(f"User with {self.user_input} does not exit!")
                user_menu(self)
            
                
        def delete_record(self):
            self.list1 = [ ] 
            self.user_input = int(input("Please Enter user Phone Number: "))
            if self.user_input in self.list1:
                print(f"User with {self.user_input} deleted successfully!")
            else:
                print(f"User with {self.user_input} does not exit!") 
            user_menu(self)               
                
        
        def block_record(self):
            self.list1 = [ ] 
            self.user_input = int(input("Please Enter user Phone Number: "))
            if self.user_input in self.list1:
                print(f"User with {self.user_input} blocked successfully!")
            else:
                print(f"User with {self.user_input} does not exit!") 
            user_menu(self) 

                
        def unblock_record(self):
            self.blocked = [ ] 
            self.user_input = int(input("Please Enter user Phone Number: "))
            if self.user_input in self.blocked:
                print(f"User with {self.user_input} unblocked successfully!")
            else:
                print(f"User with {self.user_input} does not exit in blocked list!") 
            user_menu(self) 

        def searchRecord_Alpha(self):
            self.list1 = ['Ehtisham','Ali','Ayesha','Dua','Adeen']
            self.user_input = input("Please a Alphabet: ")
            for i in self.list1:
                if i.startswith(self.user_input):
                    print(i)
            user_menu(self)

        
        def searchRecord_city(self):
            self.city = ['Ehtisham','Ali','Ayesha','Dua','Adeen']
            self.user_input = input("Please a Alphabet: ")
            for i in self.city:
                if i == self.user_input:
                    print(i)
            user_menu(self)

        def searchRecord_blood(self):
            self.blood = ['Ehtisham','Ali','Ayesha','Dua','Adeen']
            self.user_input = input("Please a Alphabet: ")
            for i in self.blood:
                if i == self.user_input:
                    print(i)
            user_menu(self)

        while True:
                self.main_choice = int(input("""
                1.Enter to login as a User : \n
                2.Enter to exit your porgram. \n"""))

                if self.main_choice==1:
                    user_menu(self)
                if self.main_choice==2:
                    break
obj=Telephone_directory()