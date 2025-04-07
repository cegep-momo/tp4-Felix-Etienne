from time import sleep
from gpiozero import RGBLED, Button
import LCD1602

class Platine:
    def __init__(self, rouge, vert, bleu, bouton_rouge,bouton_green,bouton_blue,bouton_Magenta):
        self.LED = RGBLED(red = rouge, green=vert, blue=bleu, active_high=False)
        self.boutons = {"Rouge":Button(bouton_rouge),"Vert":Button(bouton_green),"Bleu":Button(bouton_blue),"Magenta":Button(bouton_Magenta)}
        LCD1602.init(0x27, 1)
        
    def afficher_message_LCD(self, x, y, message):
        LCD1602.write(x, y, message)
        
    def clear_LCD(self):
        LCD1602.clear()
            
    def quitter(self):
        self.LED.color = (0, 0, 0) 
        for bouton in self.boutons.values():
            bouton.close()
        LCD1602.clear() 
