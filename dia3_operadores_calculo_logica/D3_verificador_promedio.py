#DÍA 3 – Operadores, cálculo y lógica combinada

# INSTRUCCIONES GENERADAS POR CHAT GPT

#Pídele al usuario 3 notas, calcula el promedio y dile si aprueba (promedio ≥ 4.0).

#-----------#-----------#-----------#-----------#-----------#

#variable notas, definir como float y solicitar los datos a trabajar

nota1 = float(input("Ingresa la primera nota: ")) 
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

# Calculo de promedio

promedio = (nota1 + nota2 + nota3) / 3

#Mostrar los resultados
if promedio >= 4.0:
    print(f"¡Felicidades Aprobaste con {promedio:.2f}!")
elif promedio < 4.0:
    print(f"¡Reprobaste con {promedio:.2f}!") 


