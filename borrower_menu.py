import borrower_queries as bq

def borrower_menu():
    """Outer-most menu for borrowers, asks for card number Borr0"""
    tempstring = input("Please input your card number\n")
    try:
        cardNo = int(tempstring)
    except:
        print("Card number should only consist of number please try again.\n")
        borrower_menu()
    if validate_card(cardNo) == 1:
        checkout_or_return(cardNo)
        return
    else:
        print("invalid card, try again")
        borrower_menu()

def checkout_or_return(cardNo):
    """Menu that borrowers always return to. They exit back to the main menu from here. Borr1"""
    user_input = input("""\
Please select an option:
1) Checkout a Book
2) Return a Book
3) Quit to Previous  
""")
    menu_selection=0
    try:
        menu_selection=int(user_input)
    except:
        print("Please enter a numeric value.")
        checkout_or_return(cardNo) 
    if menu_selection == 1:
        checkout_controller(cardNo)
    elif menu_selection == 2:
        return_controller(cardNo)
    elif menu_selection == 3:
        return
    else:
        print("Please choose a number in the list.")
        checkout_or_return(cardNo)
    checkout_or_return(cardNo)

def checkout_controller(cardNo):
    """Logic controller for checking out, goes back to checkout_or_return when done"""
    branch = select_branch("check out from")
    if branch is None:
        return
    book = select_book_menu(cardNo, branch)
    if book is None:
        return
    process_checkout(cardNo, branch, book)
    #input("press enter to continue")

def return_controller(cardNo):
    """Logic controller for returning books, goes back to checkout_or_return when done"""
    branch = select_branch("return to")
    if branch is None:
        return
    book = select_returnable_book(cardNo, branch)
    if book is None:
        return
    process_return(cardNo, branch, book)

def select_branch(action_string, branch_list=[]):
    """Lists all branches and takes in an action string(set in controllers) to reflect action selected by user either checkout or return"""
    if (len(branch_list) == 0):
        branch_list = bq.get_all_branches()
    print("Please select which branch you wish to {} by number:".format(action_string))
    menu_itemno = 1
    for branch in branch_list:
        print("{}) {}, {}".format(menu_itemno, branch[1], branch[2]))#branch[1] should be branch name
        menu_itemno=menu_itemno+1
    print("{}) Quit to previous".format(menu_itemno))
    user_input = input()
    try:
        input_as_int = int(user_input)
    except:
        print("Please use a number to select the branch.")
        select_branch(action_string, branch_list)
    if input_as_int == menu_itemno:
        return None
    elif input_as_int < 1 or input_as_int > menu_itemno:
        print("Please select a number in the list")
        return select_branch(action_string, branch_list)
    selected_branch = branch_list[input_as_int-1]
    return selected_branch

def select_book_menu(cardNo, branch, books_to_list = []):
    """List books that the selected branch has available copies"""
    if len(books_to_list) == 0:
        query_result = bq.find_books_available_for_checkout(cardNo, branch[0])
        books_to_list = consolidate_book_authors(query_result)
    print("Please select the book you wish to checkout by number")
    menu_itemno = 1
    for book in books_to_list:
        print("{}) {} by {}".format(menu_itemno, book[1], book[2]))
        menu_itemno=menu_itemno+1
    print("{}) Quit to cancel checkout".format(menu_itemno))
    user_input = input()
    #Perform input validation
    try:
        input_as_int = int(user_input)
    except:
        print("Please use a number to select the book.")
        select_book_menu(cardNo, branch, books_to_list)
    if input_as_int == menu_itemno:#check for quit request
        return None
    elif input_as_int < 1 or input_as_int > menu_itemno:
        print("Please select a number in the list")
        return select_book_menu(cardNo, branch,books_to_list)
    return books_to_list[input_as_int-1]

def select_returnable_book(cardNo, branch, books_to_list=[]):
    """Lists books that the user has checked out and not returned from the selected branch"""
    if len(books_to_list) == 0:
        query_result = bq.find_books_available_for_return(cardNo, branch[0])
        books_to_list = consolidate_book_authors(query_result)
    print("Please select the book you wish to return by number")
    menu_itemno = 1
    for book in books_to_list:
        print("{}) {} by {}".format(menu_itemno, book[1], book[2]))
        menu_itemno=menu_itemno+1
    print("{}) Quit to cancel return".format(menu_itemno))
    user_input = input()
    #Perform input validation
    try:
        input_as_int = int(user_input)
    except:
        print("Please use a number to select the book.")
        select_returnable_book(cardNo, branch, books_to_list)
    if input_as_int == menu_itemno:#check for quit request
        return None
    elif input_as_int < 1 or input_as_int > menu_itemno:
        print("Please select a number in the list")
        return select_returnable_book(cardNo, branch, books_to_list)
    return books_to_list[input_as_int-1]

def process_checkout(cardNo, branch, book):
    """Takes info from previous checkout steps and sends it to the function that executes the procedure"""
    query_tuple = (cardNo, branch[0], book[0], 0)#cardno, branchId, bookId, placeholder for OUT due_date
    loan_info = bq.checkout_book(query_tuple)
    due_date=loan_info[3][0:10]#removes the time from datetime of query
    print("\nYour book has been checked out. Your due date is: {}\n".format(due_date))

def process_return(cardNo, branch, book):
    """Takes info from previous return steps and sends it to the function that executes the procedure"""
    query_tuple = (cardNo, branch[0], book[0])
    bq.return_book(query_tuple)
    print("\nYour book has been returned. Thanks for visiting!\n")

def validate_card(cardNo):
    """Calls query to make sure card number exists"""
    results = bq.get_card_matches(cardNo)
    if (results is None):
        return 0
    else:
        return 1

def consolidate_book_authors(book_list):
    """Returns that groups the authors as the value and 
    the key is a tuple of the other values (bookId, title, string of author names separated by commas)
    """
    consolidated_book_dictionary = {}
    for book in book_list:
        book_tuple_key = (book[0], book[1]) #(bookId, title)
        if book_tuple_key in consolidated_book_dictionary:#Look into making sure all authors show up
            consolidated_book_dictionary[book_tuple_key].append(book[2])
        else:
            consolidated_book_dictionary[book_tuple_key]=[book[2]]
    #Work on formatting for the dictionary!
    return_list = []
    for key, value in consolidated_book_dictionary.items():
        author_string = ""#string that nicely comma separates the authors
        for i in range(len(value)):
            author_string = author_string + value[i]
            if i < len(value) - 1:#adds a comma and space as long as it isn't the last author
                author_string = author_string + ", "
        temp_tuple = (key[0], key[1], author_string)
        return_list.append(temp_tuple)
    return return_list
