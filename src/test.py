from src.srm.chamber import Chamber
from src.srm.motor import Motor
from src.srm.nozzle import Nozzle
from src.srm.grain import Grain
from src.srm.propellant import *

# cha = Chamber(75, 250, 6)
# noz = Nozzle(15, 1.5)
# knsu = Propellant(198, 1.13)
# gra = Grain(knsu, 69, 20, 120, 2, 1, 0, 0)

knsu = KNSU()
print(knsu.KN_coef)
print(knsu.n)
print(knsu.k)

# m = Motor(cha, noz, gra)
# print(m.chamber.lgt)
# print(m.nozzle.dt)
# print(m.grain.lgt)
# # todo test all changes
