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
print(m.chamber.lgt)
print(m.nozzle.dt)
print(m.grain.propellant.R)
# todo test all changes
