from helper_functions import *
import db_connections as dbc
from datetime import datetime

def add_book():
    valid = 0
    while valid == 0:
        title = input('Insert Book Title or Enter to return to admin menu: ')
        if title == '':
          return
        elif lookup('find_book', [title, 0]) != 0:
            print('Book already exists!')
        else:
            print('Select a publisher: ')
            pubs = display_publishers()
            print('00) To create new publisher\nEnter to skip')  
         
            while valid == 0:         
                choice = input()
                if choice.lower() == '00':
                    proc('insert_book', [title, add_publisher(1)])
                    valid = 1
                elif choice == '':
                    proc('insert_book', [title, 0])
                    valid = 1
                elif choice.isdecimal() and int(choice) in range (1, [len(pubs)+1][0]):
                    proc('insert_book', [title, pubs[int(choice) - 1][0]])
                    valid = 1             
                else:
                    print('Select a valid option')  

         
            print('Select an author: ')
            authors = display_authors()           
            print('00) To create new author\nEnter to skip')             
            bookid = lookup('find_book', [title, 0])  
            valid = 0
            while valid == 0:         
                choice = input()
                if choice.lower() == '00':
                    res = add_author(1)
                    if res != 0:
                        insert_book_author(bookid, res)                 
                    else:
                        print('Since no author was added, try again')                  
                elif choice == '':
                    print(title,'has been added to the database! Enter to continue...')
                    return 
                elif choice.isdecimal() and int(choice) in range (1, [len(authors)+1][0]):
                    insert_book_author(bookid,authors[int(choice) - 1][0])
                else:
                    print('Select a valid option')
                coAuth = input('''Add co-Author? (y/n): ''') 
                if coAuth.lower() == 'y':
                    print('Select an author: ')
                    authors = display_authors()           
                    print('0) To end\n00) To create new author ')
                elif coAuth.lower() == 'n':
                    print(title,'has been added to the database! Enter to continue...')
                    return
                          
def delete_book():
    valid = 0
    while valid == 0:   
        print('Select a book to delete or Enter to exit: ')         
        books = display_books()        
        choice = input()
        if choice == '':
            return
        elif int(choice) in range(1, len(books)+1):          
    
            if lookup('check_book_dependencies', [int(choice), 0]) > 0:
                print('Deleting this book will cause issues with dependancy in the data base. No action taken')  
            else:          
                proc('delete_book_author', [books[int(choice)-1][0], -1])
                proc('delete_book', [books[int(choice)-1][0],])                
                print('Book has been deleted!')   
                return                 
        else:
            print('Select a valid option')

def update_book():
    valid = 0
    while valid == 0:
        print('Select a book to update: ')
        books = display_books()
        print('Or enter to exit')

        choose_book = 0
        while choose_book == 0:        
            choice = input()
            if choice == '':
                return
                #choose the book
            elif int(choice) in range(1, len(books)+1):
                bookid = books[int(choice)-1][0]  
                new_title = input('Enter a new book title, leave blank for no changes: ')
                print('Select a new publisher, or press enter to skip: ')
                pubs = display_publishers()
                print('00) To create new publisher') 
                pub_loop  = 0 
                while pub_loop == 0:         
                    choice = input()
                    if choice == '00':
                        new_pub = add_publisher(1)
                        proc('update_book', [bookid, new_title, new_pub])
                        pub_loop = 1
                        choose_book = 1                       
                    elif choice == '':                                       
                        proc('update_book', [int(bookid), new_title, 0])
                        pub_loop = 1 
                        choose_book = 1
                    elif int(choice) in range (1, len(pubs)+1):
                        proc('update_book', [bookid, new_title, pubs[int(choice)-1][0]])
                        pub_loop = 1
                        choose_book = 1           
                    else:
                        print('Select a valid option')


                #BookAuthor                      
                author_loop = 0
                while author_loop == 0:
                    print('Current authors of this book: ')
                    book_auth = lookup_authors_of_book(int(bookid))
                    choice = input('''\nSelect a choice:
1) Add author to this book
2) Remove author from this book
Or press Enter to skip
\n''')  
                    if choice == '1':
                        print('Select an author to associate with this book: ')
                        authors = display_authors()           
                        print('00) To create new author\nOr leave blank to skip ')            
                        add_author_loop = 0              
                        while add_author_loop == 0:         
                            choice = input()
                            if choice == '00':
                                authorID = add_author(1)
                                if authorID != 0:
                                    insert_book_author(bookid, authorID)  
                                    print('New author has been associated with this book!')                                  
                                else:
                                    print('Since no author was added, try again')
                            elif choice == '':                               
                                author_loop = 1        
                            elif int(choice) in range (1, len(authors)+1):
                                authorid = authors[int(choice) - 1][0]                                
                                if lookup_book_author(int(bookid), authorid) == 0:
                                    insert_book_author(int(bookid), authorid)                                         
                                else:
                                    print('Author already exists for this book!, please select a new author')
                            add_author_loop = 1
                    elif choice == '2':
                        print('Select an author to remove from this book, Or Enter to exit: ')
                        remove_loop = 0
                        while remove_loop == 0:
                            choice = input()                        
                            if choice == '':                                
                                remove_loop=1                                                   
                                    
                            elif int(choice) in range (1, len(book_auth)+1):
                                author = book_auth[int(choice) - 1][0]
                                proc('delete_book_author', [int(bookid), lookup('find_author', [author, 0])])
                                print('Author deleted')
                                remove_loop = 1
                    elif choice == '':
                        remove_loop = 1
                        author_loop = 1
                    else:
                        print('Select a valid option')

            else:
                print('Select a valid option') 

