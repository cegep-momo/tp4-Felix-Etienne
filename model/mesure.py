import datetime
from view.ADCDevice import *


class Mesure:
    def __init__(self,dataMesure):
        self.dateHeureMesure = datetime.datetime.now().isoformat()
        self.dataMesure = dataMesure
    
    def __repr__ (self):
        message = self.dateHeureMesure + self.dataMesure
        return message

    def afficherMesure(self):
        message = self.dateHeureMesure + self.dataMesure
        return message