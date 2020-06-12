from admin_functions import *

def manage_books_and_authors(): 
    valid = 0  
    while(valid == 0):
        print('''Books and authors: what would you like to do:
1) Add Book
2) Delete Book
3) Edit Book
4) Add Author
5) Delete Author
6) Update Author
Or Enter to go back to admin menu    
    ''')
        choice = input()
        if choice == '':
            return 
        if(choice.isdecimal() and int(choice) in range(0,7)):
            if choice == '1':        
                add_book()          
            elif choice == '2':
                delete_book()
            elif choice == '3':
                update_book()
            elif choice == '4':
                add_author(0)
            elif choice == '5':
                delete_author()
            elif choice == '6':
                update_author()
        else:
            print('Please enter a valid option: ',end='')
      
def manage_publishers():   
    valid = 0  
    while(valid == 0):
        print('''Publishers: what would you like to do:
1) Add Publishers
2) Delete Publishers
3) Edit Publishers    
Or enter Enter to go back to admin menu    
    ''')
        choice = input()
        if choice == '':
            return  
        elif(choice.isdecimal() and int(choice) in range(0,4)):
            if choice == '1':        
                add_publisher(0)          
            elif choice == '2':
                delete_publisher()
            elif choice == '3':
                update_publisher()          
        else:
            print('Please enter a valid option: ',end='')        


def manage_branches():    
    valid = 0  
    while(valid == 0):
        print('''Branches: what would you like to do:
1) Add Branch
2) Delete Branch
3) Edit Branch    
Or Enter to go back to admin menu    
    ''')
        choice = input()
        if choice == '':
            return   
        if(choice.isdecimal() and int(choice) in range(0,4)):
            if choice == '1':        
                add_branch()          
            elif choice == '2':
                delete_branch()
            elif choice == '3':
                update_branch()           
        else:
            print('Please enter a valid option: ',end='')

def manage_borrowers():
    
    valid = 0  
    while(valid == 0):
        print('''Branches: what would you like to do:
1) Add Borrowers
2) Delete Borrowers
3) Edit Borrowers  
Or Enter to go back to admin menu   
    ''')
        choice = input()
        if choice == '':
            return  
        if(choice.isdecimal() and int(choice) in range(0,4)):
            if choice == '1':        
                add_borrower()          
            elif choice == '2':
                delete_borrower()
            elif choice == '3':
                update_borrower()       
            else:
                print('Please enter a valid option: ',end='')



def admin_menu():    
    valid = 0  
    while(valid == 0):
        print('''Hello Administrator, what would you like to do:
1) Manage Book and Authors
2) Manage Publishers
3) Manage Library Branches
4) Manage Borrowers
5) Override a Due Date for a Book Loan
Or Enter to go back to main menu    
    ''')
        choice = input()
        if choice == '':            
            return
        if(choice.isdecimal() and int(choice) in range(0,6)):
            if choice == '1':        
                manage_books_and_authors()           
            elif choice == '2':
                manage_publishers()
            elif choice == '3':
                manage_branches()
            elif choice == '4':
                manage_borrowers()
            elif choice == '5':
                manage_due_date()
        else:
            print('Please enter a valid option: ',end='')