from numpy import arange
from numpy import pi

class Motor:
    """
    Class to represent a full solid rocket motor.
    """

    def __init__(self, chamber, nozzle, grain):
        """
        Constructor
        :param chamber: chamber object
        :param nozzle: nozzle object
        :param grain: grain object
        """
        self._chamber = chamber
        self._nozzle = nozzle
        self._grain = grain

    @property
    def chamber(self):
        """
        :return: chamber object
        """
        return self._chamber

    @property
    def nozzle(self):
        """
        :return: nozzle object
        """
        return self._nozzle

    @property
    def grain(self):
        """
        :return: grain object
        """
        return self._grain

    def MEOP2d_t(self):
        """
        :return: nozzle.d_t in order to meet MEOP
        """
        x_end = (self.grain.d_ext-self.grain.d_int)/2
        x = arange(0, x_end, 0.1)
        d = self.grain.d_int + 2*x*self.grain.int_inhibit
        D = self.grain.d_ext - 2*x*self.grain.ext_inhibit
        L = self.grain.L_tot - 2*x*self.grain.n*self.grain.lat_inhibit
        A_int = self.grain.int_inhibit*pi*d*L
        A_ext = self.grain.ext_inhibit*pi*D*L
        A_lat = self.grain.lat_inhibit*(2*self.grain.n*pi/4)*(D**2-d**2)
        A_b = A_int+A_ext+A_lat
        KN_max = self.grain.propellant.KN_coef[0] + self.grain.propellant.KN_coef[1]*self.chamber.MEOP + self.grain.propellant.KN_coef[2]*self.chamber.MEOP**2
        A_t = max(A_b)/KN_max
        self.nozzle._d_t = (4*A_t/pi)

# todo implement method to compute pressure/thrust over time and other performance properties
