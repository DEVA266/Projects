# This program is used to store search and delete the contact details

def adding_contact(): 
    remaining_details = []
    print("adding contact".upper())
    try : 
        contatct_name = input("Enter the contact name : ").capitalize()
        contact_number = int(input("Enter the contact number : "))
    except:
        print("You entered a wrong information \nplease enter it correctly".upper())
    else : 
        pass




def search_contact():
    pass

def delete_contact():
    pass


contact_details = {}

while True : 
    print("Welcome User 🙏".upper())
    print("1.Add a new contact")
    print("2.Search in contact")
    print("3.Delete a contact")
    print("4.Exit")

    try :
        option = int(input("Choose any one in the option : "))
    except :
        print("Please enter a Correct input ! ")
    else : 
        if (option == 1):
            adding_contact()
        elif(option==2):
            search_contact()
        elif(option == 3):
            delete_contact()
        elif(option == 4):
            break
        else : 
            print("Please enter an valid option !")



