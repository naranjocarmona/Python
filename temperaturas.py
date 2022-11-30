# Para obtener la fecha y hora actuales, importo la libreria datetime
from datetime import datetime

temperaturas = []
dia=1

# Bucle infinito hasta que escriba 100
while True:

    # Pregunto temp. min y max.
    # Para sustituir variables en el texto se pone una plantilla (%d)
    # Luego se especifica al final qué variable se va a usar para la sustitución (dia)
    temp_min=float(input("Día %d. Temperatura mínima: " % dia))
    # Si la minima es 100, termino el bucle
    if temp_min == 100:
        break

    temp_max=float(input("Día %d. Temperatura máxima: " % dia))
    # Si la maxima es 100, termino el bucle
    if temp_max == 100:
        break

    # Las guardo en muestra
    muestra = []
    muestra.append(temp_min)
    muestra.append(temp_max)

    # Y las añado a temperaturas
    temperaturas.append(muestra)

    # Aumento en 1 el día
    dia += 1

# Calculo el número de muestras. Número de posiciones que tiene el array temperaturas.
num_muestras = len(temperaturas)

# Calculo la fecha y hora actuales
fechaHora = datetime.now()

# Extraigo la fecha en el formato que necesito
fecha = fechaHora.strftime("%d-%m-%Y")

# Extraigo la hora en el formato que necesito
hora = fechaHora.strftime("%H:%M")

# Separo temperaturas minimas y maximas.
minimas = []
maximas = []
for muestra in temperaturas:
    minimas.append(muestra[0])
    maximas.append(muestra[1])

# Calculo media.
# Sumo todas las temperaturas (maximas y minimas) y divido entre numero de muestras x 2
# Multiplico por dos porque cada muestra tiene dos temperaturas (min y max).
suma = sum(minimas) + sum(maximas)
media = suma / (num_muestras * 2)

# Imprimo informe
print("Informe de temperaturas del Parque Natural de Doñana:")
print("Fecha: %s" % fecha)
print("Hora: %s" % hora)
print("Número de muestras: %d" % num_muestras)
print("Temperaturas tomadas: %s" % temperaturas)
print("Temperatura máxima: %f" % max(maximas))
print("Temperatura mínima: %f" % min(minimas))
print("Temperatura media: %f" % media)
