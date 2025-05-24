#DÍA 2: Condicionales y Decisiones

# INSTRUCCIONES GENERADAS POR CHAT GPT

#INSTRUCCIONES

# Haz un programa que:

# Pregunte tu nombre, edad y si sabes programar.

# Use condicionales para decir:

# Si eres mayor de edad y sabes programar → "Puedes acceder al sistema".

# Si eres menor de edad → "Acceso denegado: eres menor".

# Si no sabes programar → "Acceso limitado: aprende programación."
#-----------#-----------#-----------#-----------#-----------#


#Solicitudes de datos
nombre = input("¿Cual es tú nombre?: ")
edad= int(input("¿Cual es tu edad?: "))
sabes_programar = input("¿Sabes programar? Si/No: ")

# Verificación de datos
if edad >= 18:
    print("Puedes acceder al sistema")
elif edad < 18 and sabes_programar.lower() == "no":
    print("Acceso limitado: aprende programación")
else:
    print("Acceso denegado.")
    