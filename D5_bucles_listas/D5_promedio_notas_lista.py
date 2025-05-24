#Dia 5 Bucles y Listas

# INSTRUCCIONES GENERADAS POR CHAT GPT

#Solicita 3 notas, guárdalas en una lista, saca el promedio y muestra si aprueba.

#-----------#-----------#-----------#-----------#-----------#



nota1= float(input("Ingresa la primera nota: ")) 
nota2=  float(input("Ingresa la segunda nota: "))
nota3= float(input("Ingresa la tercera nota: "))

lista_notas = [nota1,nota2,nota3]

promedio = sum(lista_notas) / len(lista_notas)

if promedio <= 4.0:
    print(f"Aprobaste con un: {promedio:.2f}")
else:
    print(f"Reprobaste con un: {promedio:.2f}")