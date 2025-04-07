from controler import Controler

if __name__ == "__main__":
    FICHIER_JSON = "resultats.json"
    app = Controler(FICHIER_JSON)
    app.executer()