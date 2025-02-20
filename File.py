# -*- coding: utf-8 -*-

"""
Une liste de type File a pour but de faire "partir" / defiler le 1er element
qui est rentré dans ce tableau.
"""
from tkinter import *
class Service:
    def __init__(self):
        self.serv = []
    def est_file_vide(self):
        """ Vérifie si la file d'attente est vide. """    
        if len(self.serv) == 0:
            return True
        else:
            return False
       
    def enfiler(self, e):
        """ Ajoute une personne dans la file d'attente """
        self.serv.append(e)
   
    def defiler(self):
        """ Enlève la 1ere personne de la file d'attente """
        if len(self.serv) >= 1:
            print(self.serv[0])
            self.serv.pop(0)
        else:
            return "La File est vide." 
    def afficher(self):
        print(self.serv)

class FileAttente: # GERE TOUS LES SERVICES
    def __init__ (self, nbServ):     # constructeur d’une file vide
        self.nbServ = nbServ
        self.nbPersonne = {i+1 : Service() for i in range(self.nbServ)}
    
    def actu(self, lb1):
        """
        Actualise la file lorsque quelqu'un est ajouté/retiré
        """
        lb1.delete(0, END)
        for service_num, service in self.nbPersonne.items():
            for client in service.serv:
                lb1.insert(END, f"{client[0]} {client[1]} (Service {service_num})")  # Ferme la popup après validation


    def gererClient(self, lb1):
        """ Ouvre une popup pour demander les informations du client """
        
        def submitClient(lb1):
            """Récupère le nom, prénom, et le service demandé lorsque le client confirme"""
            nom = entry_nom.get()
            prenom = entry_prenom.get()
            service = int(service_var.get())
            if nom != "" and prenom != "": # Verifier si nom/prénom est vide
                
                self.nbPersonne[service].enfiler((nom, prenom))
                # print(f"Client ajouté: {nom} {prenom}, Service: {service}")
                popup.destroy()
                self.actu(lb1)
            else:
                Label(popup, text="Nom/Prénom invalide",font = ("Arial", 11)).grid(row=4, column=1)

        # Création de la popup
        popup = Toplevel()
        popup.geometry("400x400")
        popup.title("Gérer Client")
        
        # Widgets de la popup pour saisir les infos
        Label(popup, text="Nom:",font = ("Arial", 18)).grid(row=0, column=0)
        entry_nom = Entry(popup,font = ("Arial", 18))
        entry_nom.grid(row=0, column=1)

        Label(popup, text="Prénom:",font = ("Arial", 18)).grid(row=1, column=0)
        entry_prenom = Entry(popup,font = ("Arial", 18))
        entry_prenom.grid(row=1, column=1)

        Label(popup, text="Service:",font = ("Arial", 18)).grid(row=2, column=0)
        service_var = StringVar(popup)
        servListe = [i for i in self.nbPersonne.keys()]
        service_var.set(str(servListe[0]))
        service_menu = OptionMenu(popup, service_var, *servListe)
        service_menu.grid(row=2, column=1)

        Button(popup, text="Valider", command=lambda: submitClient(lb1), font=("Arial", 18)).grid(row=3, column=1)

            
    def gererGuichetier(self, lb1, t): # Liste + label comme arguments
        """ Ouvre une popup pour choisir un service et 
        afficher le premier client de la file d'attente """

        # Création de la popup
        popup = Toplevel()
        popup.geometry("400x400")
        popup.title("Gérer Guichetier")
        
        Label(popup, text="Mot de passe:",font = ("Arial", 18)).grid(row=1, column=0)
        entry_m = Entry(popup,font = ("Arial", 18))
        entry_m.grid(row=2, column=0)
        
        
        Label(popup, text="Sélectionnez le service:",font = ("Arial", 18)).grid(row=3, column=0)
        service_var = StringVar(popup)
        servListe = [i for i in self.nbPersonne.keys()]
        service_var.set(str(servListe[0]))
        service_menu = OptionMenu(popup, service_var, *servListe)
        service_menu.grid(row=4, column=1)

        Button(popup, text="Valider", command=lambda: self.afficheur(lb1, service_var, entry_m, popup, t)).grid(row=5, column=1)



    def gererAdmin(self, lb1):
        def ajouterService(lb1=lb1):
            self.nbServ += 1
            self.nbPersonne[self.nbServ] = Service()
            # print(f"Nouveau service ajouté : Service {self.nbServ}")
            popup.destroy()
            self.actu(lb1)

        def retirerService(lb1=lb1):
            service_to_remove = int(service_var.get())
            if service_to_remove in self.nbPersonne:
                del self.nbPersonne[service_to_remove]
                # print(f"Service {service_to_remove} retiré.")
                self.actu(lb1)
                popup.destroy()
            else:
                print("Service invalide.")

        # Création de la popup
        popup = Toplevel()
        popup.geometry("800x300")
        popup.title("Gérer les services")

        Label(popup, text="Voulez-vous ajouter ou retirer un service ?", font=("Arial", 18)).grid(row=0, column=0, columnspan=2)

        # Boutons pour ajouter ou retirer un service
        Button(popup, text="Ajouter un service", font=("Arial", 18), command=ajouterService).grid(row=1, column=0)

        Label(popup, text="Numéro du service à retirer :", font=("Arial", 18)).grid(row=2, column=0)
        service_var = StringVar(popup) # Variable de la valeur choisie
        servListe = [i for i in self.nbPersonne.keys()] # Liste de tous les noms de services
        service_var.set(str(servListe[0])) # Valeur par défaut
        service_menu = OptionMenu(popup, service_var, *servListe)
        service_menu.grid(row=3, column=0)

        Button(popup, text="Retirer un service", font=("Arial", 18), command=retirerService).grid(row=4, column=1)

    
    def afficheur(self, lb1, service_var, entry_m, popup, t):
        service = int(service_var.get())
        mdp = entry_m.get()
        if len(self.nbPersonne[service].serv) > 0 and mdp == "admin1234":
            client = self.nbPersonne[service].serv[0]  # Récupère le premier client dans la file
            print(f"Guichetier pour le Service {service}, Premier client: {client[0]} {client[1]}")
            tlabel = f"Nom:{client[0]}\nPrénom:{client[1]}\nService:{service}"
            t.config(text=tlabel)
            self.nbPersonne[service].defiler()  # Retire le client de la file
            #"popup.destroy()
            self.actu(lb1)
            
        elif mdp != "admin1234":
            Label(popup, text="Mauvais mot de passe", font=("Arial", 11)).grid(row=5, column=0)
        else:
            #print(f"Le service {service} n'a pas de clients en attente.")
            Label(popup, text="Il n'y a personne sur ce service", font=("Arial", 18)).grid(row=6, column=0)

    
    
