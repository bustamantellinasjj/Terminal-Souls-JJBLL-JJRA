# MOTOR_DEL_SIMULADOR.py ES EL ARCHIVO QUE CONTIENE TODAS LAS FUNCIONES DEL JUEGO.
# NO EJECUTADA NADA, SOLO CUANDO LO IMPORTA MORTAL_KOMBAT.py

# LLAMAMOS LA FUNCION random PARA PODER GENERAR NUMEROS ALEATORIOS.
import random

# AQUI DEFINIMOS LAS VARIABLES CONSTANTES, SE PUEDEN CAMBIAR LOS VALORES PREDETERMINADOS.

SALUD_HEROE_MAX     = 100   # VIDA INICIAL DEL HEROE.
SALUD_ENEMIGO_MAX   = 120   # VIDA INICIAL DEL ENEMIGO.
POCIONES_MAX        = 3     # CANTIDAD MAXIMA DE POCIONES.
CURACION_HP         = 20    # 

ATAQUE_MIN          = 10    # DAÑO MAXIMO QUE PUEDE GENERAR EL HEROE.
ATAQUE_MAX          = 25    # DAÑO MAXIMO QUE PUEDE GENERAR EL HEROE.

ESPECIAL_MIN        = 30    # DAÑO MINIMO DE LA HABILIDAD ESPECIAL.
ESPECIAL_MAX        = 50    # DAÑO MAXIMO DE LA HABILIDAD ESPECIAL.
ESPECIAL_FALLO      = 0.50  # LA PROBABILIDAD DE FALLO DEL ATAQUE ESPECIAL ES DEL 50%.

ENEMIGO_MIN         = 15    # DAÑO MINIMO QUE PUEDE GENERAR EL ENEMIGO.
ENEMIGO_MAX         = 20    # DAÑO MAXIMO QUE PUEDE GENERAR EL ENEMIGO.

CRITICO_PROB        = 0.10  # LA PROBABILIDAD DE DAR UN GOLPE CRITICO ES DEL 10%.
ENEMIGO_CURA_UMBRAL = 0.20  # EL ENEMIGO SE CURA SI BAJA DEL 20% DE SALUD.

BARRA_LARGO         = 20    # ANCHO DE LA BARRA DE VIDA.


# 1RA FUNCION:
# CREAMOS LA FUNCION generar_daño LA CUAL RECIBIRA DOS VALORES: (minimo, maximo) 
# LUEGO GENERA UN NUMERO ALEATORIO ENTRE ESOS DOS VALORES
# Y DEVUELVE EL VALOR A QUIEN LLAMÓ LA FUNCION.

def generar_daño(minimo: int, maximo: int) -> int:  # -> (RETORNA UN NUMERO ENTERO).
    return random.randint(minimo, maximo)


# 2DA FUNCION:
# CREAMOS LA FUNCION aplicar_critico LA CUAL RECIBIRA DOS VALORES: (daño, atacante)
# GENERA UN NUMERO DECIMAL ALEATORIO ENTRE 0.0 Y 1.0 CON random.random() 
# SI ESE NUMERO ES MENOR QUE 0.10 (10% DE PROBABILIDAD) → DUPLICA EL DAÑO
# SI NO ES MENOR -> DEVUELVE EL DAÑO SIN CAMBIO.
# EN AMBOS CASOS DEVUELVE EL VALOR A QUIEN LLAMÓ LA FUNCION.

def aplicar_critico(daño: int, atacante: str) -> int: # -> (RETORNA UN NUMERO ENTERO).
    if random.random() < CRITICO_PROB: # AQUI SE GENERA UN FLOAT ENTRE 0.0 Y 1.0
        print(f"  ⚡ ¡GOLPE CRÍTICO de {atacante}! El daño se duplica.")
        return daño * 2 # SI HAY CRITICO DUPLICA EL DAÑO Y SALE DE LA FUNCION
    return daño         # SI NO HAY CRITICO DEVUELV EL DAÑO ORIGINAL.


# 3RA FUNCION:
# CREAMOS LA FUNCION barra_vida LA CUAL RECIBIRA DOS VALORES: (salud_actual, salud_max)
# CALCULA EL PORCENTAJE DE VIDA ACTUAL CON max() PARA EVITAR NEGATIVOS.
# LUEGO CALCULA CUANTOS '#' (LLENOS) Y '-' (VACIOS) MOSTRAR.
# CONSTRUYE Y DEVUELVE LA BARRA VISUAL [####----] COMO TEXTO.

def barra_vida(salud_actual: int, salud_max: int) -> str: # -> (RETORNA UN TEXTO).
    porcentaje = max(salud_actual, 0) / salud_max  # EVITA NEGATIVOS, CALCULA % DE VIDA
    llenos     = int(porcentaje * BARRA_LARGO)     # CUANTOS '#' CABEN SEGUN EL PORCENTAJE
    vacios     = BARRA_LARGO - llenos              # EL RESTO SON '-'
    return f"[{'■' * llenos}{'-' * vacios}]"       # ENSAMBLA Y DEVUELVE LA BARRA.


