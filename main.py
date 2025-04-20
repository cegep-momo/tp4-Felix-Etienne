from controler.controler import Controler

if __name__ == "__main__":
    try :
        FICHIER_JSON = "resultats.json"
        app = Controler(FICHIER_JSON)
    except KeyboardInterrupt :
        print("FIN")