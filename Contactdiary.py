class contact:
    def __init__(self):
        print("Enter the details")
        self.name=input("Enter the name ")
        self.number=input("Enter the contact number")
        self.email=input("Enter the email id of the person,press '0' to skip")
        if(self.email=='0'):
            self.email="skipped"
        self.birthday=input("Enter the birthday with slashes or without spaces,Press 0 to skip")
        if(self.birthday=='0'):
            self.birthday="skipped"
        print("Pani done")

    def show_details(self):
        print(self.name,self.number,self.birthday,self.email)

print("Welcome user")
print("select the options")
print("1.Add a new contact")
print("2.See all the contacts")
option=int(input())
if(option==1):
    contact_var=contact()
    contact_var.show_details()
elif(option==2):
    print("Its still in the development stage")
else:
    print("Invalid option")