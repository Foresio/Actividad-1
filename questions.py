import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Se crea la variable puntaje
puntaje = 0

# Uso de zip para acomodar las tres listas en una misma variable
# Creando una lista de listas
# Todas posicionadas y colocadas en el mismo orden y lugar
# forzando a que del zip salga como variable lista para evitar error
# Para que el 'random.sample' pueda procesarlo y sacar al azar de cada lista en orden
# hasta k=3 preguntas con sus correspondientes opciones y respuestas correctas

questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)

# Cabe aclarar que el uso de un .sample evita repeticiones al elegir al azar
# Donde un .choice es capaz de repetir resultados sacados del mismo sitio
# Por estas limitaciones, el .sample no podria aplicarse en una lista menor a un numero de secuencia establecida
# En cambio el .choice es capaz de trabajar con una secuencia mayor a la cantidad de objetos en lista


# El usuario deberá contestar 3 preguntas
for _ in range(3):
    
    # Creo variables auxiliares para almacenar la lista con su correspondiente problema y datos
    # Cada variable posee su propia lista con los datos obtenidos al elegir un problema al azar
    # Queda mejor acomodado en el caso de futuras alteraciones
    problema = questions_to_ask[_] 
    pregunta_aux = problema[0]
    respuestas_aux = problema[1]
    correcta_aux = problema[2]
    
    # Se muestra la pregunta y las respuestas posibles
    print(pregunta_aux)
    for i, respuestas in enumerate(respuestas_aux):
        print(f"{i + 1}. {respuestas}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2): 
        user_input = input("Respuesta: ")

        # Verifica que sea número antes de convertir
        if user_input.isdigit():
            user_answer = int(user_input) - 1
            if 0 <= user_answer <= 3:
                if user_answer == correcta_aux:
                    print("¡Correcto!")
                    puntaje += 1
                    break
                else:
                    if puntaje != 0:
                        puntaje = puntaje - 0.5
            else:
                print("Respuesta no válida")
                sys.exit(1)        
        else:
            print("Respuesta no válida")
            sys.exit(1)
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        print("Incorrecto. La respuesta correcta es:")
        print(respuestas_aux[correcta_aux])
    # Se imprime un blanco al final de la pregunta
    print()
print(f"Tu puntaje final son {puntaje} de 3 puntos")