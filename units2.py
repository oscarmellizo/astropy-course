from astropy import units as unit
from astropy import constants as const

x = (3.0 * unit.kilometer / (130.51 * unit.meter / unit.second)).decompose()  
print(x)
x = 3.0 * unit.kilometer / (130.51 * unit.meter / unit.second)
print(x)


mass = 125000000 * unit.M_sun
mass2 = pow(mass, 2)
print(mass2)
mass2 = mass2.decompose()  
print(mass2)

G3 = pow(const.G, 3)
print(G3)
G3 = G3.decompose()  
print(G3)