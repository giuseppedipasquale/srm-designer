class Propellant:
    """
    Generic class to represent a propellant.
    """

    def __init__(self, R, k):
        """
        Constructor
        :param R: gas constant [J/(kg*K)]
        :param k:
        """
        self._R = R
        self._k = k

    @property
    def R(self):
        """
        :return: gas constant
        """
        return self._R

    @property
    def k(self):
        """
        :return: specific heat coefficient
        """
        return self._k


class KNSU(Propellant):
    """
    Class to represent a KNSU.
    """

    def __init__(self):
        self._R = 198
        self._k = 1.139
        self._T = 1634
        self._rho = 1.795
        self._a = 8.26
        self._n = 0.319
        self._A = 32.954
        self._B = 44.108
        self._C = -1.1025
