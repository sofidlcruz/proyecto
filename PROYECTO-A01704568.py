"""
Sofía de la Cruz Vázquez - A01704568
Examen sobre cultura general en México.
El examen trata sobre información cultura general México donde se harán preguntas de
conocimiento general sobre pueblos mágicos, economía, historia, atracciones regionales, 
además de evaluación sobre información básica de la económica del país.
El programa esta diseñado para ser contestado de manera dinámica para contestarlo 
por medio de preguntas abiertas. Las respuestas del usuario se compararán
con las respuestas correctas.Al final de cada preguntara se le dará al usuario la respuesta correcta.
Al final se dara el puntaje total con la calificación correspondida.

"""
import math

# entrada a nombre
usuario = str(input("Porfavor introduce tu nombre: "))
# imprime bienvenida
print("Hola", usuario,
      "bienvenido al examen de conocimiento turistico en México \na continuación visualizaras las preguntas y "
      "consecutivamente encontraras \npreguntas de opción multiple o preguntas abiertas. En las preguntas de escribir "
      "\ningresa su respuesta en minuscula y sin acentos.")


def respuestacorrecta():
    print("Tu respuesta es correcta")


def enter():
    espacio = input("\n\npresiona enter para continuar\n\n")

def iva_dulce(dulce, iva):
    porcentaje = dulce * iva
    return porcentaje + dulce


r1 = (iva_dulce(35, 0.16))
p1 = float(input("Si compras un dulce en la tienda y su valor es de $35 + iva ¿Cuál sera su precio total?"))
diferencia = p1 - r1
if r1 != p1:
    print("Respuesta incorrecta, tu resultado vario en: ", diferencia)
else:
    respuestacorrecta()

# espacio
enter()


# Operación con uso de operadores
def cambio(dolar, ext):
    presupuesto = ext * dolar
    return presupuesto - cambio


r2 = (iva_dulce(20.19, 87))
dolar = float(input(
    "Imagina que vienes de visita a México y tienes de presupuesto 87 dolares para gastar por día \n¿Cuanto dinero "
    "tienes al día para gastar en pesos? \nNOTA: el precio del dolar es de 20.19 pesos mexicanos?\n "))
diferencia = dolar - r2

if r2 != dolar:
    print("Respuesta incorrecta, tu resultado vario en: ", diferencia)
else:
    respuestacorrecta()

# espacio
enter()
# espacio

mont = str(input("¿Cual es la capital de Nuevo León? "))

if mont == "monterrey":
    respuestacorrecta()
else:
    print("Respuesta incorrecta, la respuesta correcta es monterrey")

# espacio
enter()
# espacio

p4 = float(input("¿En que año se fundo la Constitución que rige en la actualidad a México?"))
if p4 == 1917:
    print("Correcto")
else:
    print("Respuesta incorrecta, la respuesta correcta es 1917")

# espacio
enter()
# espacio


p5 = int(input("¿Cuál es el año de la Revolución mexicana, si es la raiz cuadrada de 3648100?"))
r5 = (math.sqrt(3648100))
diferencia = p5 - r5
if p5 == r5:
    print("Respuesta incorrecta, tu resultado vario en: ", diferencia)
else:
    respuestacorrecta()

#fin del programa