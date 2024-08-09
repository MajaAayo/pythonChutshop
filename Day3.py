students = {}

for i in range(1):
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    address = input("Enter address: ")
    email = input("Enter an email: ")
    phone = input("Enter  contact details: ")
    students[roll_no] = {"Name": name, "address": address, "email": email, "phone": phone}
    
    

print(students)

# Contact details

def contact( name, phone, email):
    contact[name]={'phone':phone, 'email':email}
    return contact()
        
newContact={}
newContact= contact('Kushal Bhandari', '9824995555', 'kushalbhandari10@gmail')
newContact= contact('Maljeet Mama', '982900000', 'maljeet40@gmail')

print (contact)