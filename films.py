from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

def ajouter():
    annee = entrerannee.get()
    films = entrerfilms.get()
    

    #Creeon la connexion
    con = sqlite3.connect('film.db')
    cuser = con.cursor()
    cuser.execute("insert into Films('annee','films') values (?,?)",(annee,films,))
    con.commit()
    con.close()
    messagebox.showinfo("Patient ajouter")

    #afficher
    con = sqlite3.connect('film.db')
    cuser = con.cursor()
    select = cuser.execute("select * from Films ")
    select = list(select)
    table.insert('',END,values = select[0])
    con.close()

def modifier():
        annee = entrerannee.get()
        films = entrerfilms.get()
    

        # Creeon la connexion
        con = sqlite3.connect('film.db')
        cuser = con.cursor()
        cuser.execute(
            "update Films set annee=?,film=?",
            (annee, film))
        con.commit()
        con.close()
        messagebox.showinfo("Modifier")

        # afficher
        con = sqlite3.connect('film.db')
        cuser = con.cursor()
        select = cuser.execute("select * from Films")
        select = list(select)
        table.insert('', END, values=select[0])
        con.close()


def supprimer():
    codeSelectionner = table.item(table.selection())['values'][0]
    con = sqlite3.connect("film.db")
    cuser = con.cursor()
    delete  =cuser.execute("delete from Films where code = {}".format(codeSelectionner))
    con.commit()
    table.delete(table.selection())



#titre general
root = Tk()
root.title("Classement et repertoire de film et serie ")
root.geometry("1300x700")


#Ajouter le titre
lbltitre = Label(root,bd = 20, relief = RIDGE, text = "Ici le meilleur site de classement de film", font = ("Arial", 30), bg = "red", fg="white")
lbltitre.place(x = 0, y = 0, width = 1365)

#Liste des Films
lblListefilm = Label(root, text = "LISTES DES Films ", font = ("Arial", 16), bg = "darkblue", fg="white")
lblListefilm.place(x=600,y=100,width=760)



#text annee
lblannee = Label(root, text = " annee de sortie ", font = ("Arial", 16), bg = "black", fg="white")
lblannee.place(x=0,y=100,width=200)
entrerannee = Entry(root)
entrerannee.place(x=200,y=100,width=160,height=30)

#text titre 
lblnom = Label(root, text = "Titre du films ou serie", font = ("Arial", 16), bg = "black", fg="white")
lblnom.place(x=0,y=150,width=200)
entrernom = Entry(root)
entrernom.place(x=200,y=150,width=200,height=30)


#Enregistrer
btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = ajouter)
btnenregistrer.place(x=30, y= 450, width=200)

#modifier
btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = modifier)
btnmodofier.place(x=270, y= 450, width=200)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = supprimer)
btnSupprimer.place(x=150, y= 500, width=200)



#Table
table = ttk.Treeview(root, columns = (1, 2, 3, 4, 5, 6, 7), height = 5, show = "headings")
table.place(x = 600,y = 150, width = 760, height = 450)

#Entete
table.heading(1 , text = "annee")
table.heading(2 , text = "titre")


#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 150)
table.column(3,width = 150)
table.column(4,width = 50)
table.column(5,width = 150)
table.column(6,width = 100)
table.column(7,width = 150)

# afficher les informations de la table
con =  sqlite3.connect('film.db')
cuser = con.cursor()
select = cuser.execute("select * from Films")
for row in select:
    table.insert('', END, value = row)
con.close()


root.mainloop()