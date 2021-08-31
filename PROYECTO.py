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


#entrada a nombre
usuario=str(input("Porfavor introduce tu nombre: "))
#imprime bienvenida
print ("Hola", usuario, "bienvenido al examen de conocimiento turistico en México \na continuación visualizaras las preguntas y consecutivamente encontraras \npreguntas de opción multiple o preguntas abiertas. En las preguntas de escribir \ningresa su respuesta en minuscula y sin acentos.")


#inicio de funciones
IVA = 0.16 #float
dulce=35 #foat
v= dulce*IVA #se saca el porcentaje de iva del valor de dulce
r1=(v+dulce) #suma los dos valores dados anteriormente para sacar el precio total

#entrada de respuesta a iva 1
p1= float(input("Si compras un dulce en la tienda y su valor es de $35 + iva ¿Cuál sera su precio total?"))
diferencia = p1-r1
print("Tu precio vario en un: ", diferencia)
print("Tu resultado final tendria que ser= ", r1)

#Uso de operadores booleanos
p2 = str(input("¿Cual es la capital de Nuevo León? "))
monterrey = p2
if p2 == monterrey:
    print("Correcto")
else:
    print("Incorrecto")
    
print("La respuesta correcta es monterrey")

#Operación con uso de operadores
p3 = float(input("Imagina que vienes de visita a México y tienes de presupuesto 87 dolares para gastar por día \n¿Cuanto dinero tienes al día para gastar en pesos? \nNOTA: el precio del dolar es de 20.19 pesos mexicanos"))
dolar = 20.19
ext = 87
presupuesto= ext*dolar
dif = presupuesto-p3
print("Tu precio vario en un: ", dif)
print("Tu resultado final tendria que ser= ", presupuesto)

#operación
#uso de funciones
p4 = float(input("¿En que año se fundo la Constitución que rige en la actualidad a México?"))
const= 1824
if const>=1824:
    print("Correcto")
else:
    print("Incorrecto")

print("La respuesta correcta es 1824")

#operación dividir y multiplicar
p5= float(input("¿Si el territorio de México es el doble de la mitad de 9.86 millones de km², \n¿Cuál es el territorio total en km²?"))
print("escribe la cifra completa y sin letras")
div= 9.86/2
comp= div*2
dif= comp-p5
print("Tu precio vario en un: ", dif)
print("La respuesta correcta es: ", comp, "Millones")

#operacion
p8= str(input("Uno de los cañones más importantes en el mundo con gran riqueza ecológica. Ubicado en el sur de México. "))
r8= "cañon del sumidero"
print("La respuesta correcta es:", r8)


#Uso de operadores booleanos
p6= str(input("¿En que estado se encuentra la Zona Arqueológica de Monte Albán?"))
oaxaca = p6
if p6 == oaxaca:
    print("Correcto")
else:
    print("Incorrecto")
    
print("La respuesta correcta es oaxaca")

#operacion raiz cuadrada
p9= int(input("¿Cuál es el año de la Revolución mexicana, si es la raiz cuadrada de 3648100?"))
r9= (math.sqrt(3648100))
print("La respuesta correcta es:", r9)


#Uso de operadores booleanos
P7= str(input("¿Cuál es el nombre de las cavernas con agua que eran sitios sagrados para los mayas?"))
r7= "cenotes"
print("La respuesta correcta es: ", r7)

#fin preguntas
