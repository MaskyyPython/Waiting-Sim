# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import PIL.Image # gestion d'images
from PIL import ImageTk
from File import *
# import File

# Fênetre et sa création
root = Tk()
root.title("Waiting Simulator | v1.0")
root.resizable(height=False, width=False)
screen_x = int(root.winfo_screenwidth())
screen_y = int(root.winfo_screenheight())
window_x = 1280
window_y = 720

posX = (screen_x // 2) - (window_x // 2) # positionnement de l'écran
posY = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
root.geometry(geo)

FilesAttentes = FileAttente(5) # 5 files par défaut

def gererBouton(): # gestion pour savoir le role de l'utilisateur
    global lb1
    if choix_job.get() == "Client":
        FilesAttentes.gererClient(lb1)
    elif choix_job.get() == "Guichetier":
        FilesAttentes.gererGuichetier(lb1, tLabel)
    else:
        FilesAttentes.gererAdmin(lb1)

def actuListe(): # Fonction pour recharger la liste
    lb1.delete(0, END)
    for service_num, service in FilesAttentes.nbPersonne.items():
        for client in service.serv:
            lb1.insert(END, f"{client[0]} {client[1]} (Service {service_num})")


# Genere le cadre de la liste d'attente : En haut a gauche
cadreListe = Frame(root, bd = 2, relief = "solid")
nblabel1 = Label(cadreListe, text="Liste d'attente", font=("Arial", 18))
cadreListe.grid(row = 0, column = 1, padx = (50,0), ipadx=0)
lb1 = Listbox(cadreListe, font=("Arial", 12))

lb1.grid(row=1, column=0, ipadx=20)
nblabel1.grid(row = 0, column = 0)

userButton = Button(cadreListe, text="Reset", font=("Arial", 18), command=actuListe)
userButton.grid(row = 2, column = 0, pady = (0, 25))

# Genere le cadre du ChatBot : En haut au milieu
cadrePerso = Frame(root, bd = 2, relief = "solid")
nblabel2 = Label(cadrePerso, text="Cadre du Conseiller", font=("Arial", 18))
cadrePerso.grid(row = 0, column = 2, padx = 85)
nblabel2.grid(row = 0, column = 0)

# Transformation de l'image pour être utilisable sur Tkinter
chatbot = PIL.Image.open("images/secretaire.png")
chatbot = ImageTk.PhotoImage(master=cadrePerso, image=chatbot)

chatbotImage = Label(cadrePerso, image=chatbot)
chatbotImage.grid(row = 1, column = 0)

# Liste de choix entre différents rôles
choix_job = ttk.Combobox(root, state="readonly", font=("Arial", 18))
choix_job['values']=("Admin", "Guichetier", "Client")
choix_job.current(2)
choix_job.grid(row=3, column=2)


# Genere le cadre qui affiche le client appelé : En haut à droite
cadreTicket = Frame(root, bd = 2, relief = "solid")
nblabel3 = Label(cadreTicket, text="Client appelé", font=("Arial", 18))
tLabel = Label(cadreTicket, text="Nom :\nPrénom :\nService :", font=("Arial", 16))
cadreTicket.grid(row = 0, column = 3, padx= (0, 50))
nblabel3.grid(row = 0, column = 0)
tLabel.grid(row=1, column=0)

# Bouton pour confirmer le rôle de l'utilisateur
jobButton = Button(root, text="✅", font=("Arial", 18), command=gererBouton)
jobButton.grid(row = 4, column = 2, pady = (0, 25))

root.mainloop()