# IMPORTAMOS DESDE MOTOR_DEL_SIMULADOR.py SOLO LO QUE NECESITA ESTE ARCHIVO.
# SE IMPORTAN LAS CONSTANTES: SALUD_HEROE_MAX, SALUD_ENEMIGO_MAX, POCIONES_MAX.
# SE IMPORTAN LAS FUNCIONES: mostrar_estado, turno_jugador, turno_enemigo, verificar_ganador.
# NO SE IMPORTA generar_daño NI aplicar_critico PORQUE SON FUNCIONES AUXILIARES DEL MOTOR.

from MOTOR_DEL_SIMULADOR import (
    SALUD_HEROE_MAX,
    SALUD_ENEMIGO_MAX,
    POCIONES_MAX,
    mostrar_estado,
    turno_jugador,
    turno_enemigo,
    verificar_ganador,
)


# 1RA FUNCION EN MORTAL_KOMBAT.py:
# CREAMOS LA FUNCION pedir_nombre LA CUAL RECIBIRA UN VALOR: (mensaje).
# nombre = "" INICIALIZA LA VARIABLE ANTES DEL while.
# while not nombre REPITE MIENTRAS EL NOMBRE ESTE VACIO.
# .strip() ELIMINA ESPACIOS EN BLANCO AL INICIO Y AL FINAL.
# Ctrl+C RESETEA nombre = "" Y VUELVE A PREGUNTAR SIN CERRAR EL JUEGO.
# SI EL NOMBRE TIENE MAS DE 20 CARACTERES → AVISA Y VUELVE A PREGUNTAR.
# DEVUELVE EL NOMBRE VALIDO A iniciar_juego().
# ============================================================
def pedir_nombre(mensaje: str) -> str:  # -> (RETORNA UN TEXTO).
    nombre = ""                         # INICIALIZA COMO VACIO ANTES DEL while.
    while not nombre:                   # REPITE MIENTRAS EL NOMBRE ESTE VACIO.
        try:
            nombre = input(mensaje).strip()  # .strip() ELIMINA ESPACIOS EN BLANCO.
        except KeyboardInterrupt:
            nombre = ""                 # Ctrl+C → RESETEA Y VUELVE A PREGUNTAR.
        if not nombre:
            print("\n  ⛔  El nombre no puede estar vacío.")
        elif len(nombre) > 20:          # MAXIMO 20 CARACTERES.
            print("\n  ⛔  Máximo 20 caracteres.")
            nombre = ""                 # RESETEA PARA VOLVER A PREGUNTAR.
    return nombre                       # DEVUELVE EL NOMBRE VALIDO.


# 2DA FUNCION EN MORTAL_KOMBAT.py:
# iniciar_juego() ES EL PUNTO DE ENTRADA DEL JUEGO.
# MUESTRA LA PANTALLA DE BIENVENIDA.
# "★" * 42 REPITE EL CARACTER 42 VECES.
# pedir_nombre() PIDE Y VALIDA LOS NOMBRES DE AMBOS COMBATIENTES.
def iniciar_juego():

    # INTERFAZ DE INICIO:
    print("\n" + "🔥" * 20)                               # REPITE 🔥 42 VECES
    print("   MORTAL KOMBAT  — by. JJBLL & JJRA  ")
    print("🔥" * 20)
 


   # INGRESO DE NOMBRES:
    # pedir_nombre() MANEJA VACIO, Ctrl+C Y LIMITE DE 20 CARACTERES.
    nombre_h = pedir_nombre("\n 🥷🦸 Ingresa el nombre de tu luchador: ")
    nombre_e = pedir_nombre("\n 💀👹 Ingresa el nombre del enemigo:    ")

    # ESTADO INICIAL DEL COMBATE:
    # LAS CONSTANTES NUNCA CAMBIAN, LAS VARIABLES DE ESTADO SI.
    salud_h  = SALUD_HEROE_MAX    # VARIABLE DE ESTADO: ARRANCA EN 100, CAMBIA CADA TURNO
    salud_e  = SALUD_ENEMIGO_MAX  # VARIABLE DE ESTADO: ARRANCA EN 120, CAMBIA CADA TURNO
    pociones = POCIONES_MAX       # VARIABLE DE ESTADO: ARRANCA EN 3, BAJA AL CURAR
    turno    = 1                  # CONTADOR INFORMATIVO DE ROUNDS

    print(f"\n  EL KOMBATE EMPIEZA {nombre_h} vs {nombre_e}\n")  # MENSAJE DE INICIO


    # BUCLE PRINCIPAL — REPITE MIENTRAS EL COMBATE CONTINUE
    el_combate_continua = True         # TRUE = COMBATE ACTIVO, FALSE = COMBATE TERMINADO

    while el_combate_continua:         # REPITE HASTA QUE ALGUIEN LLEGUE A 0 HP
        print(f"\n  ══ RONDA {turno} ══")
        mostrar_estado(nombre_h, salud_h, nombre_e, salud_e)  # MUESTRA VIDA DE AMBOS

        # TURNO DEL JUGADOR — ACTUALIZA salud_h, salud_e, pociones
        salud_h, salud_e, pociones = turno_jugador(
            nombre_h, salud_h, nombre_e, salud_e, pociones
        )

        # VERIFICA SI EL ENEMIGO MURIO TRAS EL ATAQUE DEL HEROE
        if verificar_ganador(nombre_h, salud_h, nombre_e, salud_e):
            el_combate_continua = False  # PARA EL BUCLE

        # TURNO DEL ENEMIGO — SOLO SI EL JUGADOR NO GANO AUN
        if el_combate_continua:          # EVITA QUE EL ENEMIGO ATAQUE ESTANDO MUERTO
            salud_h, salud_e = turno_enemigo(nombre_h, salud_h, nombre_e, salud_e)

            # VERIFICA SI EL HEROE MURIO TRAS EL ATAQUE DEL ENEMIGO
            if verificar_ganador(nombre_h, salud_h, nombre_e, salud_e):
                el_combate_continua = False  # PARA EL BUCLE

        turno += 1                       # turno = turno + 1 → SIGUIENTE ROUND

    # ESTADO FINAL — MUESTRA LA VIDA AL TERMINAR EL COMBATE
    mostrar_estado(nombre_h, salud_h, nombre_e, salud_e)
    print("\n  MORTAL KOMBAT — by. JJBLL & JJRA | RIWI Pte!\n")  # MENSAJE DE DESPEDIDA


# PUNTO DE ENTRADA:
# SOLO EJECUTA iniciar_juego() SI CORRES ESTE ARCHIVO DIRECTAMENTE.
# SI LO IMPORTAS DESDE OTRO ARCHIVO, iniciar_juego() NO SE EJECUTA SOLO.
if __name__ == "__main__":
    iniciar_juego()