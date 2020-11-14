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
# todo add all remaining properties
# todo understand how to implement different propellants with minimal effort
