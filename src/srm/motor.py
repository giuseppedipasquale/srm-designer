from numpy import arange, sqrt, zeros, pi
import matplotlib.pyplot as plt


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
        x_end = (self.grain.d_ext - self.grain.d_int) / 2
        x = arange(0, x_end, 0.1)
        d = self.grain.d_int + 2 * x * self.grain.int_inhibit
        D = self.grain.d_ext - 2 * x * self.grain.ext_inhibit
        L = self.grain.L_tot - 2 * x * self.grain.n * self.grain.lat_inhibit
        A_int = self.grain.int_inhibit * pi * d * L
        A_ext = self.grain.ext_inhibit * pi * D * L
        A_lat = self.grain.lat_inhibit * (2 * self.grain.n * pi / 4) * (D ** 2 - d ** 2)
        A_b = A_int + A_ext + A_lat
        KN_max = self.grain.propellant.KN_coef[0] + self.grain.propellant.KN_coef[1] * self.chamber.MEOP + \
                 self.grain.propellant.KN_coef[2] * self.chamber.MEOP ** 2
        A_t = max(A_b) / KN_max
        self.nozzle._d_t = (4 * A_t / pi) ** 0.5

    def compute_p(self):
        """
        :return: Calculates pressure over time
        """
        k = self.grain.propellant.k
        T0 = self.grain.propellant.T
        R = self.grain.propellant.R
        dx = 0.02
        x_end = (self.grain.d_ext - self.grain.d_int) / 2
        x = arange(0, x_end, dx)
        d = zeros(len(x))
        D = zeros(len(x))
        L = zeros(len(x))
        t = zeros(len(x))
        r = zeros(len(x))
        p = zeros(len(x))
        m_gen = zeros(len(x))
        m_noz = zeros(len(x))
        m_sto = zeros(len(x))
        mass_sto = zeros(len(x))
        rho_prod = zeros(len(x))
        d[0] = self.grain.d_int
        D[0] = self.grain.d_ext
        L[0] = self.grain.L
        for i in range(1, len(x)):
            d[i] = d[i - 1] + 2 * dx * self.grain.int_inhibit
            D[i] = D[i - 1] - 2 * dx * self.grain.ext_inhibit
            L[i] = L[i - 1] - 2 * dx * self.grain.n * self.grain.lat_inhibit
        A_star = self.nozzle.a_t
        V_grain = pi / 4 * (D ** 2 - d ** 2) * L
        V_free = (self.chamber.V - V_grain) / 1000 ** 3
        m_grain = self.grain.propellant.rho * V_grain / 1000 ** 2
        p[0] = 0.101
        r[0] = self.grain.propellant.a * p[0] ** self.grain.propellant.n
        for i in range(1, len(x)):
            r[i] = self.grain.propellant.a * p[i - 1] ** self.grain.propellant.n
            t[i] = t[i - 1] + dx / r[i]
            m_gen[i] = (m_grain[i - 1] - m_grain[i]) / (t[i] - t[i - 1])
            m_noz[i] = ((p[i - 1] - 0.101) * 1000000 * A_star / sqrt(R * T0)) * sqrt(k) * (2 / (k + 1)) ** (
                    (k + 1) / (2 * (k - 1)))
            m_sto[i] = m_gen[i] - m_noz[i]
            if m_sto[i] * (t[i] - t[i - 1]) + mass_sto[i - 1] < 0:
                mass_sto[i] = 0
            else:
                mass_sto[i] = mass_sto[i - 1] + m_sto[i] * (t[i] - t[i - 1])
            rho_prod[i] = mass_sto[i] / V_free[i]
            p[i] = (rho_prod[i] * R * T0 + 1e6 * 0.101) / 1e6 # To be commented

        plt.plot(t, p)
        plt.show()
