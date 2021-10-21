"""
Sofía de la Cruz Vázquez - A01704568
Nombre del proyecto = Cultura Mexico
Examen sobre cultura general en México.
El examen trata sobre información de cultura general en México donde se evaluara el
conocimiento sobre economía, historia y geografía.
El programa esta diseñado para ser contestado de manera dinámica y para ayudar al
usuario a repasar conocimiento util si visita México.
Las preguntas son abiertas y se compararán con la respuesta correcta,
por lo que hasta que se ingrese la respuesta correcta
no cambiara de pregunta.
NOTA: En las preguntas de operación matematica se dara la diferencia en caso de ser
erronea.
"""
#importa biblioteca math para su uso en linea 188
import math
#inicio funciones auxiliares 
def respuestacorrecta():
    """
    (uso funciones)
    Función para cuando las respuestas son correctas
    devuelve:imprime texto
    """
    print("Tu respuesta es correcta")
    
def incorrecta(n):
    """
    (uso funciones)
    recibe:n
    Función para cuando las respuestas son incorrectas
    en preguntas de operaciones, n es el valor de
    la diferencia entre la respuesta correcta y la del usuario.
    devuelve: imprime el texto y el valor de n
    """
    print("Respuesta incorrecta.\nIntenta de nuevo, tu diferencia es de", n)

def enter():
    """
    (uso funciones)
    devuelve:imprime instrucciones y al dar enter, imprime doble espacio
    entre el texto de instrucción y la nueva pregunta.
    """
    input("\n\nPresione enter para continuar\n\n")

def imprime_for(matriz):
    """
    (uso de listas anidadas, listas, funciones,ciclos anidados)
    recibe: matriz 
    Imprime los valores en una lista con un
    espacio entre los valores de la
    lista anidada, el siguiente for toma
    los componentes de cada sublista
    y con el uso de 'end=""'  termina de
    imprimir toda la lista anidada en
    orden y sin caracteres extras.
    devuelve: lista impresa en orden.
    Uso de 'end=' investigado de: (RemcoGerlich, 2018)
    Recuperado del artículo referenciado en Readme.
    """
    for linea in matriz:
        for columna in linea:
            print(columna, end=" ")#'end=':(RemcoGerlich, 2018) 
        print()
        
#inicio funciones de preguntas
def iva_dulce(dulce, iva):
    """
    (uso de operadores, funciones, ciclos)
    recibe: matriz 
    Función con lista que guarda en un acumuludor el
    valor del iva y lo suma para sacar el valor total
    devuelve: el total de la operación.
    """ 
    acum = 0
    for ren in range(2):
        acum = dulce * iva
        total= acum + 35
    return total

def diferencia(num1,num2):#aqui
    """
    (uso de operadores, funciones)
    recibe:num1, num2
    Función que hace una resta para sacar la diferencia
    a la respuesta correcta y la respuesta del usuario
    devuelve: resultado de la diferencia entre los dos valores.
    """
    resultado = num1 - num2
    return resultado 
    
    
"""
Inicio de funciones con ciclos while para que cada vez que la respuesta
sea incorrecta se repita el ciclo con los casts
adecuados para cada respuesta(string,enteros o flotantes).
Los ciclos no se rompen hasta recibir la respuesta correcta.
"""

def ciclo_2(ciclo2):
    """
    (uso de funciones, ciclos)
    recibe:ciclo2
    Función utilizada en numero entero para
    reiniciar el ciclo hasta que la respuesta
    de la operación sea correcta.
    regresa: respuesta correcta o reincia la pregunta y te da la diferencia.
    """
    while ciclo2 != 0:
        incorrecta(ciclo2)
        dolar = int(input("Imagina que vienes de visita a México y tienes de presupuesto \n87 dolares para gastar por día \n¿Cuanto dinero tienes al día para gastar en pesos? \nNOTA: el precio del dolar es de $20 pesos mexicanos?\n "))
        ciclo2 = (diferencia(dolar,r2))
    return respuestacorrecta()

