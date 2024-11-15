import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('crm.db')

# Create a cursor
c = conn.cursor()

# Create a table to store customer information
c.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    company TEXT,
    notes TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
def add_customer(name, email, phone, company, notes):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers (name, email, phone, company, notes) VALUES (?, ?, ?, ?, ?)",
              (name, email, phone, company, notes))
    conn.commit()
    conn.close()
    print(f"Customer {name} added successfully!")
def view_customers():
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(row)
def search_customer(name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE name LIKE ?", ('%' + name + '%',))
    rows = c.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(row)
    else:
        print(f"No customer found with the name: {name}")
def update_customer(id, name=None, email=None, phone=None, company=None, notes=None):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute('''UPDATE customers
                 SET name = COALESCE(?, name),
                     email = COALESCE(?, email),
                     phone = COALESCE(?, phone),
                     company = COALESCE(?, company),
                     notes = COALESCE(?, notes)
                 WHERE id = ?''', (name, email, phone, company, notes, id))
    conn.commit()
    conn.close()
    print(f"Customer with ID {id} updated successfully!")
def delete_customer(id):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print(f"Customer with ID {id} deleted.")
def menu():
    print("""
    ==== Simple CRM ====
    1. Add Customer
    2. View All Customers
    3. Search Customer
    4. Update Customer
    5. Delete Customer
    6. Exit
    """)

def main():
    while True:
        menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            company = input("Enter company name: ")
            notes = input("Enter additional notes: ")
            add_customer(name, email, phone, company, notes)
        
        elif choice == '2':
            view_customers()
        
        elif choice == '3':
            name = input("Enter name to search: ")
            search_customer(name)
        
        elif choice == '4':
            id = int(input("Enter customer ID to update: "))
            name = input("Update name (leave blank to skip): ")
            email = input("Update email (leave blank to skip): ")
            phone = input("Update phone (leave blank to skip): ")
            company = input("Update company (leave blank to skip): ")
            notes = input("Update notes (leave blank to skip): ")
            update_customer(id, name or None, email or None, phone or None, company or None, notes or None)
        
        elif choice == '5':
            id = int(input("Enter customer ID to delete: "))
            delete_customer(id)
        
        elif choice == '6':
            print("Exiting CRM. Goodbye!")
            break
        
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
