 # #Día 4 – Lógica nivel Pro: decisiones inteligentes

# INSTRUCCIONES GENERADAS POR CHAT GPT

#  📘 Segundo ejercicio: Control de asistencia
# Un estudiante puede aprobar el ramo si:

# Tiene más de 70% de asistencia y

# Su nota final es mayor o igual a 4.0

# 🔸 Pídele al usuario:

# Porcentaje de asistencia (como float)

# Nota final (como float)

# 🔸 Muestra si aprueba o reprueba, y por qué.

#-----------#-----------#-----------#-----------#-----------#

#Solicitud datos

porcentaje_asistencia = float(input("Ingresa tu porcentaje de asistencia: "))
nota_final = float(input("Ingresa tu nota final: "))

# calculos si aprueba o no

if porcentaje_asistencia >= 0.70 and nota_final >= 4.0: 
    print("¡Felicidades aprobaste!")
elif porcentaje_asistencia < 0.70 and nota_final < 4.0:
    print("¡Reprobaste por asistencia y nota!")
elif porcentaje_asistencia < 0.70:
    print("¡Reprobaste por asistencia!")
elif nota_final < 4.0: 
    print("¡Reprobaste por nota!")