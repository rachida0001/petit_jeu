import numpy as np
import random

class Jeu:
    """
    Jeu où le joueur doit deviner un nombre entre 0 et m tiré au hazard, en ayant n essais.
    """
    def __init__(self, m):
        """
        Initialise le jeu avec un nombre tiré au hasard entre 0 et m donnée.
        
        doc test :
        >>> jeu = Jeu(10)
        >>> 0 <= jeu.k <= 10
        True
        """
        self.k = random.randint(0,m)
        
    def test(self, k):
        """_summary_

        Args:
            k : un nombre entier pour le tester avec self.k

        Returns:
            True : si le nombre k est self.k sont egaux
            False : sinon
        
        doc test 2:
        >>> jeu = Jeu(10)
        >>> jeu.test(11)
        Trop grand !
        False
        """
        if self.k<k :
            print("Trop grand !")
            return False
        elif(self.k>k):
            print("Trop petit !")
            return False
        else:
            print("Bravo, tu as gagné !")
            return True
        
    def jouer(self):
        """
        Demande au joueur un nombre jusqu'à ce qu'il trouve le bon.
        """
        b = False
        while not(b):
            k = int(input("Entre un nombre :"))
            b = self.test(k)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    jeu = Jeu(10)
    jeu.test(11)
    jeu.jouer()
    
    
    
   
    
