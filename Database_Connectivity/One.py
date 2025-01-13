import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection

def connect_db() -> MySQLConnection:
    """Establish connection with MySQL"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="club_py"
        )

        if connection.is_connected():
            version_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server Version {version_info}")
            return connection
        
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def create_user(name: str, email: str, age: int, country: str) -> None:
    pass

def read_users() -> None:
    pass

def update_user(user_id: int, new_name: str = None, new_email: str = None, new_age: int = 0, new_country: str = None) -> None:
    pass

def get_user_by_id(user_id: int) -> None:
    pass

def delete_user(user_id: int) -> None:
    pass

def main():
    while True:
        print("\n-- CRUD Menu ---")
        print("1. Create User")
        print("2. Read All User")
        print("3. Update User")
        print("4. Delete User")
        print("5. GetUserById")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        match choice:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case 6:
                pass

            case _:
                print("Invalid choice. Please enter a number betwee 1 and 6.")

if __name__ == "__main__":
    main()