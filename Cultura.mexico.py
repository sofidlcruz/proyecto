"""
Sofía de la Cruz Vázquez - A01704568
Examen sobre cultura general en México.
El examen trata sobre información cultura general México donde se harán preguntas de
conocimiento general sobre pueblos mágicos, economía, historia, atracciones regionales, 
además de evaluación sobre información básica de la económica del país.
El programa esta diseñado para ser contestado de manera dinámica para contestarlo 
por medio de preguntas abiertas. Las respuestas del usuario se compararán
con las respuestas correctas y no avanzara a la siguiente pregunta de operación hasta que
se ingrese la respuesta correcta(se le dara la diferencia del error).
Al final de cada preguntara se le dará al usuario la respuesta correcta.

"""
import math
#inicio funciones
def respuestacorrecta():
    print("Tu respuesta es correcta")
    
def incorrecta(n):
    print("Respuesta es incorrecta. Tu respuesta vario en un:", n)

def enter():
    espacio = input("\n\npresiona enter para continuar\n\n")

def iva_dulce(dulce, iva):
    porcentaje = dulce * iva
    return porcentaje + dulce

def diferencia(num1,num2):
    dif = num1 - num2
    return dif

def cambio(dolar, ext):
    return ext *dolar 

# entrada a nombre
usuario = str(input("Porfavor introduce tu nombre: "))
# imprime bienvenida
print("Hola", usuario,
      "bienvenido al examen de conocimiento turistico en México \na continuación visualizaras las preguntas y "
      "consecutivamente encontraras \npreguntas de opción multiple o preguntas abiertas. En las preguntas de escribir "
      "\ningresa su respuesta en minuscula y sin acentos.")


r1 = (iva_dulce(35, 0.16))
p1 = float(input("Si compras un dulce en la tienda y su valor es de $35 + iva ¿Cuál sera su precio total?"))
dif= (diferencia(p1,r1))
def ciclo_1(dif):
    while dif != 0:
        incorrecta(dif)
        p1 = float(input("Si compras un dulce en la tienda y su valor es de $35 + iva ¿Cuál sera su precio total?"))
        dif= (diferencia(p1,r1))
    return respuestacorrecta()
ciclo_1(dif)
# espacio
enter()

# Llamada operador cambio
r2 = (cambio(20, 87))
dolar = int(input("Imagina que vienes de visita a México y tienes de presupuesto 87 dolares para gastar por día \n¿Cuanto dinero "
    "tienes al día para gastar en pesos? \nNOTA: el precio del dolar es de $20 pesos mexicanos?\n "))
dif= (diferencia(dolar, r2))
def ciclo_2(dif):
    while dif != 0:
        incorrecta(dif)
        dolar = int(input("Imagina que vienes de visita a México y tienes de presupuesto 87 dolares para gastar por día \n¿Cuanto dinero "
    "tienes al día para gastar en pesos? \nNOTA: el precio del dolar es de $20 pesos mexicanos?\n "))
        dif= (diferencia(dolar,r2))
    return respuestacorrecta()
ciclo_2(dif)

# espacio
enter()
# espacio

mont = str(input("¿Cual es la capital de Nuevo León? "))

if mont == "monterrey":
    respuestacorrecta()
elif mont == "Monterrey":
    respuestacorrecta()
else:
    print("Respuesta incorrecta, la respuesta correcta es monterrey")

# espacio
enter()
# espacio

p4 = float(input("¿En que año se fundo la Constitución que rige en la actualidad a México?"))
if p4 == 1917:
    respuestacorrecta()
else:
    print("Respuesta incorrecta, la respuesta correcta es 1917")
# espacio
enter()
# espacio


p5 = int(input("¿Cuál es el año de la Revolución mexicana, si es la raiz cuadrada de 3648100?"))
r5 = (math.sqrt(3648100))
dif = (diferencia(p5,r5))
def ciclo_3(dif):
    while dif != 0:
        incorrecta(dif)
        p5 = int(input("¿Cuál es el año de la Revolución mexicana, si es la raiz cuadrada de 3648100?"))
        r5 = (math.sqrt(3648100))
        dif= (diferencia(p5,r5))
    return respuestacorrecta()
ciclo_3(dif)
 
#fin del programa
fin = input("\nEste es el fin del programa \n¡gracias por participar! ")