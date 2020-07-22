import borrower_menu, admin_menu, librarian_menu
import db_connections as dbc

def main_menu():
  valid = 0
  while (valid == 0):
    print('''Which user are you?
1) Borrower
2) Librarian
3) Administrator
Or enter 0 to exit
    ''')
    choice = input()
    try:
      choice_as_int = int(choice)
    except:
        print('Please enter a numeric value')
        continue
    if(choice_as_int in range(0,4)):
        if choice == '1':
            borrower_menu.borrower_menu()
        elif choice == '2':
            librarian_menu.LIB1()
        elif choice == '3':
          admin_menu.admin_menu()
        elif choice == '0':
            valid = 1
        #should end the program
    else:
        print('Please enter a valid option\n')

print("Exiting...")
dbc.open_connection()
main_menu()
dbc.close_connection()
exit()