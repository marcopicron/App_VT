from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

root = Tk()
root.title("Formulaire d'identification")

width = 540
height = 780
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# =======================================VARIABLES=====================================
LOGIN = StringVar()
PASSWORD = StringVar()
PRENOM = StringVar()
NOM = StringVar()
RUE = StringVar()
CODE = StringVar()
VILLE= StringVar()
TEL = StringVar()
EMAIL= StringVar()

# =======================================METHODS=======================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_VTONLINE.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS user (users_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, login TEXT, password TEXT, prenom TEXT, nom TEXT, adresse TEXT, code INTEGER, ville TEXT, tel TEXT, email TEXT, type TEXT)")

def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)

    lbl_username = Label(LoginFrame, text="Login:", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=2)

    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)

    username = Entry(LoginFrame, font=('arial', 20), textvariable=LOGIN, width=15)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*" )
    password.grid(row=2, column=1)

    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)

    lbl_register = Label(LoginFrame, text="S'enregistrer", fg="Blue", font=('arial', 22))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', ToggleToRegister)


def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame()
#    RegisterFrame.title("Registration")
    RegisterFrame.pack(side=TOP, pady=2)
    lbl_username = Label(RegisterFrame, text="Login:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="Prénom:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Nom:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_adresse = Label(RegisterFrame, text="Rue + N°:", font=('arial', 18), bd=18)
    lbl_adresse.grid(row=5)
    lbl_code = Label(RegisterFrame, text="Code Postal :", font=('arial', 18), bd=18)
    lbl_code.grid(row=6)
    lbl_adresse = Label(RegisterFrame, text="Ville:", font=('arial', 18), bd=18)
    lbl_adresse.grid(row=7)
    lbl_code = Label(RegisterFrame, text="Téléphone:", font=('arial', 18), bd=18)
    lbl_code.grid(row=8)
    lbl_email = Label(RegisterFrame, text="E-Mail or Website:", font=('arial', 18), bd=18)
    lbl_email.grid(row=9)

    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=12, columnspan=2)

    username = Entry(RegisterFrame, font=('arial', 20), textvariable=LOGIN, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=PRENOM, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=NOM, width=15)
    lastname.grid(row=4, column=1)

    adresse = Entry(RegisterFrame, font=('arial', 20), textvariable=RUE, width=15)
    adresse.grid(row=5, column=1)
    code = Entry(RegisterFrame, font=('arial', 20), textvariable=CODE, width=15)
    code.grid(row=6, column=1)
    ville = Entry(RegisterFrame, font=('arial', 20), textvariable=VILLE, width=15)
    ville.grid(row=7, column=1)
    telephone = Entry(RegisterFrame, font=('arial', 20), textvariable=TEL, width=15)
    telephone.grid(row=8, column=1)
    email = Entry(RegisterFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=9, column=1)

    btn_login = Button(RegisterFrame, text="S'enregistrer", font=('arial', 18), width=35, command=RegisterUser)
    btn_login.grid(row=10, columnspan=2, pady=10)
    btn_login = Button(RegisterFrame, text="S'enregistrer en tant que professionel", font=('arial', 14), width=35, command=RegisterStaff)
    btn_login.grid(row=11, columnspan=2, pady=10)

    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)

def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()

def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()

# ============================ENREGISTREMENT DES DONNEES UTILISATEURS==========================
def RegisterUser():
    Database()
    if LOGIN.get == "" or PASSWORD.get() == "" or PRENOM.get() == "" or NOM.get == "":
        lbl_result2.config(text="Veuillez compléter le formulaire !", fg="orange")
    else:
        cursor.execute("SELECT * FROM user WHERE login = ?", (LOGIN.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Ce nom existe déjà", fg="red")
        else:
            cursor.execute("INSERT INTO user (login, password, prenom, nom, adresse, code, ville, tel , email, type) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, 'user')",
                           (str(LOGIN.get()), str(PASSWORD.get()), str(PRENOM.get()), str(NOM.get()), str(RUE.get()), str(CODE.get()), str(VILLE.get()),str(TEL.get()), str(EMAIL.get())))
            conn.commit()
            LOGIN.set("")
            PASSWORD.set("")
            PRENOM.set("")
            NOM.set("")
            RUE.set("")
            CODE.set("")
            VILLE.set("")
            TEL.set("")
            EMAIL.set("")

            lbl_result2.config(text="Vous êtes bien enregistré !", fg="black")
        cursor.close()
        conn.close()
# ============================ENREGISTREMENT DES DONNEES VETERINAIRES==========================
def RegisterStaff():
    Database()
    if LOGIN.get == "" or PASSWORD.get() == "" or PRENOM.get() == "" or NOM.get == "":
        lbl_result2.config(text="Veuillez compléter le formulaire !", fg="orange")
    else:
        cursor.execute("SELECT * FROM user WHERE login = ?", (LOGIN.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Ce nom existe déjà", fg="red")
        else:
            cursor.execute("INSERT INTO user (login, password, prenom, nom, adresse, code, ville, tel , email, type) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, 'staff')",
                           (str(LOGIN.get()), str(PASSWORD.get()), str(PRENOM.get()), str(NOM.get()), str(RUE.get()), str(CODE.get()), str(VILLE.get()),str(TEL.get()), str(EMAIL.get())))
            conn.commit()
            lbl_result2.config(text="Vous êtes bien enregistré en tant que Professionnel !", fg="black")
        cursor.close()
        conn.close()

# ============================ OUVERTURE DE LA FENETRE USER ==========================
def utilisateur():
    winAdmin = Toplevel()
    winAdmin.geometry("600x300")
    winAdmin.title("Fenêtre Utilisateur")
    winAdmin['bg'] = "ivory"
    label_accueil1 = Label(winAdmin, text="Fenêtre USER", fg="black",
                           font="Verdana 18")
    label_accueil1.pack(pady=5)
    winAdmin.mainloop()

# ============================ OUVERTURE DE LA FENETRE VETERINAIRE==========================
def staff():
    winStaff = Toplevel()
    winStaff.geometry("600x300")
    winStaff.title("Fenêtre Professionnel")
    winStaff['bg'] = "ivory"
    label_accueil1 = Label(winStaff, text="Bienvenue aux VETERINAIRES", fg="black",
                           font="Verdana 18")
    label_accueil1.pack(pady=5)
    winStaff.mainloop()


# ============================ VERIFICATION DU LOGIN ET DU MOT DE PASSE ==========================
def Login(event):
    Database()
    if LOGIN.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Veuiller complétez le formulaire : Login et/ou mot de passe manquant", fg="orange")
    else:
        cursor.execute("SELECT * FROM user WHERE login = ? and password = ?",
                       (LOGIN.get(), PASSWORD.get()))

        if cursor.fetchone() is not None:
            lbl_result1.config(text="Identification REUSSIE", fg="green")
            l = cursor.execute("SELECT type FROM user WHERE login=? AND password = ?",
                               (LOGIN.get(), PASSWORD.get()))
            us = l.fetchone()
            if us [0]== "user":
                utilisateur()
            else :
                staff()

        else:
            lbl_result1.config(text="Mot de passe et/ou login invalides", fg="red")

LoginForm()

# ========================================MENUBAR WIDGETS==================================
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="Exit", command=Exit)
# menubar.add_cascade(label="File", menu=filemenu)
# root.config(menu=menubar)

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.bind('<Return>', Login )
    root.mainloop()