# 4TA FUNCION:
# CREAMOS LA FUNCION mostrar_estado LA CUAL RECIBIRA CUATRO VALORES: (nombre_h, salud_h, nombre_e, salud_e).
# LLAMA A barra_vida() PARA OBTENER LA BARRA VISUAL DE CADA COMBATIENTE.
# {nombre:10s} IMPRIME EL NOMBRE OCUPANDO SIEMPRE 10 CARACTERES PARA ALINEAR LAS BARRAS.
# {max(salud,0):>3} IMPRIME LA SALUD ALINEADA A LA DERECHA EN 3 CARACTERES SIN NEGATIVOS.
# NO DEVUELVE NADA -> None, SOLO IMPRIME EN PANTALLA.

def mostrar_estado(nombre_h: str, salud_h: int,
                   nombre_e: str, salud_e: int) -> None:  # -> None (NO RETORNA NADA, SOLO IMPRIME).
    print("\n╔══════════════════════════════════════╗")
    barra_h = barra_vida(salud_h, SALUD_HEROE_MAX)  # LLAMA barra_vida() Y GUARDA EL RESULTADO.
    print(f"║  ❤️  {nombre_h:10s} {barra_h} {max(salud_h,0):>3}/{SALUD_HEROE_MAX}")  # IMPRIME HEROE.
    barra_e = barra_vida(salud_e, SALUD_ENEMIGO_MAX)  # LLAMA barra_vida() Y GUARDA EL RESULTADO.
    print(f"║  💀 {nombre_e:10s} {barra_e} {max(salud_e,0):>3}/{SALUD_ENEMIGO_MAX}")  # IMPRIME ENEMIGO.
    print("╚══════════════════════════════════════╝")


# 5TA FUNCION:
# CREAMOS LA FUNCION verificar_ganador LA CUAL RECIBIRA CUATRO VALORES: (nombre_h, salud_h, nombre_e, salud_e).
# VERIFICA SI ALGUNO DE LOS DOS COMBATIENTES LLEGO A 0 HP O MENOS.
# SI EL HEROE LLEGO A 0 → IMPRIME MENSAJE Y DEVUELVE True (COMBATE TERMINADO).
# SI EL ENEMIGO LLEGO A 0 → IMPRIME MENSAJE Y DEVUELVE True (COMBATE TERMINADO).
# SI NADIE LLEGO A 0 → DEVUELVE False (EL COMBATE CONTINUA).
# USA DOS if EN VEZ DE if/elif PARA DETECTAR SI AMBOS LLEGAN A 0 AL MISMO TIEMPO.

def verificar_ganador(nombre_h: str, salud_h: int,
                      nombre_e: str, salud_e: int) -> bool: # -> (RETORNA UN True O False). 
    if salud_h <= 0:  # SI EL HEROE LLEGO A 0 O MENOS.
        print(f"\n  💀 ¡{nombre_h} ha caído! {nombre_e} gana. FATALITY.")
        return True   # COMBATE TERMINADO.
    if salud_e <= 0:  # SI EL ENEMIGO LLEGO A 0 O MENOS.
        print(f"\n  🏆 ¡{nombre_e} derrotado! ¡{nombre_h} gana. FINISH HIM!")
        return True   # COMBATE TERMINADO.
    return False      # NADIE MURIO, EL COMBATE CONTINUA.


