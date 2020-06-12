import mysql.connector
from mysql.connector import errorcode

libDB=None
def open_connection():
    """Function to open the connection and return it so cursors can be made elsewhere"""
    try:
        global libDB
        libDB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Fall2019!",#change to what your root password is locally
            database='library2'
        )
        print("connection opened")
        
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)

    return libDB #needed when called in other modules

def close_connection():
    libDB.close()
    print("connection closed")

def commit_db():
    return libDB.commit()

def get_db_cursor():
    return libDB.cursor()

def show_tables():
    """Debugging Query to see if our schema exists"""
    open_connection()
    libcursor = get_db_cursor()
    libcursor.execute("SHOW TABLES")
    for db in libcursor:
        print(db)
    libcursor.close()
    close_connection()
