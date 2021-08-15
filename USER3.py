import sqlite3
from tkinter import *
from tkinter import ttk


global conn, cursor, codeP, a, b, c, Nom
conn = sqlite3.connect("db_VTONLINE.db")
cursor = conn.cursor()


# ================================FENETRE PRINCIPALE=====================================
win = Tk()
win.title("Rechercher votre vétérinaire")
win.geometry("800x900+350+70")
win['bg'] = "orange"

label_accueil1 = Label(win, text="Bienvenue sur VT_ONLINE", fg="white", bg="grey",font="Verdana 34")
label_accueil1.grid(row=1, columnspan=4, sticky="W", padx=140, pady=10)

label_accueil2 = Label(win, text="Choisissez votre spécialiste près de chez vous", fg="black",font="Verdana 18")
label_accueil2.grid(row=2, columnspan=4, sticky="W", padx=140, pady=20)

#Les labels
labelUn = Label(win, text="Votre animal ? ")
labelUn.grid(row=3, column=1, sticky="E", padx=10)
labelDeux = Label(win, text="Type de consultation:")
labelDeux.grid(row=4, column=1, sticky="E", padx=10)
labelTrois = Label(win, text="Votre code postal :")
labelTrois.grid(row=5, column=1, sticky="E", padx=10)
label4 = Label(win, text="Commentaires :")
label4.grid(row=6, column=1, sticky="E", padx=10)


#COMMENTAIRES
frameC=Frame(win)
frameC.grid(row=6, column=2, rowspan=2)
comment = Entry(win)
comment.grid(row=6, column=2)

# =======================================LISTE DEROULANTE=====================================
#Liste déroulante animaux
frame1=Frame(win)
frame1.grid(row=3, column=2)
vlist1 = ["chien", "chat", "lapin","chinchille", "gerbille", "souris", "dègue du Chili", "furet", "poule", "caille", "canard", "oie", "cochon d'inde", "chèvre","chèvre","Perruche", "Perroquet","Vache","Mouton", "poisson","chèvre", "âne", "autruche", "alpagua", "serpent","Plusieurs animaux"]
Combo1=ttk.Combobox(frame1,values=vlist1)
Combo1.set ("Veuillez choisir")
Combo1.pack()
Combo1.bind('<<ComboboxSelected>>', lambda e: print(Combo1.get()))
a=Combo1.get()


#Liste déroulante type de consultations
frame2=Frame(win)
frame2.grid(row=4, column=2)
vlist2 = ["Vaccination", "Stérilisation", "Vermifuge","Radiographie", "Puce électronique", "Visite à domicile", "Dentition", "Opération chirurgie", "Plusieurs animaux"]
Combo2=ttk.Combobox(frame2,values=vlist2)
Combo2.set ("Veuillez choisir")
Combo2.pack()
Combo2.bind('<<ComboboxSelected>>', lambda e: print(Combo2.get()))
b=Combo2.get()

#CODE POSTAUX : LISTE DEROULANTE
frame3=Frame(win)
frame3.grid(row=5, column=2)
conn = sqlite3.connect("db_VTONLINE.db")
cursor = conn.cursor()

cp=cursor.execute("SELECT code FROM user")
codes=cp.fetchall()

#vlist3 = [CP]
Combo3=ttk.Combobox(frame3,values=codes)
Combo3.set ("Veuillez choisir")
Combo3.pack()
Combo3.bind('<<ComboboxSelected>>', lambda e: print(Combo3.get()))

# IMAGE VT
width=200
height=150
imageVT1=PhotoImage(file="Image1.png").zoom(35).subsample(32)
canvas1 = Canvas(win, width=width, height=height, bg='orange',bd=0, highlightthickness=0)
canvas1.create_image(width/2, height/2, image=imageVT1)
canvas1.grid(row=3, column=3, rowspan=4, padx=50, pady=10)

frame4=Frame(win)
frame4.grid(row=8, columnspan=4, rowspan=4, pady=15)

frame5 = Frame(win)
#frame5 ['bg'] = "orange"
frame5.grid(row=12, columnspan=4, rowspan=4, pady=25, padx=15)


############################################################
#RESULTATS de la requête
############################################################

