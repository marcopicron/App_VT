from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

vt = Tk()
vt.title("Planing Consultation")
vt.geometry("1250x800+100+0")
vt.minsize(480,360)
vt['bg'] = "orange"


lbl_titre = Label(vt, text="Bienvenue dans l'application VT_ONLINE", fg="white", bg="grey", font="Verdana 34")
lbl_titre.pack()

lbl_log = Label(vt, text="Introduisez votre login svp :", fg="black", bg="orange",font="Verdana 22")
lbl_log.place(x=50, y=100)
entryLog = Entry(vt, font=('arial', 20),  width=5)
entryLog.place(x=400, y=100)

#def image():
frameR=Frame(vt)
frameR.pack(side = RIGHT)
width=500
height=300
imageVT2=PhotoImage(file="Image3.png").zoom(10).subsample(10)
canvas1 = Canvas(frameR, width=width, height=height, bg='orange', bd=0, highlightthickness=0)
canvas1.create_image(width/2, height/2, image=imageVT2)
canvas1.pack(padx= 20)

#######################################
#GRILLE HORAIRES
######################################
FrameL= Frame(vt)
FrameL.pack(side=LEFT, pady=10, padx=50)

lbl_sstitre = Label(vt, text="Choisissez vos jours de consultations et vos horaires", fg="black", bg="orange",font="Verdana 22")
lbl_sstitre.place(x=60, y=200)

label=Label(FrameL, text = "                 AM                      PM                 ", font=("Arial", 20), bg="grey", fg="white")
label.grid(row=0,column=2, columnspan=4,pady=10, padx=18)

lbl1 = Label(FrameL, text="LUNDI", fg="black", font="Verdana 18")
lbl1.grid(row=1,column=1,pady=10, padx=10)
lbl2 = Label(FrameL, text="MARDI", fg="black", font="Verdana 18")
lbl2.grid(row=2,column=1,pady=10, padx=10)
lbl3 = Label(FrameL, text="MERCREDI", fg="black", font="Verdana 18")
lbl3.grid(row=3,column=1,pady=10, padx=10)
lbl4 = Label(FrameL, text="JEUDI", fg="black", font="Verdana 18")
lbl4.grid(row=4,column=1,pady=10, padx=10)
lbl5 = Label(FrameL, text="VENDREDI", fg="black", font="Verdana 18")
lbl5.grid(row=5,column=1, pady=10, padx=10)

######### Les Entrées pour les heures de consultations
#LUNDI
e1 = Entry(FrameL, font=('arial', 20),  width=5)
e1.grid(row=1, column=2,pady=10, padx=10)
e2 = Entry(FrameL, font=('arial', 20),  width=5)
e2.grid(row=1, column=3,pady=10, padx=10)
e3 = Entry(FrameL, font=('arial', 20),  width=5)
e3.grid(row=1, column=4,pady=10, padx=10)
e4 = Entry(FrameL, font=('arial', 20), width=5)
e4.grid(row=1, column=5,pady=10, padx=10)
#MARDI
e5 = Entry(FrameL, font=('arial', 20), width=5)
e5.grid(row=2, column=2,pady=10, padx=10)
e6 = Entry(FrameL, font=('arial', 20),  width=5)
e6.grid(row=2, column=3,pady=10, padx=10)
e7 = Entry(FrameL, font=('arial', 20),  width=5)
e7.grid(row=2, column=4,pady=10, padx=10)
e8 = Entry(FrameL, font=('arial', 20),  width=5)
e8.grid(row=2, column=5,pady=10, padx=10)
#MERCREDI
e9 = Entry(FrameL, font=('arial', 20), width=5)
e9.grid(row=3, column=2,pady=10, padx=10)
e10 = Entry(FrameL, font=('arial', 20), width=5)
e10.grid(row=3, column=3,pady=10, padx=10)
e11 = Entry(FrameL, font=('arial', 20),  width=5)
e11.grid(row=3, column=4,pady=10, padx=30)
e12 = Entry(FrameL, font=('arial', 20),  width=5)
e12.grid(row=3, column=5,pady=10, padx=30)
e13 = Entry(FrameL, font=('arial', 20),  width=5)
#JEUDI
e13.grid(row=4, column=2,pady=10, padx=30)
e14 = Entry(FrameL, font=('arial', 20), width=5)
e14.grid(row=4, column=3,pady=10, padx=30)
e15 = Entry(FrameL, font=('arial', 20), width=5)
e15.grid(row=4, column=4,pady=10, padx=30)
e16 = Entry(FrameL, font=('arial', 20),  width=5)
e16.grid(row=4, column=5,pady=10, padx=10)
#VENDREDI
e17 = Entry(FrameL, font=('arial', 20),  width=5)
e17.grid(row=5, column=2,pady=10, padx=10)
e18 = Entry(FrameL, font=('arial', 20),  width=5)
e18.grid(row=5, column=3,pady=10, padx=10)
e19 = Entry(FrameL, font=('arial', 20), width=5)
e19.grid(row=5, column=4,pady=10, padx=10)
e20 = Entry(FrameL, font=('arial', 20), width=5)
e20.grid(row=5, column=5,pady=10, padx=10)

