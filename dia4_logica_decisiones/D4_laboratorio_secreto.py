#Día 4 – Lógica nivel Pro: decisiones inteligentes

# INSTRUCCIONES GENERADAS POR CHAT GPT

# ¡Tú sistema de acceso exclusivo!

# Crea un sistema que simule el ingreso a un laboratorio secreto de élite.

# Debe incluir:

# ✅ Verificación de identidad (nombre y clave)
# ✅ Verificación de edad
# ✅ Verificación de autorización especial (Sí o No)

# 🔐 Solo pueden ingresar quienes:

# Se llamen "Neo" o "Trinity"

# Sean mayores de 20 años

# Tengan autorización especial

# 💥 Usa condiciones anidadas, and, or, not... ¡Sé creativo!

#Sistema de  acceso exclusivo

#-----------#-----------#-----------#-----------#-----------#

#Verificacion identidad
nombre = input("Ingresa tu nombre: ")
clave = input("Ingresa tu clave: ")

#verificacion edad
edad = int(input ("Ingresa tu edad: "))

#verificación de autorización especial ( si /no 

verificacion= input("¿Tienes autorización especial? Si/No: ")

#Mayuscuals o minisculas correción 
verificacion = verificacion.lower()

#Sistema de verificación
if (nombre == "Neo" or nombre == "Trinity") and edad > 20 and verificacion == "si":
    print("Acceso concedido al laboratorio.")
else:
    print("Acceso denegado")
    
 