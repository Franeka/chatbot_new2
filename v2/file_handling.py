import json


class file_handling:
    def __init__(self, filepath):
        try:
            with open(filepath) as antworten:
                self.antworten = json.load(antworten)
        except FileNotFoundError:
            print("Datei nicht gefunden.")
        except AttributeError:
            print("Keine Daten vorhanden")

        self.reaktionen = self.antworten['reaktionen']
        self.zufallsantworten = self.antworten['zufallsantworten']

    # def getAntworten(self, type):
    #     if type == "zufall":
    #         return self.zufallsantworten
    #     elif type == "reaktion":
    #         return self.reaktionen
    #     else:
    #         return "Fehler"
