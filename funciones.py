# ============================================================
#  funciones.py  —  Motor de combate de Terminal Souls
#  Este archivo SOLO contiene funciones; no ejecuta nada solo.
#  Se importa desde terminal_souls.py para usarse allí.
# ============================================================

import random  # Necesario para generar daños y probabilidades aleatorias

# ---------- CONSTANTES DEL JUEGO ----------
# Centralizar los valores aquí permite cambiarlos en un solo lugar.

HEROE_HP_MAX        = 100
HEROE_POCIONES      = 3

ENEMIGO_HP_MAX      = 120
ENEMIGO_CURA_HP     = 25
ENEMIGO_CURA_UMBRAL = 0.20   # El enemigo se cura si su vida baja del 20 %

ATAQUE_MIN          = 10
ATAQUE_MAX          = 25

ESPECIAL_MIN        = 30
ESPECIAL_MAX        = 50
ESPECIAL_FALLO      = 0.50   # 50 % de probabilidad de que la especial falle

ENEMIGO_MIN         = 15
ENEMIGO_MAX         = 20

CURACION_HP         = 20
CRITICO_PROB        = 0.10   # 10 % de probabilidad de golpe crítico
BARRA_LARGO         = 20     # Caracteres de ancho de la barra de vida


# ============================================================
#  generar_daño(minimo, maximo)
#  Devuelve un entero aleatorio dentro del rango recibido.
#  random.randint incluye AMBOS extremos (min y max).
# ============================================================
def generar_daño(minimo: int, maximo: int) -> int:
    return random.randint(minimo, maximo)


# ============================================================
#  barra_vida(hp_actual, hp_max)
#  Construye la barra visual [####----] proporcional al HP.
#  Usa max() para evitar que hp_actual sea negativo en la fórmula.
# ============================================================
def barra_vida(hp_actual: int, hp_max: int) -> str:
    porcentaje = max(hp_actual, 0) / hp_max        # Proporción de vida restante
    llenos     = int(porcentaje * BARRA_LARGO)     # Cuántos '#' caben
    vacios     = BARRA_LARGO - llenos              # El resto son '-'
    return f"[{'#' * llenos}{'-' * vacios}]"       # Cadena final ensamblada


# ============================================================
#  mostrar_estado(nombre_h, hp_h, nombre_e, hp_e)
#  Imprime en pantalla la vida de ambos combatientes.
#  Muestra barra visual [####----] y números exactos de HP.
# ============================================================
def mostrar_estado(nombre_h: str, hp_h: int,
                   nombre_e: str, hp_e: int) -> None:

    print("\n" + "=" * 40)
    barra_h = barra_vida(hp_h, HEROE_HP_MAX)
    print(f"  {nombre_h:10s} {barra_h}  HP: {max(hp_h, 0):>3}/{HEROE_HP_MAX}")
    barra_e = barra_vida(hp_e, ENEMIGO_HP_MAX)
    print(f"  {nombre_e:10s} {barra_e}  HP: {max(hp_e, 0):>3}/{ENEMIGO_HP_MAX}")
    print("=" * 40)


# ============================================================
#  aplicar_critico(daño, atacante)
#  Lanza la probabilidad de crítico (10 %).
#  random.random() genera un float entre 0.0 y 1.0;
#  si cae por debajo de 0.10 → crítico → daño x2.
# ============================================================
def aplicar_critico(daño: int, atacante: str) -> int:
    if random.random() < CRITICO_PROB:
        print(f"  ⚡ ¡GOLPE CRÍTICO de {atacante}! El daño se duplica.")
        return daño * 2
    return daño   # Sin cambio si no hubo crítico


