class Grain:
    """
    Class to represent a grain or set of propellant grains.
    """

    def __init__(self, propellant, d_ext, d_int, L, n, int_inhibit, ext_inhibit, lat_inhibit):
        """
        Constructor
        :param propellant: Propellant
        :param d_ext: External diameter [mm]
        :param d_int: Internal diameter [mm]
        :param L: Length of single grain [mm]
        :param n: Number of grains
        :param int_inhibit: Internal inhibit
        :param ext_inhibit: External inhibit
        :param lat_inihibit: Lateral inhibit
        """
        self._d_ext = d_ext
        self._d_int = d_int
        self._L = L
        self._n = n
        self._propellant = propellant
        self._int_inhibit = int_inhibit
        self._ext_inhibit = ext_inhibit
        self._lat_inhibit = lat_inhibit

    @property
    def d_ext(self):
        """
        :return: External grain diameter [mm]
        """
        return self._d_ext

    @property
    def d_int(self):
        """
        :return: Internal grain diameter [mm]
        """
        return self._d_int

    @property
    def L(self):
        """
        :return: Grain length L [mm]
        """
        return self._L

    @property
    def n(self):
        """
        :return: Number of grains
        """
        return self._n

    @property
    def propellant(self):
        """
        :return: Propellant
        """
        return self._propellant

    @property
    def int_inhibit(self):
        """
        :return: Internal inhibit
        """
        return self._int_inhibit

    @property
    def ext_inhibit(self):
        """
        :return: External inhibit
        """
        return self._ext_inhibit

    @property
    def lat_inhibit(self):
        """
        :return: Lateral inhibit
        """
        return self._lat_inhibit

    @property
    def L_tot(self):
        """
        :return: Total grains length
        """
        return self._n*self._L
