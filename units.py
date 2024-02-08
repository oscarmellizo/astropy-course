from astropy import units as u

distancia = 14512 * u.meter
tiempo = 3.46 * u.second

velocidad = distancia / tiempo
print(velocidad)
velocidadKH = velocidad.to("km/h")

print(velocidadKH)