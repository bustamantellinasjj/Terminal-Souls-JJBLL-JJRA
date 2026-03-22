import random

SALUD_HEROE_MAX     = 100  
SALUD_ENEMIGO_MAX   = 120   
POCIONES_MAX        = 3     
CURACION_HP         = 20    
ATAQUE_MIN          = 10    
ATAQUE_MAX          = 25   
ESPECIAL_MIN        = 30   
ESPECIAL_MAX        = 50    
ESPECIAL_FALLO      = 0.50  
ENEMIGO_MIN         = 15    
ENEMIGO_MAX         = 20    
CRITICO_PROB        = 0.10  
ENEMIGO_CURA_UMBRAL = 0.20  
BARRA_LARGO         = 20    

def generar_daño(minimo: int, maximo: int) -> int:  
    return random.randint(minimo, maximo)

def aplicar_critico(daño: int, atacante: str) -> int: 
    if random.random() < CRITICO_PROB: 
        print(f"  ⚡ ¡GOLPE CRÍTICO de {atacante}! El daño se duplica.")
        return daño * 2 
    return daño       

def barra_vida(salud_actual: int, salud_max: int) -> str: 
    porcentaje = max(salud_actual, 0) / salud_max
    llenos     = int(porcentaje * BARRA_LARGO)
    vacios     = BARRA_LARGO - llenos
    return f"[{'■' * llenos}{'-' * vacios}]"

def mostrar_estado(nombre_h: str, salud_h: int,
                   nombre_e: str, salud_e: int) -> None:
    print("\n╔══════════════════════════════════════╗")
    barra_h = barra_vida(salud_h, SALUD_HEROE_MAX)
    print(f"║  ❤️  {nombre_h:10s} {barra_h} {max(salud_h,0):>3}/{SALUD_HEROE_MAX}")
    barra_e = barra_vida(salud_e, SALUD_ENEMIGO_MAX)
    print(f"║  💀 {nombre_e:10s} {barra_e} {max(salud_e,0):>3}/{SALUD_ENEMIGO_MAX}")
    print("╚══════════════════════════════════════╝")

def verificar_ganador(nombre_h: str, salud_h: int,
                      nombre_e: str, salud_e: int) -> bool:  
    if salud_h <= 0:
        print(f"\n  💀 ¡{nombre_h} ha caído! {nombre_e} gana. FATALITY.")
        return True
    if salud_e <= 0:
        print(f"\n  🏆 ¡{nombre_e} derrotado! ¡{nombre_h} gana. FINISH HIM!")
        return True
    return False

def turno_jugador(nombre_h: str, salud_h: int,
                  nombre_e: str, salud_e: int,
                  pociones: int) -> tuple[int, int, int]:  


    turno_valido = False   

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
            print("  ⛔  Escribe un número: 1, 2 o 3.")
            turno_valido = False
        except KeyboardInterrupt:
            print("  ⛔  Escribe un número: 1, 2 o 3.")
            turno_valido = False
        else:

            if opcion == 1:    
                daño = aplicar_critico(generar_daño(ATAQUE_MIN, ATAQUE_MAX), nombre_h)
                salud_e -= daño   
                print(f"╔══════════════════════════════════════╗")
                print(f"║  ⚔️  {nombre_h} ataca a {nombre_e} (-{daño} HP)")
                print(f"╚══════════════════════════════════════╝")
                turno_valido = True

            elif opcion == 2:     
                if pociones <= 0:
                    print(f"╔══════════════════════════════════════╗")
                    print(f"║  ❌ Sin pociones. Elige otra acción.")
                    print(f"╚══════════════════════════════════════╝")
                    turno_valido = False
                else:
                    pociones -= 1                                     
                    salud_h = min(salud_h + CURACION_HP, SALUD_HEROE_MAX)  
                    print(f"╔══════════════════════════════════════╗")
                    print(f"║  💊 {nombre_h} se cura (+{CURACION_HP} HP)")
                    print(f"╚══════════════════════════════════════╝")
                    turno_valido = True

            elif opcion == 3:                        
                if random.random() < ESPECIAL_FALLO:   
                    print(f"╔══════════════════════════════════════╗")
                    print(f"║  🚫 {nombre_h} intenta especial... ¡FALLA!")
                    print(f"╚══════════════════════════════════════╝")
                else:
                    daño = aplicar_critico(generar_daño(ESPECIAL_MIN, ESPECIAL_MAX), nombre_h)
                    salud_e -= daño    
                    print(f"╔══════════════════════════════════════╗")
                    print(f"║  🌟 ESPECIAL! {nombre_h} inflige -{daño} HP")
                    print(f"╚══════════════════════════════════════╝")
                turno_valido = True

            else:                       
                print("  ⛔  Opción inválida. Escribe 1, 2 o 3.")
                turno_valido = False

    return salud_h, salud_e, pociones

def turno_enemigo(nombre_h: str, salud_h: int,
                  nombre_e: str, salud_e: int) -> tuple[int, int]: 

    if salud_e / SALUD_ENEMIGO_MAX < ENEMIGO_CURA_UMBRAL:   
        salud_e = min(salud_e + CURACION_HP, SALUD_ENEMIGO_MAX) 
        print(f"╔══════════════════════════════════════╗")
        print(f"║  🩹 {nombre_e} está débil y se cura (+{CURACION_HP} HP)")
        print(f"╚══════════════════════════════════════╝")
    else:                                                          
        daño = aplicar_critico(generar_daño(ENEMIGO_MIN, ENEMIGO_MAX), nombre_e)
        salud_h -= daño                                           
        print(f"╔══════════════════════════════════════╗")
        print(f"║  🤬 {nombre_e} ataca a {nombre_h} (-{daño} HP)")
        print(f"╚══════════════════════════════════════╝")

    return salud_h, salud_e