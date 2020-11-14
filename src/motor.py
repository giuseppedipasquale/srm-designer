class Motor:
    """
    Class to represent a full solid rocket motor.
    """

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
