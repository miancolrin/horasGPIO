# -*- coding: utf-8 -*-

# Programa para la Raspberry Pi de discriminación horaria
# Creado por @miancolrin

# Tenemos dos horarios: pico y valle
# En horarios pico el precio del kWh es de 0,16€
# En horarios valle el precio del kWh es de 0,06€
# Las horas valle son de 10:00 a 14:00 y de 19:00 a 23:00
# Este programa encenderá el GPIO 17 cuando estemos en horario valle
# Tambien se encenderá el GPIO 27 cuando estemos en horario pico
# GPIO 17 conectado a LED verde
# GPIO 27 conectado a LED rojo
# Cuando estemos en horario valle se abrirán los GPIO 4, 22, 18, 23, 24 y 25
# Estos GPIO estarán conectados a un relé, que se abrirá en horario valle
# Así aprovecharemos el bajo precio de la luz de forma automática

import RPi.GPIO as GPIO # Librería de los GPIO y la llamamos 'GPIO'
import time # Importamos el tiempo para la discriminación horaria

# Se establece el sistema de nueración de los GPIO a BCM
GPIO.setmode(GPIO.BCM)

# Se confirguran TODOS los GPIO como salida
GPIO.setup(17, GPIO.OUT) # LED verde
GPIO.setup(27, GPIO.OUT) # LED rojo
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

# Se declaran las variables de la hora, minuto y segundo
hora = time.strftime('%H')
minuto = time.strftime('%M')
segundo = time.strftime('%S')

# Bucle infinito que comprueba en qué horario estamos (pico o valle)
# Dentro del bucle se toman las medidas dependiendo del horario
while True:
    if int(hora) >= 10 and int(hora) <= 13:
        GPIO.output(17, GPIO.HIGH) # Encender LED verde
        GPIO.output(27, GPIO.LOW) # Apagar LED rojo
        GPIO.output(4, GPIO.HIGH) # Cerrar los relés para encender
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
    elif int(hora) >= 19 and int(hora) <= 22:
        GPIO.output(17, GPIO.HIGH) # Encender LED verde
        GPIO.output(27, GPIO.LOW) # Apagar LED rojo
        GPIO.output(4, GPIO.HIGH) # Cerrar los relés para encender
        GPIO.setup(22, GPIO.HIGH)
        GPIO.setup(18, GPIO.HIGH)
        GPIO.setup(23, GPIO.HIGH)
        GPIO.setup(24, GPIO.HIGH)
        GPIO.setup(25, GPIO.HIGH)
    else:
        GPIO.output(27, GPIO.HIGH) # Encender LED rojo
        GPIO.output(17, GPIO.LOW) # Apagar LED verde
        GPIO.output(4, GPIO.LOW) # Abrir los relés para apagar
        GPIO.setup(22, GPIO.LOW)
        GPIO.setup(18, GPIO.LOW)
        GPIO.setup(23, GPIO.LOW)
        GPIO.setup(24, GPIO.LOW)
        GPIO.setup(25, GPIO.LOW)
    time.sleep(60) # Hacer la comprobación cada minuto
