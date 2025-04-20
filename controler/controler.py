from view.view import View
from model.platine import Platine
import random
import time

#class contrôleur
class Controler:
    """gère les interactons entre l'utilisateur et l'application"""
    
    # avec paramètre fichier json: fichier json
    def __init__(self):
        self.vue = View()
        self.platine = Platine( 19, 26)
        self.vue.afficher_message_LCD(0, 0, "Lancement...")
        boucle = 0
        while True:
            message = None
            while message == None:
                message = self.platine.start()
            if boucle == 0:
                self.vue.afficher_message_LCD(0, 0, message[0])
                self.vue.afficher_message_LCD(0, 1, message[1])
                boucle = 1
            else:
                self.vue.clear_LCD()
                self.vue.afficher_message_LCD(0, 0, message[0])
                self.vue.afficher_message_LCD(0, 1, message[1])
            
            
        
        
        
    
    