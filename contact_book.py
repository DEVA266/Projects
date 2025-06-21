# This program is used to store search and delete the contact details
import pandas as pd

contactBook = open("contact_details.csv","a")
# FIle pointer name

Contact_Details = pd.read_csv("contact_details.csv")
# The data Frame that hold the file pointer

def adding_contact(): 
    print("\n adding contact \n".upper())
    try : 
        contatct_name = input("Enter the contact name : ")
        contact_number = int(input("Enter the contact number : "))
        contact_email = input("Enter the email address : ")
        email_username = contact_email[0:contact_email.index("@")]
        domain_name = contact_email[contact_email.index("@")+1:]
    except:
        print("\n You entered a wrong information \nplease enter it correctly".upper())
    else : 
        contactBook.write(f"{contatct_name},{contact_number},{contact_email},{email_username},{domain_name}\n")

        
def search_contact():
    print("\n Searchiing contact \n ".upper())
    print("Select from below options : ")
    print("1.Search by Name")
    print("2.Search by Number")
    print("3.Search by Email")
    print("4.Search by Username")
    print("5.Go Back")

    try :
        choice = int(input("Enter your choice : "))
    except:
        print("Invalid Input !")
        return
    
    else :
        try :
            if(choice==1):
                searchingName = input("Enter the name :")
                result = Contact_Details[Contact_Details["Name"]==searchingName]
                if(result.empty):
                    print("No Contacts are Found ")
                    print("1.Search again ")
                    print("2.Exit")
                    try : 
                        secondaryOption = int(input("Enter an Option : "))
                    except:
                        print("Invalid Input !")
                        return
                    else:
                        if(secondaryOption == 1):
                            search_contact()
                            return
                        elif(secondaryOption == 2):
                            return
                        else :
                            print("You Entered an Wrong option !")
                            print("Returning to the Previous Menu")
                            return
                        
                else : 
                    print("\n The Results are : ")
                    print("------------------------------------")
                    print(f"NAME          : {result.iloc[0,0]}")
                    print(f"Mobile Number : {result.iloc[0,1]}")
                    print(f"Email Address : {result.iloc[0,2]}")
                    print("------------------------------------")
                    del result
                    return 
                

            elif(choice==2):

                searchingNumber = int(input("Enter the number : "))
                result = Contact_Details[Contact_Details["Mobile Number"]==searchingNumber]

                if(result.empty):
                    print("No Contacts are Found ")
                    print("1.Search again ")
                    print("2.Exit")

                    try : 
                        secondaryOption = int(input("Enter an Option : "))
                    except:
                        print("Invalid Input !")
                        return
                    
                    else:
                        if(secondaryOption == 1):
                            search_contact()
                            return
                        elif(secondaryOption == 2):
                            return
                        else :
                            print("You Entered an Wrong option !")
                            print("Returning to the Previous Menu")
                            return
                        
                else :
                    print("\n The Results are : ")
                    print("------------------------------------")
                    print(f"NAME          : {result.iloc[0,0]}")
                    print(f"Mobile Number : {result.iloc[0,1]}")
                    print(f"Email Address : {result.iloc[0,2]}")
                    print("------------------------------------")
                    del result
                    return 

            elif (choice == 3):
                searchingEmail = input("Enter the email : ")
                result = Contact_Details[Contact_Details["Email Address"]==searchingEmail]
                if(result.empty):
                    print("No Contacts are Found ")
                    print("1.Search again ")
                    print("2.Exit")

                    try : 
                        secondaryOption = int(input("Enter an Option : "))
                    except:
                        print("Invalid Input !")
                        return
                    
                    else:
                        if(secondaryOption == 1):
                            search_contact()
                            return
                        elif(secondaryOption == 2):
                            return
                        else :
                            print("You Entered an Wrong option !")
                            print("Returning to the Previous Menu")
                            return
                        
                else :
                    print("\n The Results are : ")
                    print("------------------------------------")
                    print(f"NAME          : {result.iloc[0,0]}")
                    print(f"Mobile Number : {result.iloc[0,1]}")
                    print(f"Email Address : {result.iloc[0,2]}")
                    print("------------------------------------")
                    del result
                    return 

            elif (choice == 4):
                searchingUsername = input("Enter the username : ")
                result = Contact_Details[Contact_Details["Email Username"]==searchingUsername]
                if(result.empty):
                    print("No Contacts are Found ")
                    print("1.Search again ")
                    print("2.Exit")

                    try : 
                        secondaryOption = int(input("Enter an Option : "))
                    except:
                        print("Invalid Input !")
                        return
                    
                    else:
                        if(secondaryOption == 1):
                            search_contact()
                            return
                        elif(secondaryOption == 2):
                            return
                        else :
                            print("You Entered an Wrong option !")
                            print("Returning to the Previous Menu")
                            return
                        
                else :
                    print("\n The Results are : ")
                    print("------------------------------------")
                    print(f"NAME          : {result.iloc[0,0]}")
                    print(f"Mobile Number : {result.iloc[0,1]}")
                    print(f"Email Address : {result.iloc[0,2]}")
                    print("------------------------------------")
                    del result
                    return 
                
            elif(choice==5):
                print("Going Back to the Previous Menu \n")
                return
            else :
                print("Invalid Choice !")
                return
        except :
            print("\nInvalid Information \n")
            return

def delete_contact():
    pass

def viewContact():
    print(Contact_Details.head())


while True : 
    print("Welcome User 🙏".upper())
    print("1.Add a new contact")
    print("2.Search in contact")
    print("3.Delete a contact")
    print("4.View contacts")
    print("5.Exit")

    try :
        option = int(input("Choose any one in the option : "))
    except :
        print("\n Please enter a Correct input ! ")
    else : 
        if (option == 1):
            adding_contact()
        elif(option==2):
            search_contact()
        elif(option == 3):
            delete_contact()
        elif(option == 4):
            viewContact()
        elif(option == 5):
            break
        else : 
            print(" \n Please enter an valid option !")



