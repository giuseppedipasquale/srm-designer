from numpy import pi


class Nozzle:
    """
    Class to represent a nozzle.
    """

    def __init__(self, dt, cf):
        """
        Constructor
        :param dt: Throat diameter dt [mm]
        :param cf: Thrust coefficient cf
        """
        self._dt = dt
        self._cf = cf

    @property
    def dt(self):
        """
        :return: throat diameter
        """
        return self._dt

    @property
    def cf(self):
        """
        :return: thrust coefficient
        """
        return self._cf

    @property
    def a_t(self):
        """
        :return: throat area
        """
        return pi/4*self.dt**2

