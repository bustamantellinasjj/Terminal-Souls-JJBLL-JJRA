# ============================================================
#  terminal_souls.py  —  Punto de entrada del juego
#  Este archivo SOLO contiene el flujo principal (main).
#  Toda la lógica vive en funciones.py y se importa aquí.
# ============================================================

# Importamos TODO lo que necesitamos desde nuestro módulo funciones.py
# El asterisco (*) trae todas las funciones y constantes de ese archivo.
from funciones import (
    HEROE_HP_MAX,
    HEROE_POCIONES,
    ENEMIGO_HP_MAX,
    mostrar_estado,
    turno_jugador,
    turno_enemigo,
    verificar_ganador,
)


# ============================================================
#  main()
#  Punto de entrada del juego: presentación, configuración
#  y el bucle principal que repite turnos hasta que alguien muera.
# ============================================================
def main():

    # --- Pantalla de bienvenida ---
    print("\n" + "★" * 40)
    print("       ⚔️   TERMINAL SOULS   ⚔️")
    print("★" * 40)

    # --- Nombre del héroe con manejo de Ctrl+C ---
    # KeyboardInterrupt se lanza cuando el usuario presiona Ctrl+C.
    # Lo capturamos para cerrar el juego limpiamente en lugar de mostrar
    # un error feo en la terminal.
    try:
        nombre_h = input("\n  Ingresa el nombre de tu héroe: ").strip()
    except KeyboardInterrupt:
        print("\n\n  Juego cancelado. ¡Hasta la próxima batalla!")
        return   # Salimos de main() sin ejecutar nada más

    # Si el jugador no escribe nada, asignamos un nombre por defecto
    if not nombre_h:
        nombre_h = "Héroe"

    nombre_e = "Demonio Oscuro"   # Nombre fijo del enemigo

    # --- Estado inicial del combate ---
    hp_h     = HEROE_HP_MAX     # Héroe comienza con vida completa
    hp_e     = ENEMIGO_HP_MAX   # Enemigo también
    pociones = HEROE_POCIONES   # Pociones iniciales del héroe
    turno    = 1                # Contador informativo de turnos

    print(f"\n  ¡El combate entre {nombre_h} y {nombre_e} comienza!\n")

    # ============================================================
    #  BUCLE PRINCIPAL — "el_combate_continua"
    #
    #  Nombrar el bucle con una variable booleana hace el código
    #  más legible que un simple "while True": al leer
    #  "while el_combate_continua" queda claro el propósito.
    #
    #  El bucle se detiene cuando verificar_ganador() retorna True,
    #  lo que hace que el_combate_continua pase a False.
    # ============================================================
    el_combate_continua = True

    while el_combate_continua:

        print(f"\n  ══ TURNO {turno} ══")
        mostrar_estado(nombre_h, hp_h, nombre_e, hp_e)

        # --- Turno del jugador ---
        # Capturamos Ctrl+C dentro del bucle también, por si el jugador
        # quiere salir a mitad de la partida sin romper la terminal.
        try:
            hp_h, hp_e, pociones = turno_jugador(
                nombre_h, hp_h, nombre_e, hp_e, pociones
            )
        except KeyboardInterrupt:
            print("\n\n  Combate interrumpido. ¡Hasta la próxima batalla!")
            el_combate_continua = False   # Detenemos el bucle limpiamente
            break

        # Verificamos si el enemigo murió tras el turno del héroe
        if verificar_ganador(nombre_h, hp_h, nombre_e, hp_e):
            el_combate_continua = False
            break

        # --- Turno del enemigo ---
        hp_h, hp_e = turno_enemigo(nombre_h, hp_h, nombre_e, hp_e)

        # Verificamos si el héroe murió tras el turno del enemigo
        if verificar_ganador(nombre_h, hp_h, nombre_e, hp_e):
            el_combate_continua = False
            break

        turno += 1   # Siguiente turno

    # --- Estado final y despedida ---
    mostrar_estado(nombre_h, hp_h, nombre_e, hp_e)
    print("\n  Gracias por jugar Terminal Souls. ¡Hasta la próxima batalla!\n")


# ============================================================
#  PUNTO DE ENTRADA
#  Solo ejecuta main() si corres este archivo directamente:
#      python terminal_souls.py
#  Si lo importas desde otro script, main() NO se ejecuta solo.
# ============================================================
if __name__ == "__main__":
    main()
