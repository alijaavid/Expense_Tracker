import json
from datetime import date, datetime



def load_expenses() : 
    global expenses
    try : 
        with open ("expenses.json" , "r") as file :
            expenses = json.load(file)
    except : 
        expenses = []

def save_expenses() : 
    with open ("expenses.json" , "w") as file : 
        json.dump(expenses , file , indent= 4 )

def add_expense() : 
    amount = int (input("Enter Amount : "))
    category = input("Enter Category : ")
    description = input("Enter Description : ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    expenses.append ({
        "amount" : amount ,
        "description" : description ,
        "datetime" : now ,
        "category" : category
        })
    save_expenses()
    
def show_expenses() :
    for expense in expenses : 
        print ("Amount" , expense["amount"])
        print ("Description =  " , expense["description"])
        print ("Datetime = " , expense["datetime"] )
        print ("Category = " , expense["category"] )
        print("#" * 30)

def edit_expenses() :
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print ("On what basis do you want to edit ?")
    print("1. Amount")        
    print("2. Description")                
    print("3. Category")        
    choice = input("Please Choose One Of Them : ")        
        
    if choice == "1" : 
       a = int (input("Please Enter Your Amount You Want edit : "))        
       found = False        
       for expense in expenses : 
                   if expense["amount"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )
                       new_amount =int( input("Please enter new amount : "))
                       new_description = input("Please enter new description : ")
                       new_category = input("Please enter new category : ")
                       answer = input ("Save Changes (y/n) : ")
                       if answer == "y" : 
                            expense["amount"] = new_amount 
                            expense["description"] = new_description
                            expense["category"] = new_category
                            expense["datetime"] = now
                            save_expenses()
                       
       if not found : 
                   print("Expense Not Found !!!")
                   return
    elif choice == "2" : 
       a = input("Please Enter Your Description You Want edit : ")     
       found = False        
       for expense in expenses : 
                   if expense["description"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )
                       new_amount =int( input("Please enter new amount : "))
                       new_description = input("Please enter new description : ")
                       new_category = input("Please enter new category : ")
                       answer = input ("Save Changes (y/n) : ")
                       if answer == "y" : 
                            expense["amount"] = new_amount 
                            expense["description"] = new_description
                            expense["category"] = new_category
                            expense["datetime"] = now
                            save_expenses()
                       
       if not found : 
                   print("Expense Not Found !!!")
                   return

    elif choice == "3" : 
       a = input("Please Enter Your Category You Want edit : ")     
       found = False        
       for expense in expenses : 
                   if expense["category"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )
                       new_amount =int( input("Please enter new amount : "))
                       new_description = input("Please enter new description : ")
                       new_category = input("Please enter new category : ")
                       answer = input ("Save Changes (y/n) : ")
                       if answer == "y" : 
                            expense["amount"] = new_amount 
                            expense["description"] = new_description
                            expense["category"] = new_category
                            expense["datetime"] = now
                            save_expenses()
                       
       if not found : 
                   print("Expense Not Found !!!")
                   return
    
def search_expenses() :
    print("On what basis do you want to search? ")        
    print("1. Amount")        
    print("2. Description")        
    print("3. Datetime")        
    print("4. Category")        
    choice = input("Please Choose One Of Them : ")        
        
    if choice == "1" : 
       a = int (input("Please Enter Your Amount You Want Search : "))        
       found = False        
       for expense in expenses : 
                   if expense["amount"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )        
       if not found : 
                   print("Expense Not Found !!!")                

    elif choice == "2" : 
               a = (input("Please Enter Your Description You Want Search : "))
               found = False
               for expense in expenses : 
                   if expense["description"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )
               if not found : 
                   print("Expense Not Found !!!")        

    elif choice == "3" : 
               a = (input("Please Enter Your Datetime You Want Search : "))
               found = False
               for expense in expenses : 
                   if expense["datetime"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )
               if not found : 
                   print("Expense Not Found !!!")        

    elif choice == "4" : 
               a = (input("Please Enter Your Category You Want Search : "))
               found = False
               for expense in expenses : 
                   if expense["category"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )
               if not found : 
                   print("Expense Not Found !!!")        

def delete_expenses() : 
    print ("On what basis do you want to delete ?")
    print("1. Amount")        
    print("2. Description")                
    print("3. Category")        
    choice = input("Please Choose One Of Them : ")        
        
    if choice == "1" : 
       a = int (input("Please Enter Your Amount You Want delete : "))        
       found = False        
       for expense in expenses : 
                   if expense["amount"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )
                       answer = input("Are You Sure You Want Delete (y/n) : ")
                       if answer == "y" : 
                           expenses.remove(expense)
                           save_expenses()
                       else :
                            return
                   if not found : 
                        print("Expense Not Found !!!")
                        return


    elif choice == "2" : 
        a = input("Please Enter Your Description You Want delete : ")    
        found = False        
        for expense in expenses : 
                   if expense["description"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )
                       answer = input("Are You Sure You Want Delete (y/n) : ")
                       if answer == "y" : 
                           expenses.remove(expense)
                           save_expenses()
                       else :
                            return
                   if not found : 
                        print("Expense Not Found !!!")
                        return

    elif choice == "3" : 
        a = input("Please Enter Your Category You Want delete : ")    
        found = False        
        for expense in expenses : 
                   if expense["category"] == a :
                       found = True
                       print ("Amount : " , expense["amount"])
                       print ("Description : " , expense["description"])
                       print ("Datetime : " , expense["datetime"])
                       print ("Category : " , expense["category"])
                       print ("#" * 30 )
                       answer = input("Are You Sure You Want Delete (y/n) : ")
                       if answer == "y" : 
                           expenses.remove(expense)
                           save_expenses()
                       else :
                            return
                   if not found : 
                        print("Expense Not Found !!!")
                        return


expenses = []
"""
load_expenses()
"""

while(True) : 
    print ("1. Add expense")
    print ("2. Show expense")
    print ("3. Edit expense")
    print ("4. Search expense")
    print ("5. Delete expense")
    print ("6. Exit")

    choice = input("Please Choose One Of Them : ")
    if choice == "1" : 
        add_expense()
    elif choice == "2" : 
        show_expenses()
    elif choice == "3" : 
        edit_expenses()
    elif choice == "4" : 
        search_expenses()
    elif choice == "5" : 
        delete_expenses()
    elif choice == "6" :
        break

