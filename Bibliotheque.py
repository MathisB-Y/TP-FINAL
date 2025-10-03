import json
import csv
import os

class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def sauvegarder(self, fichier):
        try:
            data = [livre.__dict__ for livre in self.livres]
            with open(fichier, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print("Erreur de sauvegarde :", e)

    def charger(self, fichier):
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.livres = [Livre(**d) for d in data]
        except FileNotFoundError:
            print("Fichier introuvable.")
        except json.JSONDecodeError:
            print("Format JSON invalide.")
        except Exception as e:
            print("Erreur de chargement :", e)

    def exporter_csv(self, fichier):
        try:
            with open(fichier, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["titre", "auteur", "isbn"])
                writer.writeheader()
                for livre in self.livres:
                    writer.writerow(livre.__dict__)
        except Exception as e:
            print("Erreur d'export CSV :", e)


if __name__ == "__main__":
    biblio = Bibliotheque()


    biblio.ajouter_livre(Livre("Harry Potter", "J.K Rowling", "111"))
    biblio.ajouter_livre(Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "222"))


    dossier_script = os.path.dirname(os.path.abspath(__file__))

    chemin_json = os.path.join(dossier_script, "biblio.json")
    chemin_csv = os.path.join(dossier_script, "biblio.csv")


    biblio.sauvegarder(chemin_json)

    biblio.charger(chemin_json)

    biblio.exporter_csv(chemin_csv)