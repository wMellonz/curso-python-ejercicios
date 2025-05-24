#Día 4 – Lógica nivel Pro: decisiones inteligentes

# INSTRUCCIONES GENERADAS POR CHAT GPT

# 🧪 Ejercicio práctico: Verificación de acceso
# Crea un programa que:

# 🔹 Pida al usuario:

# Su edad

# Si tiene carnet de identidad (Sí o No)

# Si tiene invitación (Sí o No)

# 🔹 Solo puede ingresar si:

# Tiene más de 18 años y tiene carnet

# O tiene invitación (aunque sea menor de edad)

# 💡 Usa and, or, not si quieres experimentar más.

#-----------#-----------#-----------#-----------#-----------#

#Solicitud de datos

edad = int(input("¿Cual es tú edad?: "))
carnet_identidad = input("¿Tiene carnet de identidad? Si/No: ")
invitacion = input("¿Tiene invitación? Si/No: ")
#minisculas para evitar errores

carnet_identidad = carnet_identidad.lower()
invitacion = invitacion.lower()

# permisos
if edad >= 18 and carnet_identidad == "si":
    print("Puedes ingresar.") 
elif invitacion == "si": 
    print("Puedes ingresar.")
else:
    print("No puedes ingresar")


