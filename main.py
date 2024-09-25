import numpy as np

class Jeu:
    """
    Jeu où le joueur doit deviner un nombre entre 0 et m tiré au hazard, en ayant n essais.
    """
    def __init__(self, m):
        """
        Initialise le jeu avec un nombre tiré au hasard entre 0 et m.
        
        doc test :
        >>> jeu = Jeu(10)
        >>> 0 <= jeu.k <= 10
        True
        """
        self.k = np.random.randint(m)