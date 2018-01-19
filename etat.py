#!/usr/bin/python3
import random
IS_MINIMISATION = False

# Dimension du problème.
DIMENSION = 1000

class Etat:
    def __init__(self, dim_etat):
        self.vecteur = []

    def init_aleatoire(self):
        """Initialisation aléatoire de l'état."""
        for i in range(DIMENSION):
            self.vecteur.append(random.randrange(2))
        pass
    
    def afficher(self):
        """Affichage."""
        return ""
    
    def generer_voisin(self):
        """Générer un état voisin."""
        self.old_index = random.randrange(len(self.vecteur))
        self.vecteur[self.old_index] = (self.vecteur[self.old_index]+1)%2
        pass
    
    def come_back(self):
        """Retour à l'état précédent."""
        self.vecteur[self.old_index] = (self.vecteur[self.old_index]+1)%2
        pass
    
    def calcul_critere(self, temperature_initiale, temperature):
        """Évaluation des objectifs."""
        return 0.0
