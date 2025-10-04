import random

def obtener_opcion_usuario():
    opciones = ['piedra', 'papel', 'tijera']
    opcion = input("Elige piedra, papel o tijera: ").lower()
    while opcion not in opciones:
        opcion = input("Opción inválida. Elige piedra, papel o tijera: ").lower()
    return opcion

def obtener_opcion_computadora():
    return random.choice(['piedra', 'papel', 'tijera'])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "Perdiste..."

def jugar():
    print("Bienvenido al juego Piedra, Papel o Tijera")
    usuario = obtener_opcion_usuario()
    computadora = obtener_opcion_computadora()
    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)

if __name__ == "__main__":
    jugar()
