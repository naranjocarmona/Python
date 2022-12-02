# Importo librería random, para generar números aleatorios.
import random

# Para obtener la fecha y hora actuales, importo la libreria datetime
from datetime import datetime

# Declaro constante NUEVA_VARIANTE.
NUEVA_VARIANTE = "ccucggcgggca"
# Declaro longitud de ADN que se va a generar aleatoriamente.
LONGITUD_ADN = 16000000
# Declaro elementos ADN
ELEMENTOS = ["c", "u", "g", "a"]

# Pregunto código paciente
codigo_paciente = int(input("Código del paciente: " ))

# Calculo número de elementos
num_elementos = len(ELEMENTOS)

# range(inicio, fin, salto). Genera una secuencia desde inicio hasta fin - 1, de salto en salto.
# Ejemplo: range(0, 5, 1) genera desde 0 hasta 4, de 1 en 1 --> 0,1,2,3,4
#
# Itero de 0 a LONGITUD_ADN - 1 (LONGITUD_ADN veces) para calcular el ADN generado aleatoriamente.
adn_aleatorio = []
for i in range(0, LONGITUD_ADN, 1):

    # Genero un índice aleatorio para las letras, de 0 a 3.
    # random.randint(min, max) --> Devuelve un número entero aleatorio entre min y max,
    # ambos inclusive.
    indice_aleatorio = random.randint(0, num_elementos - 1)

    # Genero un elemento aleatorio y lo añado al ADN.
    adn_aleatorio.append(ELEMENTOS[indice_aleatorio])

# Pasar de la lista de adn aleatorio a una única cadena (string).
# Se puede hacer con join: "separador".join(lista).
# En este caso no quiero usar separador, así que pongo ""
adn_generado = "".join(adn_aleatorio)

# Compruebo si la nueva variante está contenida en el ADN generado.
resultado = ""
resultadoTupla = ""
if NUEVA_VARIANTE in adn_generado:
    resultado = "Positivo: Sí se encuentra restos de la variante COVID."
    resultadoTupla = "Positivo"
else:
    resultado = "Negativo: No se encuentra restos de la variante COVID."
    resultadoTupla = "Negativo"

# Calculo la fecha y hora actuales
fechaHora = datetime.now()

# Extraigo la fecha en el formato que necesito
fecha = fechaHora.strftime("%d-%m-%Y")

# Extraigo la hora en el formato que necesito
hora = fechaHora.strftime("%H:%M")

# Código de prueba para imprimir ADN generado
# print("=== ADN generado =======================================")
# print("%s" % adn_generado)
# print("========================================================")

# Imprimo informe
print("Informe de virus COVID:")
print("Fecha: %s" % fecha)
print("Hora: %s" % hora)
print("Código del paciente: %d" % codigo_paciente)
print("Resultado: %s" % resultado)

# Creo la tupla
tupla = (fecha, hora, codigo_paciente, resultadoTupla)

# Enviar la tupla a un fichero de texo.
# Abrir fichero en modo escritura (con w).
fw = open("cadenas.txt", "w")

# Escribir la tupla.
# Se usa un separador (en este caso, coma y espacio ", ") y se une cada elemento de la tupla
# con join.
fw.write(", ".join([str(valor) for valor in tupla]))

#Cerrar fichero.
fw.close()
