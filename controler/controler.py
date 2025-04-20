from view.view import View
from model.platine import Platine
import random
from time import sleep

#class contrôleur
class Controler:
    """gère les interactons entre l'utilisateur et l'application"""
    
    # avec paramètre fichier json: fichier json
    def __init__(self):
        self.vue = View()
        self.platine = Platine( 19, 26)
        start = True
        self.demar = True
        while self.demar:
            message = None
            while message == None:
                message = self.platine.start()
            if start:
                self.vue.afficher_message_LCD(0, 0, "Le système est démarré")
                sleep(2)
                start = False
            if message == "Fin":
                self.demar = False
                self.vue.afficher_message_LCD(0, 0, "Le système est en arrêt")
                sleep(2)
                self.platine.quitter()
                self.vue.clear_LCD()
            else :
                self.vue.clear_LCD()
                self.vue.afficher_message_LCD(0, 0, message[0])
                self.vue.afficher_message_LCD(0, 1, message[1])
        
            
            
            
        
        
        
    
    