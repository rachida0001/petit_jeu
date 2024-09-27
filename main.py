import random

class Jeu:
    """
    Jeu où le joueur doit deviner un nombre entre 0 et m tiré au hazard, en ayant n essais.
    """
    def __init__(self, m, n):
        """
        Initialise le jeu avec un nombre tiré au hasard entre 0 et m donnée.
        
        args :
            m : nombre entier pour difinir le nombre k 
            n : nombre d'essais
        
        doc test :
        >>> jeu = Jeu(10,5)
        >>> 0 <= jeu.k <= 10
        True
        """
        self.k = random.randint(0,m)
        self.n = n
        
    def test(self, k):
        """_summary_

        Args:
            k : un nombre entier pour le tester avec self.k

        Returns:
            True : si le nombre k est self.k sont egaux
            False : sinon
        
        doc test 2:
        >>> jeu = Jeu(10,5)
        >>> jeu.test(11)
        Trop grand !
        False
        """
        self.n -=1
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
        Demande au joueur un nombre jusqu'à ce qu'il trouve le bon si il deppasse les n essais il perde.
        """
        b = False
        while not(b):
            if(self.n==0):
                print("Tu as perdu !")
                break
            try :  
                k = int(input("Entre un nombre :"))
            except :
                print("Ceci n’est pas un entier !")  
            b = self.test(k)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    jeu = Jeu(10,5)
    #jeu.test(11)
    jeu.jouer()
    
    
    
   
    
