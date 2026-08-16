"""
registration:
    userid:int
    name:str
    email:str
    phone:str
    username:str
    password:str
    created_at:datetime
login:
    loginid:int
    userid:int
    username:str
    password:str
"""
import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import hashlib

def create_database():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login (
            login_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES registrations(user_id)
        )
    """)

    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ========================================================
# REGISTRATION
# ========================================================
def open_registration():
    registration = tk.Toplevel(login_window)
    registration.title("Registration")
    registration.geometry("600x400")

    # Make registration modal
    registration.transient(login_window)
    registration.grab_set()

    
# name widget
    tk.Label(
        registration, text="Enter Name", font=("Arial", 14)
        ).grid(row=0, column=0, padx=10, pady=10)

    txtName = tk.Entry(registration, font=("Arial", 14))

    txtName.grid(row=0, column=1, padx=10, pady=10)
# email widget
    tk.Label(
        registration, text="Enter Email", font=("Arial", 14)
        ).grid(row=1, column=0, padx=10, pady=10) 
      
    txtEmail = tk.Entry(registration, font=("Arial", 14))
    txtEmail.grid(row=1, column=1, padx=10, pady=10) 

# phone widget
    tk.Label(
        registration, text="Enter Phone", font=("Arial", 14)
        ).grid(row=2, column=0, padx=10, pady=10)   
    
    txtPhone = tk.Entry(registration, font=("Arial", 14))
    txtPhone.grid(row=2, column=1, padx=10, pady=10)   
#username widget
    tk.Label(
        registration, text="Enter Username", font=("Arial", 14)
        ).grid(row=3, column=0, padx=10, pady=10)
    txtUsername = tk.Entry(registration, font=("Arial", 14))
    txtUsername.grid(row=3, column=1, padx=10, pady=10)    
#password widget
    tk.Label(
        registration, text="Enter Password", font=("Arial", 14)
        ).grid(row=4, column=0, padx=10, pady=10)   
    txtPassword = tk.Entry(registration, font=("Arial", 14), show="*")
    txtPassword.grid(row=4, column=1, padx=10, pady=10)  

    def submit_registration():
        name = txtName.get()
        email = txtEmail.get()
        phone = txtPhone.get()
        username = txtUsername.get()
        password = txtPassword.get()

        if not name or not email or not username or not password:
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        hashed_password = hash_password(password)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO registrations (name, email, phone, created_at)VALUES (?, ?, ?, ?)", (name, email, phone, created_at))
            user_id = cursor.lastrowid

            cursor.execute("""
                INSERT INTO login (user_id, username, password)
                VALUES (?, ?, ?)
            """, (user_id, username, hashed_password))

            conn.commit()
            messagebox.showinfo("Success", "Registration successful")
            registration.destroy()  # Close registration window
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username or Email already exists")
        finally:
            conn.close()

    tk.Button(registration, text="Submit", command=submit_registration).grid(row=5, column=0, columnspan=2, pady=20)

def login():
    username= user_entry.get().strip()
    password= pass_entry.get().strip()

    if not username or not password:
        messagebox.showwarning(
            "Missing Information", 
            "Please enter both username and password",
            parent=login_window
            )
        return
    
    userhashed_password = hash_password(password)

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT login.username, login.password
        FROM login
        WHERE login.username = ? AND login.password = ?
    """, (username, userhashed_password))
    result = cursor.fetchone()
    conn.close()

    if result:
        login_window.destroy()  # Close login window
        show_dashboard(username)
    else:
        messagebox.showerror("Error", "Invalid credentials", parent=login_window)

#---------------------------------------------------------
# Dashboard
#---------------------------------------------------------
def on_dashboard_close():
    root.destroy()  # Close entire application

def show_dashboard(username):
    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")

    tk.Label(dashboard, text="Welcome to Dashboard").pack(pady=20)
    tk.Label(dashboard, text=f"Hello {username}").pack(pady=10)
    dashboard.protocol("WM_DELETE_WINDOW", on_dashboard_close)


#---------------------------------------------------------
# Main root window (Login hidden initially)
#--------------------------------------------------------

create_database()  # Ensure database and tables are created
root = tk.Tk()
root.withdraw()  # Hide root until login succeeds
login_window = tk.Toplevel(root)
login_window.title("Login")
login_window.geometry("400x200")    

login_window.protocol("WM_DELETE_WINDOW", lambda: root.destroy())  # Close entire application on login window close

tk.Label(login_window, text="Enter your Username").grid(row=0, column=0, padx=10, pady=10)
user_entry = tk.Entry(login_window)
user_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_window, text="Enter your Password").grid(row=1, column=0, padx=10, pady=10)
pass_entry = tk.Entry(login_window, show="*")
pass_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(login_window, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(login_window, text="Registration", command=open_registration).grid(row=3, column=0, columnspan=2, pady=10)    
root.mainloop()



