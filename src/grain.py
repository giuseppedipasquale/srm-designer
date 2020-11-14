class Grain:
    """
    Class to represent a grain or set of propellant grains.
    """

    def __init__(self, d_ext, d_int, lgt, n, prop):
        """
        Constructor
        :param d_ext: External diameter [mm]
        :param d_int: Internal diameter [mm]
        :param lgt: Length of single grain [mm]
        :param n: Number of grains
        :param prop: Propellant
        """
        self._d_ext = d_ext
        self._d_int = d_int
        self._lgt = lgt
        self._n = n
        self._prop = prop

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
    def lgt(self):
        """
        :return: Grain length [mm]
        """
        return self._lgt

    @property
    def n(self):
        """
        :return: Number of grains
        """
        return self._n

    @property
    def prop(self):
        """
        :return: Propellant
        """
        return self._prop