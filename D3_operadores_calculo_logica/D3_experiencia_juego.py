#DÍA 3 – Operadores, cálculo y lógica combinada

# INSTRUCCIONES GENERADAS POR CHAT GPT

# Objetivo:
# Simula un sistema de experiencia de videojuego:

# 1. Pídele al jugador:
# Nivel actual (int)

# Experiencia actual (int)

# Experiencia ganada en una misión (int)

# 2. Calcula:
# Nueva experiencia total

# Si llega a 100 puntos de experiencia → sube de nivel

# 3. Muestra:
# Nivel final

# Exp final

# Un mensaje especial si sube de nivel 🎉
#Solicitar nivel, exp actual, exp ganada en mision todos son (int) o enteros

#-----------#-----------#-----------#-----------#-----------#


nombre_player = (input("¿Cual es tu nombre jugador?: ")) 
print("-" * 50)
print(f"¡Hola! {nombre_player} ¡Bienvenido al sistema de experiencia!")
print("-" * 50)

nivel_actual = int(input("¿Cual es tu nivel actual?: "))
exp_actual = int(input("¿Cuál es tu experiencia actual?: "))
exp_ganada = int(input("¿Cuanta experiencia te dio la misión?: "))

# calculos
print("-" * 50)

exp_total = (exp_actual + exp_ganada)
subidas = 0  # Para contar cuantas veces se sube de nivel

while exp_total >= 100:
    nivel_actual += 1
    exp_total -= 100
    subidas += 1

if subidas > 0:
    print(f"\n¡Subiste {subidas} nivel(es)! 🎉")
else:
    print("\nSeguiste acumulando experiencia.")

print("-" * 50)
print(f"Nivel final: {nivel_actual}")
print(f"Experiencia final: {exp_total}")
print("-" * 50)