def add_author(location):
    valid = 0
    while valid == 0:
        author = input('Enter new authors name, leave blank to stop: ')
        if author == '':
          return 0
        else:
            verify = lookup('find_author', [author, 0])
            if verify != 0:
                print('Author already exists!, enter a new one')
            else: 
                proc('insert_author', [author,])
                print('Author added!')
                if location == 1:
                    return lookup('find_author', [author, 0])
            return
def delete_author():
    valid = 0
    while valid == 0:
        authors = display_authors()
        choice = input('Select author to delete or Enter to exit: ')
        if choice == '':
            return
        if int(choice.isdecimal() and choice) in range(1, len(authors)+1):
            authorid = authors[int(choice)-1][0] 
            if lookup('check_author_dependencies', [authorid, 0]) == 0: 
                proc('delete_author', [authorid,])  
                print('Author deleted!')
                return 
            else:
                print('Deleting this author will cause dependency issues within the database as it is associated with an book. No action taken')
        else:
            print('Enter a valid choice')  

def update_author():
    valid = 0
    while valid == 0:
        print('Authors:')
        authors = display_authors()
        choice = input('Select author to update or Enter to exit: ')
        if choice == '':
            return
        if int(choice) in range(1, len(authors)+1):
            authorid = authors[int(choice)-1][0]          
            new_name = input("Enter new name for the author: ")
            if new_name.strip() != '':
                proc('update_author', [authorid, new_name])  
                print('Author updated!')  
                return   
            else:
                print('No action taken!')

def add_publisher(location):
    valid = 0
    while valid == 0:
        publisher = input('Enter a publisher name, leave blank to stop: ')
        if publisher.strip() == '':
            return 0
        else:
            verify = lookup('find_publisher', [publisher, 0])
            if verify != 0:
                print('publisher already exists!')
            else: 
                valid = 1
                address = input('Enter publisher address: ')
                phone = input('Enter publisher phone number: ')
                proc('insert_publisher', [publisher, address, phone])
                print('Publisher added!')
                if location == 1:
                    return lookup('find_publisher', [publisher, 0])
                

def update_publisher():
    print('Enter publisher name to edit')
    valid = 0
    while valid == 0:
        pubs = display_publishers()
        choice = input('Select publisher to update or Enter to exit: ')
        if choice == '':
            return
        elif int(choice.isdecimal() and choice) in range(1, len(pubs)+1):
            new_name = input('Enter new publisher name or Enter to skip: ')      
            new_address = input('Enter new publisher address or Enter to skip: ')
            new_phone = input('Enter new publisher phone or Enter to skip: ')
            proc('update_publisher', [pubs[int(choice)-1][0], new_name, new_address, new_phone])
          
            print('Publisher has been updated!')
        else:
            print('Enter a valid choice!')
      

def delete_publisher():
    valid = 0
    while valid == 0:
        print('Select publisher to delete, or Enter to exit: ')
        pubs = display_publishers()
        choice = input()
        if choice == '':
            return
        elif int(choice) in range(1, len(pubs)+1):
            pubid = pubs[int(choice)-1][0]
            if lookup('check_publisher_dependencies', [pubid, 0]) > 0:
                print('Deleting this publisher will cause dependency issues with some books. No action taken at this time')
            else: 
                proc('delete_publisher', [pubid,])
                print('Publisher was successfully deleted!')               
        else:
            print('Please enter a valid entry')

