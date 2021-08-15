from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

global conn, cursor
conn = sqlite3.connect("db_VTONLINE.db")
cursor = conn.cursor()

vt = Tk()
vt.title("Planing Consultation")
vt.geometry("1250x800+100+0")
vt.minsize(480,360)
vt['bg'] = "orange"

lbl_titre = Label(vt, text="Bienvenue dans l'application VT_ONLINE", fg="white", bg="grey", font="Verdana 34")
lbl_titre.pack()

lbl_log = Label(vt, text="Introduisez le nom du vétérinaire :", fg="black", bg="orange",font="Verdana 22")
lbl_log.place(x=50, y=100)
entryLog = Entry(vt, font=('arial', 20),  width=5)
entryLog.place(x=460, y=100)

# cursor.execute("SELECT users_id FROM user WHERE nom = ?", (entryLog.get()))
# if cursor.fetchone() is not None:
#     nom_vete = cursor.fetchone()
#     print(nom_vete)


#def image(): IMAGE INSERTION FRAME DROITE
frameR=Frame(vt)
frameR.pack(side = RIGHT)
width=500
height=300
imageVT2=PhotoImage(file="Image3.png").zoom(10).subsample(10)
canvas1 = Canvas(frameR, width=width, height=height, bg='orange', bd=0, highlightthickness=0)
canvas1.create_image(width/2, height/2, image=imageVT2)
canvas1.pack(padx= 20)

################ FRAME GAUCHE
FrameL= Frame(vt)
FrameL.pack(side=LEFT, pady=10, padx=50)

lbl_sstitre = Label(vt, text="Choisissez vos jours de consultations et vos horaires", fg="black", bg="orange",font="Verdana 22")
lbl_sstitre.place(x=60, y=200)

label=Label(FrameL, text = "  AM  -  PM      ", font=("Arial", 20), bg="grey", fg="white")
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

######### Les GET pour les heures de consultations

###########################################
# Connexion à la base de données
def VALIDATE():
    global conn, cursor, nom_vete
    nom_vete = StringVar()
    conn = sqlite3.connect("db_VTONLINE.db")
    cursor = conn.cursor()
    nom_vete = entryLog.get()

#    cursor.execute("SELECT * FROM horaire INNER JOIN user ON horaire.id = users.fk_id")

    lundi=(cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ", ("LUNDI",nom_vete)).fetchone())
    mardi=(cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ", ("MARDI",nom_vete)).fetchone())
    mercredi=(cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ", ("MERCREDI",nom_vete)).fetchone())
    jeudi = (cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ", ("JEUDI",nom_vete)).fetchone())
    vendredi = (cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ", ("VENDREDI",nom_vete)).fetchone())

    lbl6 = Label(FrameL, text="", fg="black", font="Verdana 18")
    lbl6.grid(row=1,column=2,pady=10, padx=10)
    lbl6.config(text=lundi)

    lbl7 = Label(FrameL, text="", fg="black", font="Verdana 18")
    lbl7.grid(row=2,column=2,pady=10, padx=10)
    lbl7.config(text=mardi)

    lbl8 = Label(FrameL, text="", fg="black", font="Verdana 18")
    lbl8.grid(row=3,column=2,pady=10, padx=10)
    lbl8.config(text=mercredi)

    lbl9 = Label(FrameL, text="", fg="black", font="Verdana 18")
    lbl9.grid(row=4,column=2,pady=10, padx=10)
    lbl9.config(text=jeudi)

    lbl10 = Label(FrameL, text="", fg="black", font="Verdana 18")
    lbl10.grid(row=5,column=2,pady=10, padx=10)
    lbl10.config(text=vendredi)


button_valider = Button(vt, text="Valider", command = VALIDATE, fg="black", font="Verdana 20", bd=2, bg="light blue", relief="groove")
button_valider.place(x=560, y=100)



#if __name__ == '__main__':
vt.mainloop()
