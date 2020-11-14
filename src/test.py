from chamber import Chamber
from motor import Motor
c1 = Chamber(10, 20, 4)
m = Motor(c1)
print(m.chamber.d)
