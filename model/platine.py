import threading
from time import sleep
from gpiozero import Button
from ADCDevice import *

class Platine:
    def __init__(self, bouton_demarrer, bouton_mesure):
        self.boutons = {"Demarrer":Button(bouton_demarrer),"Mesure":Button(bouton_mesure)}
        self.running = False
        self.demarrer_thread = threading.Thread(target=self.demarrer_button, daemon=True)
        self.demarrer = False
        self.fin = False
        self.adc = ADCDevice()
        if(self.adc.detectI2C(0x4b)):
            self.adc = ADS7830()
        else:
            print("Erreur : adresse I2C non trouvée")
            exit(-1)
    
    def start(self):
        if not self.running and self.boutons["Demarrer"].is_active:
            while self.boutons["Demarrer"].is_active:
                sleep(0.1)
            self.running = True
            self.demarrer_thread.start()
            return self.update()
        elif self.running:
            elapsed_time = 0
            while elapsed_time < 5:
                if self.boutons["Mesure"].is_active:
                    while self.boutons["Mesure"].is_active:
                        sleep(0.1)
                    elapsed_time = 0
                    return self.update()
                elif self.fin:
                    self.running = False
                    return "Fin"
                else:
                    sleep(0.1)
                    elapsed_time += 0.1
            return self.update() 

                
    def demarrer_button(self):
        while self.running:
            if self.boutons["Demarrer"].is_active:
                while self.boutons["Demarrer"].is_active:
                    sleep(0.1)
                self.fin = True
                

    
    def update(self):
        valeurADC = self.adc.analogRead(0)
        voltage = valeurADC / 255.0 * 3.3
        return {0:'ValeurADC: %d'%(valeurADC), 1:'Voltage : %.2f'%(voltage)}

    
    def quitter(self):
        for bouton in self.boutons.values():
            bouton.close()
        self.adc.close()