# 6TA FUNCION:
# CREAMOS LA FUNCION turno_jugador LA CUAL RECIBIRA CINCO VALORES: (nombre_h, salud_h, nombre_e, salud_e, pociones)
# turno_valido CONTROLA SI LA ACCION FUE VALIDA PARA REPETIR EL MENU O NO
# while not turno_valido REPITE EL MENU MIENTRAS LA ACCION NO SEA VALIDA
# try/except/else: CAPTURA LETRAS Y Ctrl+C — EN AMBOS CASOS VUELVE A PREGUNTAR
# else SOLO CORRE SI NO HUBO NINGUN ERROR EN EL try
# OPCION 1: GENERA DAÑO, APLICA CRITICO Y RESTA SALUD AL ENEMIGO
# OPCION 2: VALIDA POCIONES, CURA AL HEROE SIN PASAR EL MAXIMO CON min()
# OPCION 3: 50% DE FALLAR, SI NO FALLA GENERA DAÑO ESPECIAL
# DEVUELVE TUPLA CON TRES VALORES ACTUALIZADOS: (salud_h, salud_e, pociones)
def turno_jugador(nombre_h: str, salud_h: int,
                  nombre_e: str, salud_e: int,
                  pociones: int) -> tuple[int, int, int]:  # -> (RETORNA TUPLA CON 3 ENTEROS).


    turno_valido = False   # False = repetir menú

    while not turno_valido:

        try:
            opcion = int(input(
                f"\n╔══════════════════════════════════════╗\n"
                f"  1) Atacar       (daño {ATAQUE_MIN}-{ATAQUE_MAX})\n"
                f"  2) Curar        (pociones: {pociones})\n"
                f"  3) Especial     (daño {ESPECIAL_MIN}-{ESPECIAL_MAX}, 50% falla)\n"
                f"╚══════════════════════════════════════╝\n"
                f"  >> Tu opcion: "
            ).strip())
        except ValueError:
            # Escribió letras — vuelve a preguntar
            print("  ⛔  Escribe un número: 1, 2 o 3.")
            turno_valido = False
        except KeyboardInterrupt:
            # Ctrl+C se trata igual que entrada inválida — vuelve a preguntar
            print("  ⛔  Escribe un número: 1, 2 o 3.")
            turno_valido = False
        else:
            # Solo corre si NO hubo ningún error en el try

            if opcion == 1:       # OPCION 1: ATACAR
                daño = aplicar_critico(generar_daño(ATAQUE_MIN, ATAQUE_MAX), nombre_h)
                salud_e -= daño   # RESTA EL DAÑO A LA SALUD DEL ENEMIGO
                print(f"╔══════════════════════════════════════╗")
                print(f"║  ⚔️  {nombre_h} ataca a {nombre_e} (-{daño} HP)")
                print(f"╚══════════════════════════════════════╝")
                turno_valido = True

            elif opcion == 2:      # OPCION 2: CURAR.
                if pociones <= 0:  # SIN POCIONES → NO PIERDE EL TURNO.
                    print(f"╔══════════════════════════════════════╗")
                    print(f"║  ❌ Sin pociones. Elige otra acción.")
                    print(f"╚══════════════════════════════════════╝")
                    turno_valido = False
                else:
                    pociones -= 1                                          # CONSUME UNA POCION
                    salud_h = min(salud_h + CURACION_HP, SALUD_HEROE_MAX)  # NO PASA EL MAXIMO
                    print(f"╔══════════════════════════════════════╗")
                    print(f"║  💊 {nombre_h} se cura (+{CURACION_HP} HP)")
                    print(f"╚══════════════════════════════════════╝")
                    turno_valido = True

            elif opcion == 3:                          # OPCION 3: ESPECIAL
                if random.random() < ESPECIAL_FALLO:   # 50% DE PROBABILIDAD DE FALLAR
                    print(f"╔══════════════════════════════════════╗")
                    print(f"║  🚫 {nombre_h} intenta especial... ¡FALLA!")
                    print(f"╚══════════════════════════════════════╝")
                else:
                    daño = aplicar_critico(generar_daño(ESPECIAL_MIN, ESPECIAL_MAX), nombre_h)
                    salud_e -= daño    # RESTA EL DAÑO ESPECIAL AL ENEMIGO
                    print(f"╔══════════════════════════════════════╗")
                    print(f"║  🌟 ESPECIAL! {nombre_h} inflige -{daño} HP")
                    print(f"╚══════════════════════════════════════╝")
                turno_valido = True

            else:                       # OPCION INVALIDA → VUELVE A PREGUNTAR.
                print("  ⛔  Opción inválida. Escribe 1, 2 o 3.")
                turno_valido = False

    return salud_h, salud_e, pociones   # DEVUELVE TUPLA CON LOS TRES VALORES ACTUALIZADOS.


# 7MA FUNCION:
# CREAMOS LA FUNCION turno_enemigo LA CUAL RECIBIRA CUATRO VALORES: (nombre_h, salud_h, nombre_e, salud_e)
# CALCULA EL PORCENTAJE DE VIDA ACTUAL DEL ENEMIGO
# SI ESE PORCENTAJE ES MENOR AL 20% → EL ENEMIGO SE CURA SIN PASAR EL MAXIMO CON min()
# SI NO ES MENOR AL 20% → EL ENEMIGO ATACA AL HEROE
# EN AMBOS CASOS DEVUELVE TUPLA CON DOS VALORES ACTUALIZADOS: (salud_h, salud_e)
# NO RETORNA pociones PORQUE EL ENEMIGO NO LAS USA.

def turno_enemigo(nombre_h: str, salud_h: int,
                  nombre_e: str, salud_e: int) -> tuple[int, int]:  # -> (RETORNA TUPLA CON 2 ENTEROS).

    if salud_e / SALUD_ENEMIGO_MAX < ENEMIGO_CURA_UMBRAL:  # SI VIDA ENEMIGO < 20% → SE CURA
        salud_e = min(salud_e + CURACION_HP, SALUD_ENEMIGO_MAX)  # NO PASA EL MAXIMO
        print(f"╔══════════════════════════════════════╗")
        print(f"║  🩹 {nombre_e} está débil y se cura (+{CURACION_HP} HP)")
        print(f"╚══════════════════════════════════════╝")
    else:                                                          # SI VIDA > 20% → ATACA
        daño = aplicar_critico(generar_daño(ENEMIGO_MIN, ENEMIGO_MAX), nombre_e)
        salud_h -= daño                                            # RESTA EL DAÑO AL HEROE
        print(f"╔══════════════════════════════════════╗")
        print(f"║  🤬 {nombre_e} ataca a {nombre_h} (-{daño} HP)")
        print(f"╚══════════════════════════════════════╝")

    return salud_h, salud_e  # DEVUELVE TUPLA CON LOS DOS VALORES ACTUALIZADOS
