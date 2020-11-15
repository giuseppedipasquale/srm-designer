from numpy import pi


class Nozzle:
    """
    Class to represent a nozzle.
    """

    def __init__(self, d_t, C_f):
        """
        Constructor
        :param d_t: Throat diameter dt [mm]
        :param C_f: Thrust coefficient Cf
        """
        self._d_t = d_t
        self._C_f = C_f

    @property
    def d_t(self):
        """
        :return: throat diameter
        """
        return self._d_t

    @property
    def C_f(self):
        """
        :return: thrust coefficient
        """
        return self._C_f

    @property
    def a_t(self):
        """
        :return: throat area
        """
        return pi/4*self.d_t**2

