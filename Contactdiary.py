class contact:
    def file_input(self):
        print("Enter the details")
        self.name=input("Enter the name ")
        self.number=input("Enter the contact number")
        self.email=input("Enter the email id of the person,press '0' to skip")
        if(self.email=='0'):
            self.email="skipped"
        self.birthday=input("Enter the birthday with slashes or without spaces,Press 0 to skip")
        if(self.birthday=='0'):
            self.birthday="skipped"
        print("Noted")
        with open("file.txt",'a') as f:
            f.write(self.number)
            f.write(" ")
            f.write(self.birthday)
            f.write(" ")
            f.write(self.email)
            f.write(" ")
            f.write(self.name)
            f.write("\n")
    def file_output(self):
        with open("file.txt",'r') as f:
            lst1=[]
            for line in f:
                lst2=[]
                for word in line.split():
                    lst2.append(word)
                lst1.append(lst2)
        for i in lst1:
            print("Name: ",end="")
            for j in list(range(3,len(i))):
                print(i[j],end=" ")
            else:
                print("")
            print("Mobile number: ",i[0])
            print("Date of birth: ",i[1])
            print("Email: ",i[2])
            print("")

print("Welcome user")
print("select the options")
print("1.Add a new contact")
print("2.See all the contacts")
option=int(input())
if(option==1):
    contact_var=contact()
    contact_var.file_input()
elif(option==2):
    print("")
    contact_var=contact()
    contact_var.file_output()
else:
    print("Invalid option")