###########################################
# Connexion à la base de données
def VALIDATE():
    global conn, cursor, users_id
    conn = sqlite3.connect("db_VTONLINE.db")
    cursor = conn.cursor()
    users_id=entryLog.get()
    jour1="LUNDI"
    a,b,c,d = e1.get(),e2.get(),e3.get(),e4.get()
    jour2="MARDI"
    e,f,g,h = e5.get(),e6.get(),e7.get(),e8.get()
    jour3="MERCREDI"
    i,j,k,l= e9.get(),e10.get(),e11.get(),e12.get()
    jour4="JEUDI"
    m,n,o,p= e13.get(),e14.get(),e15.get(),e16.get()
    jour5="VENDREDI"
    q,r,s,t= e17.get(),e18.get(),e19.get(), e20.get()


    ## Communication avec la base de données
    cursor.execute("INSERT INTO horaire (users_id, jour,debut_AM, fin_AM, debut_PM, fin_PM) VALUES(?,?,?,?,?,?)",
                   (users_id,jour1, a, b, c ,d))
    cursor.execute("INSERT INTO horaire (users_id, jour,debut_AM, fin_AM, debut_PM, fin_PM) VALUES(?,?,?,?,?,?)",
                   (users_id,jour2, e, f, g, h))
    cursor.execute("INSERT INTO horaire (users_id, jour,debut_AM, fin_AM, debut_PM, fin_PM) VALUES(?,?,?,?,?,?)",
                   (users_id, jour3, i, j, k, l))
    cursor.execute("INSERT INTO horaire (users_id, jour,debut_AM, fin_AM, debut_PM, fin_PM) VALUES(?,?,?,?,?,?)",
                   (users_id, jour4, m, n, o, p))
    cursor.execute("INSERT INTO horaire (users_id, jour,debut_AM, fin_AM, debut_PM, fin_PM) VALUES(?,?,?,?,?,?)",
                   (users_id, jour5, q, r, s, t))
    conn.commit()


lbl = Label(vt, text="Voulez-vous enregistrer vos modifications ?", fg="black", bg="orange", font="Verdana 24")
lbl.place(x=60, y=640)
button_valider = Button(vt, text="Valider", command = VALIDATE, fg="black", font="Verdana 20", bd=2, bg="light blue", relief="groove")
button_valider.place(x=700, y=640)

#button_valider = Button(vt, text="Annulez", command=ANNULER ,fg="black", font="Verdana 20", bd=2, bg="light blue", relief="groove")
#button_valider.place(x=700, y=680)


# def database_hor():
#     global conn, cursor
#     conn = sqlite3.connect("db_VTONLINE.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         "CREATE TABLE IF NOT EXISTS horaire (hor_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, jour DATETIME NOT NULL, debut_AM TIME, fin_AM TIME,debut_PM TIME, fin_PM TIME)")
#     conn.commit()
#



#if __name__ == '__main__':
vt.mainloop()