# ============================================================
#  turno_jugador(nombre_h, hp_h, nombre_e, hp_e, pociones)
#  Muestra el menú, valida la entrada y ejecuta la acción.
#  Retorna una tupla con los tres valores actualizados.
# ============================================================
def turno_jugador(nombre_h: str, hp_h: int,
                  nombre_e: str, hp_e: int,
                  pociones: int) -> tuple[int, int, int]:

    print(f"\n  Pociones restantes: {pociones}")
    print("  ¿Qué hace el héroe?")
    print("  [1] Atacar              (daño 10–25)")
    print("  [2] Curar               (recupera 20 HP)")
    print("  [3] Habilidad Especial  (daño 30–50, 50 % de fallar)")

    # Bucle de validación: repite hasta recibir 1, 2 o 3 válido
    while True:
        eleccion = input("  >> Tu elección: ").strip()

        if eleccion == "1":                                   # --- ATACAR ---
            daño = generar_daño(ATAQUE_MIN, ATAQUE_MAX)
            daño = aplicar_critico(daño, nombre_h)
            hp_e -= daño
            print(f"\n  ⚔️  ¡{nombre_h} golpea por {daño} de daño!")
            break

        elif eleccion == "2":                                 # --- CURAR ---
            if pociones == 0:
                # Sin pociones: avisa pero NO pierde el turno
                print("  ❌ No te quedan pociones. Elige otra acción.")
                continue   # Regresa al inicio del while de validación
            pociones -= 1
            hp_h = min(hp_h + CURACION_HP, HEROE_HP_MAX)    # No supera el máximo
            print(f"\n  💊 ¡{nombre_h} usa una poción y recupera {CURACION_HP} HP!")
            break

        elif eleccion == "3":                                 # --- ESPECIAL ---
            if random.random() < ESPECIAL_FALLO:             # 50 % de fallar
                print(f"\n  💨 ¡{nombre_h} intenta la especial... ¡y FALLA!")
            else:
                daño = generar_daño(ESPECIAL_MIN, ESPECIAL_MAX)
                daño = aplicar_critico(daño, nombre_h)
                hp_e -= daño
                print(f"\n  🌟 ¡ESPECIAL! {nombre_h} inflige {daño} de daño!")
            break

        else:
            print("  ⚠️  Opción inválida. Escribe 1, 2 o 3.")

    return hp_h, hp_e, pociones   # Tupla con los tres valores actualizados


# ============================================================
#  turno_enemigo(nombre_h, hp_h, nombre_e, hp_e)
#  IA básica del enemigo:
#  - Por debajo del 20 % de vida → se cura.
#  - En cualquier otro caso → ataca al héroe.
#  Retorna (hp_heroe, hp_enemigo) actualizados.
# ============================================================
def turno_enemigo(nombre_h: str, hp_h: int,
                  nombre_e: str, hp_e: int) -> tuple[int, int]:

    porcentaje_vida = hp_e / ENEMIGO_HP_MAX   # Proporción de vida actual

    if porcentaje_vida < ENEMIGO_CURA_UMBRAL:              # IA: decide curarse
        hp_e = min(hp_e + ENEMIGO_CURA_HP, ENEMIGO_HP_MAX)
        print(f"\n  🩹 {nombre_e} está muy débil y se cura {ENEMIGO_CURA_HP} HP!")
    else:                                                  # IA: decide atacar
        daño = generar_daño(ENEMIGO_MIN, ENEMIGO_MAX)
        daño = aplicar_critico(daño, nombre_e)
        hp_h -= daño
        print(f"\n  👹 ¡{nombre_e} ataca y golpea por {daño} de daño!")

    return hp_h, hp_e


# ============================================================
#  verificar_ganador(nombre_h, hp_h, nombre_e, hp_e)
#  Retorna True si alguno llegó a 0 HP → el bucle debe parar.
#  Retorna False si el combate debe continuar.
# ============================================================
def verificar_ganador(nombre_h: str, hp_h: int,
                      nombre_e: str, hp_e: int) -> bool:

    if hp_h <= 0:
        print(f"\n  💀 ¡{nombre_h} ha caído! {nombre_e} gana el combate.")
        return True

    if hp_e <= 0:
        print(f"\n  🏆 ¡{nombre_e} ha sido derrotado! ¡{nombre_h} es victorioso!")
        return True

    return False   # Nadie murió: el combate sigue
