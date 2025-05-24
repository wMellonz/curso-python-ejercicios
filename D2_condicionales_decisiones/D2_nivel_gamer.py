# Día 2:  Condicionales y decisiones inteligentes

# INSTRUCCIONES GENERADAS POR CHAT GPT

#INSTRUCCIONES

# Haz un verificador de nivel gamer que diga:

# Si tu edad es menor de 13: “Nivel: MiniGamer”

# Entre 13 y 18: “Nivel: JuniorGamer”

# Entre 19 y 30: “Nivel: Gamer Pro”

# Más de 30: “Nivel: Leyenda Gamer”

# 🎮 Usa if, elif, else para mostrarlo según la edad que pongas.

#-----------#-----------#-----------#-----------#-----------#

#Solicitar edad

edad = int(input("¿Cual es tu edad?: "))

# Verificación edad y nivel

if edad < 13:
    print("¡Eres un MiniGamer!")
elif edad >= 13 and edad <= 18:
    print("¡Eres un JuniorGamer!")
elif edad >= 19 and edad <= 30: 
    print("¡Eres un Gamer Pro!")
else:
    print("¡Eres una Leyenda Gamer!")