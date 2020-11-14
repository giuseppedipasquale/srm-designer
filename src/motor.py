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

# todo implement method to calculate nozzle.throat_area from chamber.MEOP
# todo implement method to compute pressure/thrust over time and other performance properties