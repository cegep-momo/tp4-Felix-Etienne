from controler.controler import Controler

if __name__ == "__main__":
    try :
        FICHIER_JSON = "resultats.json"
        app = Controler()
    except KeyboardInterrupt :
        print("FIN")