# ⚔️ MORTAL KOMBAT
### by. RIWI

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Academic-orange)

> **ES:** Simulador de combate por turnos desarrollado en Python puro — sin librerías externas.
> **EN:** Turn-based combat simulator developed in pure Python — no external libraries.

---

## 📋 Descripción / Description

**ES:**
MORTAL KOMBAT es un simulador de combate por turnos desarrollado en Python donde dos luchadores se enfrentan en una batalla estratégica. El jugador elige sus acciones cada turno — atacar, curar o lanzar una habilidad especial — mientras el enemigo responde con inteligencia artificial básica. El combate termina cuando uno de los dos combatientes llega a 0 HP.

**EN:**
MORTAL KOMBAT is a turn-based combat simulator developed in Python where two fighters face each other in a strategic battle. The player chooses their actions each turn — attack, heal, or launch a special ability — while the enemy responds with basic artificial intelligence. The combat ends when one of the two fighters reaches 0 HP.

---

## ⚙️ Funcionalidades / Features

| | Funcionalidad | Descripción ES | Description EN |
|---|---|---|---|
| ⚔️ | Atacar | Daño aleatorio entre 10 y 25 HP | Random damage between 10 and 25 HP |
| 💊 | Curar | Recupera 20 HP (máx. 3 pociones) | Recovers 20 HP (max. 3 potions) |
| 🌟 | Habilidad Especial | Daño entre 30–50 HP, 50% de fallar | Damage between 30–50 HP, 50% chance to fail |
| ⚡ | Golpe Crítico | 10% de probabilidad de duplicar el daño | 10% chance to double the damage |
| 🧠 | IA del Enemigo | Se cura si su vida baja del 20% | Heals itself if health drops below 20% |
| 📊 | Barra de vida | Muestra HP con barra visual `[####----]` | Displays HP with visual bar `[####----]` |
| ✅ | Validación | Maneja letras, Ctrl+C y nombres vacíos | Handles letters, Ctrl+C and empty names |

---

## 🚀 Instalación y uso / Installation & usage

**ES:** No requiere instalación de librerías externas. Solo necesitas Python 3.x.

**EN:** No external libraries required. You only need Python 3.x.

```bash
# Clona el repositorio / Clone the repository
git clone https://github.com/tu-usuario/mortal-kombat-riwi.git

# Entra a la carpeta / Enter the folder
cd mortal-kombat-riwi

# Ejecuta el juego / Run the game
python GAME_MORTAL_KOMBAT.py
```

---

## 📁 Estructura del proyecto / Project structure

```
📁 SIMULADOR DE KOMBAT
├── GAME_MORTAL_KOMBAT.py    # Flujo principal del juego / Main game flow
├── MOTOR_DEL_SIMULADOR.py   # Funciones y constantes / Functions and constants
└── README.md                # Documentación / Documentation
```

---

## 🏗️ Arquitectura / Architecture

**ES:** El proyecto aplica separación de responsabilidades en dos módulos:
- `MOTOR_DEL_SIMULADOR.py` — contiene toda la lógica: funciones, cálculos, IA y constantes.
- `GAME_MORTAL_KOMBAT.py` — contiene únicamente el flujo del juego: bienvenida, bucle principal y despedida.

**EN:** The project applies separation of concerns across two modules:
- `MOTOR_DEL_SIMULADOR.py` — contains all logic: functions, calculations, AI and constants.
- `GAME_MORTAL_KOMBAT.py` — contains only the game flow: welcome screen, main loop and farewell.

---

## 🏫 Contexto académico / Academic context

> Proyecto desarrollado en **RIWI** como ejercicio de programación modular en Python.
> Project developed at **RIWI** as a modular programming exercise in Python.

---

*⚔️ MORTAL KOMBAT — by. RIWI*
