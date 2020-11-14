from numpy import pi

class Chamber:
    """
    Class to represent a solid rocket motor chamber.
    """

    def __init__(self, D, L, MEOP):
        """
        Constructor
        :param D: Diameter of chamber [mm]
        :param L: Length of chamber [mm]
        :param MEOP: Maximum expected operating pressure [MPa]
        """
        self._D = D
        self._L = L
        self._MEOP = MEOP

    @property
    def D(self):
        return self._D

    @property
    def L(self):
        return self._L

    @property
    def MEOP(self):
        return self._MEOP

    @property
    def V(self):
        return pi / 4 * self.L * self.D ** 2
