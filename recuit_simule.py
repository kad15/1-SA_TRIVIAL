#!/usr/bin/python3
import math
import random
import etat


NB_TRANSITIONS = 2000
ALPHA = .995


class Recuit:
    def _accept(self, yi, yj, temperature):
        """Principe d'acceptation en maximisation.
        
        ????????????????
        ? À compléter. ?
        ????????????????
        """

        res = False
        # if(MINIMISATION):
        if True:
            if yj < yi:
                res = True
            else:
                    proba = math.exp((yj-yi)/temperature)
                    tirage = random.random()
                    if(tirage < proba):
                        res = True

        return res
    
    
    def heat_up_loop(self):
        """Détermine la température initiale."""
        
        temperature = 0.01
        taux_acceptation = 0.0
        
        xi = etat.Etat(etat.DIMENSION)
        
        while taux_acceptation < 0.8:
            accept_count = 0
            
            for i in range(NB_TRANSITIONS):
                # Génération d'un point de l'espace d'état.
                xi.init_aleatoire()
                yi = xi.calcul_critere(temperature, temperature)
                
                xi.generer_voisin()
                yj = xi.calcul_critere(temperature, temperature)
                
                if self._accept(yi, yj, temperature):
                    accept_count += 1
                    
            taux_acceptation = accept_count / NB_TRANSITIONS
            temperature *= 1.1
        
        return temperature
    
    
    def cooling_loop(self, temperature_initiale):
        """Processus de refroidissement."""
        
        temperature = temperature_initiale
        
        xi = etat.Etat(etat.DIMENSION)
        xi.init_aleatoire()
        yi = xi.calcul_critere(temperature_initiale, temperature)
        
        while temperature > 0.0001 * temperature_initiale:
            for i in range(NB_TRANSITIONS):
                xi.generer_voisin()
                yj = xi.calcul_critere(temperature_initiale, temperature)
                
                if self._accept(yi, yj, temperature):
                    yi = yj
                else:
                    xi.come_back()
                    
            temperature *= ALPHA
            
            print("Température : ", temperature, ", valeur du critère : ", yi)
            print(xi.afficher())
        

if __name__ == "__main__":
    recuit = Recuit()
    
    print("Chauffage.")
    temperature_initiale = recuit.heat_up_loop()
    
    print("Refroidissement")
    recuit.cooling_loop(temperature_initiale)
    
    
    
