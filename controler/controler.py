from view.view import View
from model.platine import Platine
import random
from time import sleep

#class contrôleur
class Controler:
    """gère les interactons entre l'utilisateur et l'application"""
    
    # avec paramètre fichier json: fichier json
    def __init__(self, FICHIER_JSON):
        self.vue = View()
        self.platine = Platine( 19, 26, FICHIER_JSON)
       
        start = True
        self.demar = True

        while self.demar:
            message = None
            while message == None:
                message = self.platine.start()
            if start:
                self.vue.afficher_message_LCD(0, 0, "Le systeme")
                self.vue.afficher_message_LCD(1, 1, "est demarre")
                sleep(2)
                self.vue.clear_LCD()
                start = False
            if message == False:
                self.vue.clear_LCD()
                self.demar = False
                self.vue.afficher_message_LCD(0, 0, "Le systeme")
                self.vue.afficher_message_LCD(1, 1, "est en arret")
                sleep(2)
                self.platine.quitter()
                self.vue.clear_LCD()
            elif message != None:
                self.vue.clear_LCD()
                self.vue.afficher_message_LCD(0, 0, message[0])
                self.vue.afficher_message_LCD(0, 1, message[1])
        
            
            
            
        
        
        
    
    