def monterrey(ciclo3):
    """
    (uso de funciones,ciclos)
    recibe:ciclo3
    Función que compara la respuesta string ingresada por el usuario
    y la respuesta correcta, no cambia de pregunta hasta estar correcta.
    devuelve: respuesta correcta o vuelve a imprimir la pregunta.
    """
    while ciclo3 != r3:
        ciclo3 = str(input("Respuesta incorrecta.Intente de nuevo \n¿Cual es la capital de Nuevo León?\n"))
    return respuestacorrecta()

def ciclo_4(ciclo4):
    """
    (uso de funciones, ciclos)
    recibe:ciclo4
    función de entero que compara la respuesta
    correcta con la del usuario hasta que
    sea correcto.
    devuelve:respuesta correcta o vuelve a imprimir la pregunta.
    """
    while ciclo4 != 1917:
        ciclo4 = int(input("Respuesta incorrecta.Intente de nuevo \n¿En que año se fundo la Constitución que rige en la actualidad a México?\n"))
    return respuestacorrecta()

def ciclo_5(ciclo5):
    """
    (uso de operadores, ciclos,funciones)
    recibe:ciclo5
    Función de ciclo while que no permite pasar de pregunta
    hasta tener la respuesta entera de la operación y que sea correcta.
    devuelve: respuesta correcta o reincia la pregunta y te da la diferencia.
    """
    while ciclo5 != 0:
        incorrecta(ciclo5)
        p5 = int(input("¿Cuál es el año de la Revolución mexicana, si es la raiz cuadrada de 3648100?"))
        r5 = (math.sqrt(3648100))
        ciclo5 = (diferencia(p5,r5))
    return respuestacorrecta()
"""
Inicio de programa
"""
# entrada a nombre
usuario = str(input("Porfavor introduce tu nombre: "))
# imprime bienvenida
print("Hola", usuario,"bienvenido al examen de conocimiento turistico en México:\nA continuación visualizara preguntas abiertas...\nRecuerde ingresar sus respuestas en MINUSCULAS y SIN ACENTOS\nNo podras avanzar de pregunta hasta tener la respuesta correcta .\n¡Mucho exito", usuario,"!")
r1 = iva_dulce(35,0.16)
p1 = float(input("\nSi compras un dulce en la tienda y su valor es de $35 + iva ¿Cuál sera su precio total?\n"))
while p1!=r1:
    ciclo1 = (diferencia(p1,r1))
    incorrecta(ciclo1)
    p1 = float(input("Si compras un dulce en la tienda y su valor es de $35 + iva ¿Cuál sera su precio total?\n"))
respuestacorrecta()
print(r1)
# espacio
enter()
r2 = 20*87
dolar = int(input("Imagina que vienes de visita a México y tienes de presupuesto\n87 dolares para gastar por día \n¿Cuanto dinero "
    "tienes al día para gastar en pesos? \nNOTA: el precio del dolar es de $20 pesos mexicanos?\n"))
ciclo2 = (diferencia(dolar, r2))
ciclo_2(ciclo2)
# espacio
enter()
p3 = str(input("¿Cual es la capital de Nuevo León?\n"))
r3 = "monterrey" 
ciclo3=p3
monterrey(ciclo3)
# espacio
enter()
ciclo4 = float(input("¿En que año se fundo la Constitución que rige en la actualidad a México?\n"))
ciclo_4(ciclo4)
# espacio
enter()
p5 = int(input("¿Cuál es el año de la Revolución mexicana, si es la raiz cuadrada de 3648100?\n"))
r5 = (math.sqrt(3648100)) #(Striver,2018)
"""
Saque la raíz de 3648100 con el uso de math.sqrt
Recuperado del artículo referenciado en Readme.
Importe la biblioteca de 'math'. (Striver, 2018)
"""
ciclo5 = (diferencia(p5,r5))
ciclo_5(ciclo5)
fin=str(input("¿Desea ver las respuestas correctas\n Porfavor ingrese 'si' o 'no':\n"))
lista = [['pregunta 1:',r1],
         ['pregunta 2: ',r2],
         ['pregunta 3: ','Monterrey'],
         ['pregunta 4: ',1917],
         ['pregunta 5: ',1910]]

despedida=print("\nEste es el fin del programa \n¡ Gracias por participar",usuario,"!")
if fin=="si":
    imprime_for(lista)
    print()
    despedida
else:
    despedida