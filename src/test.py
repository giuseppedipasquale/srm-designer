from src.srm.chamber import Chamber
from src.srm.motor import Motor
from src.srm.nozzle import Nozzle
from src.srm.grain import Grain
from src.srm.propellant import KNSU

# In order to test the srm-designer, it is necessary to create a chamber of pressure
# with a give external diameter [mm], lenght [mm] and Maximum Expected Operating Pressure [MPa]
cha = Chamber(75, 250, 6)
# Then it is necessary to have a nozzle, with a throat diameter [mm] and a thrust coefficent.
# It is possible to calculate the nozzle diameter for a given MEOP, once the motor class is created.
noz = Nozzle(15, 1.5)
# A propellant is necessary for the grain object. In this case a KNSU propellant is used.
knsu = KNSU()
# A grain object is created passing as arguments the external diameter [mm], the internal diameter [mm],
# the single grain length [mm], the number of grains and finally if the internal/external/later surfaces
# of the grain are exposed (1) or not (0).
gra = Grain(knsu, 69, 20, 120, 2, 1, 0, 0)

# Finally a motor class can be created, using the chamber, nozzle and grain classes created previously.
m = Motor(cha, noz, gra)

print(m.chamber.L)
print(m.nozzle.d_t)
# The MEOP2d_t takes the MEOP of the chamber and calcualtes the nozzle throat diameter to obtain said MEOP
# and updates the diameter of the nozzle so that the MEOP is met.
m.MEOP2d_t()
print(m.grain.propellant.R)
print(m.nozzle.d_t)
# The compute_p method calculates the pressure over time and plots it.
m.compute_p()
# todo test all changes
