import datetime
import json
import os


class Mesure:
    def __init__(self, dataMesure, FICHIER_JSON):
        self.dateHeureMesure = datetime.datetime.now().isoformat()
        self.dataMesure = dataMesure
        self.FICHIER_JSON = FICHIER_JSON
    
    def __repr__(self):
        donnees = {
            "dateHeureMesure": self.dateHeureMesure,
            "dataMesure": self.dataMesure,
        }
        if os.path.exists(self.FICHIER_JSON):
            with open(self.FICHIER_JSON,"r+", encoding="utf-8") as f:
                file_data = json.load(f)
                file_data["resultats"].append(donnees)
                f.seek(0)
                json.dump(file_data, f, indent=4, ensure_ascii=False)

    def afficherMesure(self):
        message = {0:'ValeurADC: %d'%(self.dataMesure["valeurADC"]), 1:'Voltage : %.2f'%(self.dataMesure["voltage"])}
        return message