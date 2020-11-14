class Motor:
    """
    Class to represent a full solid rocket motor.
    """
# todo add nozzle, grain as parameters in constructor
    def __init__(self, chamber):
        """
        Constructor
        :param chamber: chamber object
        """
        self._chamber = chamber

    @property
    def chamber(self):
        """
        :return: chamber object
        """
        return self._chamber
# todo implement nozzle and grain as property
# todo implement method to calculate nozzle.throat_area from chamber.MEOP
# todo implement method to compute pressure/thrust over time and other performance properties