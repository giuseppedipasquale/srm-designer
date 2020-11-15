from src.srm.chamber import Chamber
from src.srm.motor import Motor
from src.srm.nozzle import Nozzle
from src.srm.grain import Grain
from src.srm.propellant import *

cha = Chamber(75, 250, 6)
noz = Nozzle(15, 1.5)
knsu = KNSU()
gra = Grain(knsu, 69, 20, 120, 2, 1, 0, 0)


m = Motor(cha, noz, gra)
print(m.chamber.L)
print(m.nozzle.d_t)
m.MEOP2d_t()
print(m.grain.propellant.R)
print(m.nozzle.d_t)
# todo test all changes
