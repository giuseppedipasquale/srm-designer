from src.srm.chamber import Chamber
from src.srm.motor import Motor
from src.srm.nozzle import Nozzle
from src.srm.grain import Grain
from src.srm.propellant import Propellant

cha = Chamber(75, 250, 6)
noz = Nozzle(15, 1.5)
knsu = Propellant(198, 1.13)
gra = Grain(69, 20, 120, 2, knsu)

m = Motor(cha, noz, gra)
print(m.chamber.lgt)
print(m.nozzle.dt)
print(m.grain.lgt)
# todo test all changes
