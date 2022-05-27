
#import modules

from ctypes import resize
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *
from PIL import ImageTk, Image
from data import Data
import os


# Membuat window untuk register

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x350")
    register_screen.iconbitmap("Tugas Akhir PDKP/logoundip.ico")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Silakan masukkan informasi anda di bawah ini").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username *")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username, width = 30)
    username_entry.pack()
    Label(register_screen, text="").pack()
    password_lable = Label(register_screen, text="Password *")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*', width = 30)
    password_entry.pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", font = ("Montserrat", 13), width=15, height=2, command = register_user).pack()


# Membuat window untuk Login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.iconbitmap("Tugas Akhir PDKP/logoundip.ico")
    Label(login_screen, text="Silakan masukkan informasi di bawah").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username *").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, width = 30)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password *").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*',  width = 30)
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", font = ("Montserrat", 13), width=15, height=2, command = login_verify).pack()


# Setelah pencet tombol register

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("Montserrat", 11)).pack()


# Setelah pencet tombol login 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

# Login Success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("300x200")
    Label(login_success_screen, text="").pack()
    Label(login_success_screen, text="Login Success", font = ("Montserrat", 14)).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="OK", font = ("Montserrat", 15), command=delete_login_success, width = 8, height = 3).pack()

# Login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Invalid Login")
    password_not_recog_screen.geometry("300x200")

    Label(password_not_recog_screen).pack()
    Label(password_not_recog_screen, text="Invalid Password", font = ("Montserrat", 14)).pack()
    Label(password_not_recog_screen).pack()
    Button(password_not_recog_screen, text="OK", font = ("Montserrat", 14), width = 8, height = 3, command=delete_password_not_recognised).pack()

# User not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("User Not Found")
    user_not_found_screen.geometry("300x200")

    Label(user_not_found_screen).pack()
    Label(user_not_found_screen, text="User Not Found", font = ("Montserrat", 14)).pack()
    Label(user_not_found_screen).pack()
    Button(user_not_found_screen, text="OK", font = ("Montserrat", 14), width = 8, height = 3, command=delete_user_not_found_screen).pack()


# Membuat database

def database():
    global database_screen
    database_screen = Toplevel(main_screen)
    database_screen.title("Database")
    database_screen.geometry("400x200")
    database_screen.iconbitmap("Tugas Akhir PDKP/logoundip.ico")

    Label(database_screen).pack()
    Label(database_screen, text = "Akun yang sudah terbuat:", font = ("Montserrat", 14)).pack()
    Label(database_screen).pack()
    Label(database_screen, text = Data.listData(), font = ("Montserrat", 14)).pack()

# Menghapus window popups

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Membuat Main window (window awal mula)

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("800x450")
    main_screen.resizable(width = 0, height = 0)
    main_screen.title("Program Login Universitas Diponegoro")
    main_screen.iconbitmap("Tugas Akhir PDKP/logoundip.ico")
    bg = PhotoImage(file = "Tugas Akhir PDKP/landscape.png")

    label1 = Label(main_screen, image = bg)
    label1.place(x = 0, y = 0)
    label1.configure(width=800, height=450)

    Label(text="Pilih antara Login atau Register", bg="gray", width="300", height="2", font=("Montserrat", 13)).pack()
    Label(text="").pack()

    Button(text="Login", font = ("Montserrat", 15), height="3", width="30", command = login).pack()
    Label(text="").pack()

    Button(text="Register", font = ("Montserrat", 15), height="3", width="30", command = register).pack()
    img = ImageTk.PhotoImage(Image.open("Tugas Akhir PDKP/bannerlogo.jpg"))
    labelimg = Label(image = img).place(x = 258, y = 383)
    Label(text="").pack()

    Button(text="Database", font = ("Montserrat", 15), command = database, height = "3", width = "30").pack()

    main_screen.mainloop()


main_account_screen()