def add_branch(): 
    valid = 0
    while valid == 0:
        name = input('Insert a new branch name (Or hit ENTER to return to previous): ')
        if name.strip() == '':
            return 0
        elif lookup('find_branch', [name, 0]) != 0:
            print('This branch already exists!')
        else:
            address = input('Insert address: ')
            proc('insert_branch', [name, address])
            print('Branch has been added!')
            return
                  
def update_branch():     
    valid = 0
    while valid == 0:
        print('Select a branch to edit or Enter to exit: ')
        x = display_branches()  
        branch = input()
        if branch == '':
            return
        if(branch.isdecimal() and int(branch) in range(1,len(x)+1)):
            name = input('Enter new name, or enter to skip: ')
            address = input('Enter new address, or enter to skip: ')            
            proc('update_branch', [(x[int(branch)-1][0], name, address)])
            return
        else:
            print('Enter valid choice')
            
def delete_branch():   
    valid = 0
    while valid == 0:
        print('Select a branch to delete: ')
        x = display_branches()
        branch = input()
        if branch == '':
            return 0        
        if(branch.isdecimal() and int(branch) in range(1,len(x)+1)):
            if lookup('check_branch_dependencies', [x[int(branch) -1][0], 0]) > 0:
                print('Deleting this branch will cause dependancy issues within the database. No action taken at this time')
            else:
                proc('delete_branch', [x[int(branch) -1][0],])
                print('Branch successfully deleted!')
                return
        else:
            print('Please choose a valid option: ')
    
def add_borrower():
    valid = 0
    while valid == 0:
        name = input("Insert borrower name to add, or enter to exit: ")
        if name.strip() == '':
            return
        address = input("Insert address or enter to skip: ")
        phone = input("Insert phone number or enter to skip: ")
        result = insert_borrower(name, address, phone)
        if result == 0:
            print('User with identical information already exists!')
        else:
            print('Borrower added!')
            return

    

def update_borrower():
    #`update_borrower`(IN cardNo int, IN name CHAR(50), IN address CHAR(50), IN phone CHAR
    valid = 0
    while valid == 0:
        print('Select a borrower to update: ')
        x = display_borrowers()
        choice = input()
        if choice == '':
            return 0        
        if(choice.isdecimal() and int(choice) in range(1,len(x)+1)):
            name = 'null'
            address = 'null'
            phone = 'null'
            temp = input("Update Name (leave blank if you do not want to change):\n")
            if temp !='':
                name = temp
                temp = input("Update Address (leave blank if you do not want to change):\n")
            if temp !='':
                address = temp
            temp = input("Update Phone (leave blank if you do not want to change):\n")
            if temp !='':
                phone = temp
            proc('update_borrower', [x[int(choice)-1][0], name, address, phone])
            print("Updated borrower")
            return
        else:
            print('Please choose a valid option: ')



def delete_borrower():
    valid = 0
    while valid == 0:
        print('Select a borrower to delete: ')
        x = display_borrowers()
        choice = input()
        if choice == '':
            return 0        
        if(choice.isdecimal() and int(choice) in range(1,len(x)+1)):
            if lookup('check_borrower_dependencies', [x[int(choice)-1][0], 0]) > 0:
                print('This borrower has books loaned out, cannot delete at this time.')
            else:
                proc('delete_borrower', [x[int(choice) -1][0],])
                print('Borrower successfully deleted!')
                return
        else:
            print('Please choose a valid option: ')
    

def manage_due_date():
    valid = 0
    while valid == 0:
        print('Select user to override book loan or Enter to exit: ')
        x = display_borrowers()
        cardNo = input()
        if cardNo == '':
            return
        if cardNo.isdecimal() and int(cardNo) in range(1,len(x)+1):
            bookLoop = 0
            while bookLoop == 0:
                bb = display_borrower_books(x[int(cardNo)-1][0])
                
                if bb:        
                    choice = input('Select a book loan to override, or Enter to exit: ')
                    if choice == '':
                        return
                    elif int(choice) in range(1,len(bb)+1):
                        hourLoop= 0
                        while hourLoop == 0:
                            new_date = input('Enter amount of days to extend: ') 
                            if new_date.isdecimal():
                                hourLoop = 1                                               
                        book =bb[int(choice)-1][0]
                        branch =bb[int(choice)-1][1]
                        cardNo=bb[int(choice)-1][2]               
                        proc('update_due_date', [book, branch, cardNo, new_date])
                        bookLoop=1
                        print('\nDue date has been pushed back {} day.\n'.format(new_date))
                    else:
                        print('Enter a valid choice')
                else:
                    print('This user has no book loans!')
                    bookLoop=1
        else:
            print('Enter a valid choice')