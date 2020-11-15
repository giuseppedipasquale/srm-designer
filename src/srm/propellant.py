class Propellant:
    """
    Generic class to represent a propellant.
    """

    def __init__(self, R, k, T, rho, a, n, KN_coef):
        """
        Constructor
        :param R: Gas constant [J/(kg*K)]
        :param k: Specific heat ratio
        :param T: Temperature [K]
        :param rho: Propellant solid density [g/cm^3]
        :param a: Pressure coefficient [mm/s]
        :param n: Pressure exponent
        :param KN_coef: KN coefficients
        """
        self._R = R
        self._k = k
        self._T = T
        self._rho = rho
        self._a = a
        self._n = n
        self._KN_coef = KN_coef

    @property
    def R(self):
        """
        :return: Gas constant
        """
        return self._R

    @property
    def k(self):
        """
        :return: Specific heat ratio
        """
        return self._k

    @property
    def T(self):
        """
        :return: Temperature [K]
        """
        return self._T

    @property
    def rho(self):
        """
        :return: Propellant solid density [g/cm^3]
        """
        return self._rho

    @property
    def a(self):
        """
        :return: Pressure coefficient [mm/s]
        """
        return self._a

    @property
    def n(self):
        """
        :return: Pressure exponent
        """
        return self._n

    @property
    def KN_coef(self):
        """
        :return: KN coefficients
        """
        return self._KN_coef


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
        self._KN_coef = [32.954, 44.108, -1.1025]