def RESULTS():
    global conn, cursor, codeP, Nom
    lbl0 = Label(frame4, text="Voici les vétérinaires de votre région : ", fg="black", font="Verdana 18")
    lbl0.grid(row=1, column=2, pady=10, padx=10)
    codeP=Combo3.get()
    l=cursor.execute("SELECT nom, prenom FROM user WHERE type='staff' AND code = (?) ", [codeP])
    vetes=l.fetchall()
    Combo4 = ttk.Combobox(frame4, values=vetes, width=25)
    Combo4.set("Veuillez choisir")
    Combo4.grid(row=2, column=2, pady=10, padx=10)
    Combo4.bind('<<ComboboxSelected>>', lambda e: AFFICHE())

    def AFFICHE():
        Nom = Combo4.get()
        a=Combo1.get()
        b=Combo2.get()
        cursor.execute("SELECT adresse, code, ville, users_id FROM user WHERE nom = ? AND prenom = ? ", Nom.split(" "))
        rslt=cursor.fetchone()
        lbl1= Label(frame5, text="Vous avez sélectionné", fg="blue", font="Verdana 18")
        lbl1.grid(row=3, column=2, columnspan=3, pady=10, padx=10)
        lbl2 = Label(frame5, text=f"{Nom} {rslt[0]} {rslt[1]} {rslt[2]}", fg="grey", font="Verdana 18")
        lbl2.grid(row=4, column=2, pady=10, padx=10)
        lbl3 = Label(frame5, text=("Pour votre " + a + " pour  " + b ), fg="black", font="Verdana 18")
        lbl3.grid(row=5, column=2, pady=10, padx=10)

        def REQUETE(user_id):
            vt = Tk()
            vt.title("Planing Consultation")
            vt.geometry("1250x800+100+0")
            vt.minsize(480, 360)
            vt['bg'] = "orange"

            lbl_titre = Label(vt, text="Bienvenue dans l'application VT_ONLINE", fg="white", bg="grey",
                              font="Verdana 34")
            lbl_titre.pack()

            lbl_log = Label(vt, text="Introduisez le nom du vétérinaire :", fg="black", bg="orange", font="Verdana 22")
            lbl_log.place(x=50, y=100)
            entryLog = Entry(vt, font=('arial', 20), width=5)
            entryLog.place(x=460, y=100)


            # frameR = Frame(vt)
            # frameR.pack(side=RIGHT)
            # width = 500
            # height = 300
            # imageVT2 = PhotoImage(file="Image3.png").zoom(10).subsample(10)
            # canvas1 = Canvas(frameR, width=width, height=height, bg='orange', bd=0, highlightthickness=0)
            # canvas1.create_image(width / 2, height / 2, image=imageVT2)
            # canvas1.pack(padx=20)

            FrameL = Frame(vt)
            FrameL.pack(side=LEFT, pady=10, padx=50)

            lbl_sstitre = Label(vt, text="Choisissez vos jours de consultations et vos horaires", fg="black",
                                bg="orange", font="Verdana 22")
            lbl_sstitre.place(x=60, y=200)

            label = Label(FrameL, text="  AM  -  PM      ", font=("Arial", 20), bg="grey", fg="white")
            label.grid(row=0, column=2, columnspan=4, pady=10, padx=18)

            lbl1 = Label(FrameL, text="LUNDI", fg="black", font="Verdana 18")
            lbl1.grid(row=1, column=1, pady=10, padx=10)
            lbl2 = Label(FrameL, text="MARDI", fg="black", font="Verdana 18")
            lbl2.grid(row=2, column=1, pady=10, padx=10)
            lbl3 = Label(FrameL, text="MERCREDI", fg="black", font="Verdana 18")
            lbl3.grid(row=3, column=1, pady=10, padx=10)
            lbl4 = Label(FrameL, text="JEUDI", fg="black", font="Verdana 18")
            lbl4.grid(row=4, column=1, pady=10, padx=10)
            lbl5 = Label(FrameL, text="VENDREDI", fg="black", font="Verdana 18")
            lbl5.grid(row=5, column=1, pady=10, padx=10)

            lundi = (
                cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ",
                               ("LUNDI", user_id)).fetchone())
            mardi = (
                cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ",
                               ("MARDI", user_id)).fetchone())
            mercredi = (
                cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ",
                               ("MERCREDI", user_id)).fetchone())
            jeudi = (
                cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ",
                               ("JEUDI", user_id)).fetchone())
            vendredi = (
                cursor.execute("SELECT debut_AM, fin_AM, debut_PM,fin_PM FROM horaire WHERE (jour,users_id) = (?,?) ",
                               ("VENDREDI", user_id)).fetchone())

            lbl6 = Label(FrameL, text="", fg="black", font="Verdana 18")
            lbl6.grid(row=1, column=2, pady=10, padx=10)
            lbl6.config(text=f"{lundi[0]} {lundi[1]} {lundi[2]} {lundi[3]} ")

            lbl7 = Label(FrameL, text="", fg="black", font="Verdana 18")
            lbl7.grid(row=2, column=2, pady=10, padx=10)
            lbl7.config(text=mardi)

            lbl8 = Label(FrameL, text="", fg="black", font="Verdana 18")
            lbl8.grid(row=3, column=2, pady=10, padx=10)
            lbl8.config(text=mercredi)

            lbl9 = Label(FrameL, text="", fg="black", font="Verdana 18")
            lbl9.grid(row=4, column=2, pady=10, padx=10)
            lbl9.config(text=jeudi)

            lbl10 = Label(FrameL, text="", fg="black", font="Verdana 18")
            lbl10.grid(row=5, column=2, pady=10, padx=10)
            lbl10.config(text=vendredi)
            vt.mainloop()



        button_voir = Button(frame5, text="Prendre rendez-vous", command=lambda : REQUETE(rslt[3]), fg="blue", font="Verdana 12", bd=2,
                                    bg="light blue", relief="groove")
        button_voir.grid(row=4, column=3, padx=15, pady = 10)

        width = 80
        height = 90
        imageVT2 = PhotoImage(file="sihouette.png").zoom(15).subsample(10)
        canvas2 = Canvas(frame5, width=width, height=height, bg='grey', bd=1, highlightthickness=1)
        canvas2.create_image(width / 2, height / 2, image=imageVT2)
        canvas2.grid(row=3, column=1, rowspan=4, pady=10, padx = 20)


button_valider = Button(win, text="Valider", command=RESULTS, fg="blue", font="Verdana 16", bd=2, bg="light blue", relief="groove")
button_valider.grid(row=7, column=3, padx=15)


win.mainloop()
cursor.close()
conn.close()