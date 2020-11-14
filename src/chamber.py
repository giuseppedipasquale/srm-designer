from numpy import pi


class Chamber:
    """
    Class to represent a solid rocket motor chamber.
    """

    def __init__(self, d, lgt, meop):
        """
        Constructor
        :param d: Diameter of chamber [mm]
        :param lgt: Length of chamber [mm]
        :param meop: Maximum expected operating pressure [MPa]
        """
        self._d = d
        self._lgt = lgt
        self._meop = meop

    @property
    def d(self):
        """
        :return: Chamber diameter d
        """
        return self._d

    @property
    def lgt(self):
        """
        :return: Chamber length lgt
        """
        return self._lgt

    @property
    def meop(self):
        """
        :return: Maximum Expected Operating Pressure meop
        """
        return self._meop

    @property
    def v(self):
        """
        :return: Chamber volume v
        """
        return pi / 4 * self.lgt * self.d ** 2
