import mysql.connector
from getpass import getpass

# Connect to MySQL Database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",
        database="pharmacy_db"
    )

# Register User (Admin or Manager)
def register_user(role):
    print(f"\n--- {role.capitalize()} Registration ---")
    name = input("Name: ")
    email = input("Email: ")
    password = getpass("Password: ")

    db = get_db_connection()
    cursor = db.cursor()
    query = f"INSERT INTO {role} (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, password))
    db.commit()
    db.close()
    print(f"{role.capitalize()} registered successfully!")

# Login User
def login_user(role):
    print(f"\n--- {role.capitalize()} Login ---")
    email = input("Email: ")
    password = getpass("Password: ")

    db = get_db_connection()
    cursor = db.cursor()
    query = f"SELECT name FROM {role} WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    db.close()

    if result:
        print(f"Welcome {result[0]} ({role.capitalize()})!")
        return result[0]  # return user's name
    else:
        print("Invalid credentials.")
        return None

# Add Medicine (Manager)
def add_medicine(manager_name):
    print("\n--- Add Medicine ---")
    name = input("Medicine Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    db = get_db_connection()
    cursor = db.cursor()
    query = "INSERT INTO medicine (name, quantity, price, added_by) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, quantity, price, manager_name))
    db.commit()
    db.close()
    print("Medicine added successfully.")

# View Medicines
def view_medicines():
    print("\n--- List of Medicines ---")
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM medicine")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Qty: {row[2]}, Price: ₹{row[3]}, Added By: {row[4]}")
    db.close()

# Delete Medicine by ID
def delete_medicine():
    view_medicines()
    med_id = int(input("Enter Medicine ID to Delete: "))
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM medicine WHERE id=%s", (med_id,))
    db.commit()
    db.close()
    print("Medicine deleted successfully.")

# Admin View All Managers
def view_all_managers():
    print("\n--- All Managers ---")
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email FROM manager")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    db.close()

# Main Menu
def main():
    while True:
        print("\n===== Pharmacy Management System =====")
        print("1. Admin Register")
        print("2. Admin Login")
        print("3. Manager Register")
        print("4. Manager Login")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user('admin')
        elif choice == '2':
            admin_name = login_user('admin')
            if admin_name:
                while True:
                    print("\n--- Admin Panel ---")
                    print("1. View All Managers")
                    print("2. View All Medicines")
                    print("3. Logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == '1':
                        view_all_managers()
                    elif sub_choice == '2':
                        view_medicines()
                    elif sub_choice == '3':
                        break
        elif choice == '3':
            register_user('manager')
        elif choice == '4':
            manager_name = login_user('manager')
            if manager_name:
                while True:
                    print("\n--- Manager Panel ---")
                    print("1. Add Medicine")
                    print("2. View Medicines")
                    print("3. Delete Medicine")
                    print("4. Logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == '1':
                        add_medicine(manager_name)
                    elif sub_choice == '2':
                        view_medicines()
                    elif sub_choice == '3':
                        delete_medicine()
                    elif sub_choice == '4':
                        break
        elif choice == '5':
            print("Exiting Pharmacy Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()


-MySQL Setup:

CREATE DATABASE pharmacy_db;

USE pharmacy_db;

CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE manager (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE medicine (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    quantity INT,
    price FLOAT,
    added_by VARCHAR(100)
);
