import librarian_queries as lq
from admin_functions import *
from helper_functions import *
import borrower_menu as bm

def LIB1():
    user_input = input('''\
Pick from following options:
1) Enter branch you manage
2) Quit to previous 
    
''')
    menu_selection=0
    try:
        menu_selection=int(user_input)
    except:
        print("Please enter a numeric value.")
        LIB1()
    if menu_selection == 1:
        LIB2()
    elif menu_selection == 2:
        return 
    else:
        print("Please choose a number in the list.")
        LIB1()


def LIB2():
    print('''Pick from following branches:''')
    select_branch()


def LIB3(branch):
    user_input = input('''\
Pick from following options:
1) Update the details of the Library
2) Add copies of Book to the Branch
3) Quit to previous
    
''')

    menu_selection=0
    try:
        menu_selection=int(user_input)
    except:
        print("Please enter a numeric value.")
        LIB3(branch)
    if menu_selection == 1:
        update_library(branch)
    elif menu_selection == 2:
        add_copies(branch)
    elif menu_selection == 3:
        return #LIB2()
    else:
        print("Please choose a number in the list.")
        LIB3(branch)


    
def update_library(branch):
    print('You have chosen to update the Branch with Branch Id: ' +str(branch[0]) +  ' and Branch Name: ' + branch[1] )
    user_input = input('''
Choose from the following options:
  1) Update Library name
  2) Update Library address
  3) Quit to previous
    
''')
    if user_input == '1':
        user_input = input('''
Enter new name
or enter  "N/A" for no changes
or enter "quit" to return  
        
''')
        if user_input == "N/A": 
            update_library(branch)
        elif user_input == "quit":
            LIB2()
        else: 
            lq.edit_branch(branch[0], user_input, branch[2])#address isn't set so use the data from branch instead
            print('Successfully updated')

    elif user_input == '2':
        user_input = input('''
Enter new address
or enter  "N/A" for no changes
or enter "quit" to return  
        
''')
        if user_input == 'N/A': 
            update_library(branch)
        elif user_input == 'quit':
            LIB2()
        else: 
            lq.edit_branch(branch[0], branch[1], user_input)#name isn't set so use the data from branch instead
            print("Successfully updated")

    elif user_input == '3':
        LIB3(branch)
    else:
        print("error, invalid input")
        update_library(branch)


def select_branch(branch_list=[]):
    if (len(branch_list) == 0):
        branch_list = lq.get_all_branches()
    menu_itemno = 1
    for branch in branch_list:
        print('''{}) {}, {}'''.format(menu_itemno, branch[1], branch[2]))#branch[1] should be branch name
        menu_itemno=menu_itemno+1
    print("{}) Quit to previous".format(menu_itemno))
    user_input = input()
    try:
        input_as_int = int(user_input)
    except:
        print("Please use a number to select the branch.")
        select_branch(branch_list)
    if input_as_int == menu_itemno:
        return LIB1()
    elif input_as_int < 1 or input_as_int > menu_itemno:
        print("Please select a number in the list")
        return select_branch( branch_list)
    selected_branch = branch_list[input_as_int-1]
    return LIB3(selected_branch)


def add_copies(branch):
    book = select_book() # returns bookId, title, author
    if book is None:
        return
    branchId = branch[0]
    bookId = book[0]
    noOfCopies_tuple = lq.get_noOfCopies(bookId, branchId)#setting noOfCopies to the int in the tuple not the tuple itself
    noOfCopies = -1
    if noOfCopies_tuple is None or noOfCopies_tuple[0] < 1:
        noOfCopies = 0
    else:
        noOfCopies = noOfCopies_tuple[0]
    print("existing number of copies: {}".format(noOfCopies))
    int_input = -1
    while int_input < 0:
        user_input = input("Enter new number of copies: ")
        try:
            int_input = int(user_input)
        except:
            print("Please enter a numeric value.")
            continue
        if int_input < 0:
            print("Please enter a positive value")
            continue
    new_total_copies = 0
    if noOfCopies_tuple is None:
        new_total_copies = int_input
        insert_book_copies(book[0], branch[0], new_total_copies)
    else:
        new_total_copies = noOfCopies + int_input
        edit_book_copies(book[0], branch[0], new_total_copies)
    print("\n{} copies are in the branch!\n".format(new_total_copies))
    
    return LIB3(branch)


def select_book(book_list=[]):
    if(len(book_list)== 0):
        books_in_db = lq.get_all_books()
        book_list = bm.consolidate_book_authors(books_in_db)
    print('Pick the book you want to add copies of to your branch: ')
    menu_itemno = 1
    for book in book_list:
        print("{}) {}, {}".format(menu_itemno, book[1], book[2]))
        menu_itemno=menu_itemno+1
    print("{}) Quit to cancel operation".format(menu_itemno))
    user_input = input()
    #Perform input validation
    try:
        input_as_int = int(user_input)
    except:
        print("Please use a number to select the book.")
        select_book(book_list)
    if input_as_int == menu_itemno:#check for quit request
        return None
    elif input_as_int < 1 or input_as_int > menu_itemno:
        print("Please select a number in the list")
        return select_book(book_list)
    return book_list[input_as_int-1]
      
