import random

from pokedex import Pokedex, RegistroMedallas
from entrenadores import Entrenador, GIMNASIOS
from ordenamientos import bubble_sort, insertion_sort, quick_sort
from busquedas import busqueda_lineal, busqueda_binaria
from estructuras import Queue
import pokemon


def pausar():
    input("\nPresioná ENTER para continuar...")

def menu_capturar(pokedex, entrenador):
    print("\nCAPTURAR NUEVO POKÉMON")
    print("Elegí un Pokémon de la Pokédex por su ID, o '0' para capturar uno al azar.")
    entrada = input("ID a capturar: ").strip()

    if entrada == "0":
        pokemon_base = random.choice(pokedex.todos())
    else:
        if not entrada.isdigit():
            print("ID inválido.")
            return
        pokemon_base = pokedex.obtener(int(entrada))
        if pokemon_base is None:
            print("No existe ese ID en la Pokédex.")
            return

    entrenador.capturar_pokemon(pokemon_base)

def submenu_ordenar_pc(entrenador):
    if entrenador.pc.esta_vacia():
        print("La PC está vacía, no hay nada para ordenar.")
        return

    print("\nORDENAR PC")
    print("1. Alfabético")
    print("2. Por Tipo")
    print("3. Por Poder de Combate")
    opcion = input("Elegí una opción: ").strip()

    lista_temporal = entrenador.pc.convertir_lista_python()

    if opcion == "1":
        lista_temporal = bubble_sort(lista_temporal)
        print("PC ordenada alfabéticamente.")
    elif opcion == "2":
        lista_temporal = insertion_sort(lista_temporal)
        print("PC ordenada por tipo.")
    elif opcion == "3":
        lista_temporal = quick_sort(lista_temporal)
        print("PC ordenada por poder de combate (mayor a menor).")
    else:
        print("Opción inválida.")
        return

    entrenador.pc.reconstruir_desde_lista(lista_temporal)
    entrenador.mostrar_pc()


def menu_buscar_equipo(entrenador):
    nombre = input("Nombre del Pokémon a buscar en tu Equipo: ").strip()
    indice, pokemon = busqueda_lineal(entrenador.equipo_principal, nombre)
    if pokemon:
        print(f"Encontrado en la posición {indice + 1} del equipo! {pokemon}")
    else:
        print("Ese Pokémon no está en tu Equipo Principal.")

def menu_consultar_pokedex(pokedex):
    ids = pokedex.ids_ordenados()
    entrada = input("Ingresá el ID a consultar en la Pokédex: ").strip()
    if not entrada.isdigit():
        print("ID inválido.")
        return
    resultado = busqueda_binaria(ids, pokedex, int(entrada))
    if resultado:
        print(f"Encontrado: {resultado}")
    else:
        print("Ese ID no existe en la Pokédex Nacional.")


def menu_centro_pokemon(entrenador):
    print("\nCENTRO POKÉMON")
    print("1. Enviar un Pokémon del equipo a la cola")
    print("2. Procesar cola de curación (sanar a todos)")
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        if not entrenador.equipo_principal:
            print("No tenés Pokémon en tu equipo.")
            return
        entrenador.mostrar_equipo()
        nombre = input("Nombre del Pokémon a enviar: ").strip()
        _, pokemon = busqueda_lineal(entrenador.equipo_principal, nombre)
        if pokemon:
            entrenador.enviar_a_centro_pokemon(pokemon)
        else:
            print("No se encontró ese Pokémon en el equipo.")
    elif opcion == "2":
        entrenador.procesar_centro_pokemon()
    else:
        print("Opción inválida.")


def menu_transferir_oak(entrenador):
    entrenador.mostrar_pc()
    if entrenador.pc.esta_vacia():
        return
    nombre = input("Nombre del Pokémon (de la PC) a transferir al Profesor Oak: ").strip()
    pokemon_encontrado = None
    for pkm in entrenador.pc.convertir_lista_python():
        if pkm.nombre.lower() == nombre.lower():
            pokemon_encontrado = pkm
            break
    if pokemon_encontrado:
        entrenador.transferir_al_profesor_oak(pokemon_encontrado)
    else:
        print("No se encontró ese Pokémon en la PC.")

def menu_gimnasios():
    print("\nGIMNASIOS DISPONIBLES")
    for i, g in enumerate(GIMNASIOS, start=1):
        print(f"{i}. {g['nombre']} - Lider: {g['líder']} - {g['medalla']}")

def mostrar_menu_principal():
    print("POKÉMON HUERGO - MENÚ PRINCIPAL")
    print("1. Ver Pokédex")
    print("2. Ver Equipo Principal")
    print("3. Ver PC")
    print("4. Ver Medallas")
    print("5. Capturar nuevo Pokémon")
    print("6. Ordenar PC")
    print("7. Buscar Pokémon en Equipo")
    print("8. Centro Pokémon (enviar/curar)")
    print("9. Transferir Pokémon al Profesor Oak")
    print("10. Deshacer última transferencia")
    print("11. Desafiar líder de gimnasio")
    print("12. Consultar Pokédex por ID")
    print("0. Salir del sistema")


def main():
    pokedex = Pokedex("pokedex.json")
    registro_medallas = RegistroMedallas("medallas.json")
    entrenador = Entrenador(registro_medallas)

    while True:
        mostrar_menu_principal()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            pokedex.mostrar()
        elif opcion == "2":
            entrenador.mostrar_equipo()
        elif opcion == "3":
            entrenador.mostrar_pc()
        elif opcion == "4":
            registro_medallas.mostrar()
        elif opcion == "5":
            menu_capturar(pokedex, entrenador)
        elif opcion == "6":
            submenu_ordenar_pc(entrenador)
        elif opcion == "7":
            menu_buscar_equipo(entrenador)
        elif opcion == "8":
            menu_centro_pokemon(entrenador)
        elif opcion == "9":
            menu_transferir_oak(entrenador)
        elif opcion == "10":
            entrenador.deshacer_ultima_transferencia()
        elif opcion == "11":
            if len(entrenador.equipo_principal) < 6:
                print("Necesitás tener como mínimo 6 Pokémon en tu equipo para desafiar a un entrenador")
            else: 
                hay_en_centro = False
                for pkm in entrenador.equipo_principal:
                    if pkm in entrenador.centro_pokemon.convertir_lista_python():
                        hay_en_centro = True
                        break

                if hay_en_centro:
                    print("No podés desafiar a un líder mientras tenés Pokémon en el Centro Pokémon.")
                else:
                    menu_gimnasios()
                    seleccion = input("Elegí el número de gimnasio a desafiar: ").strip()
                    if seleccion.isdigit():
                        entrenador.desafiar_gimnasio(int(seleccion) - 1)
                    else:
                        print("Opción inválida.")
        elif opcion == "12":
            menu_consultar_pokedex(pokedex)
        elif opcion == "0":
            print("\nGracias por jugar!")
            break
        else:
            print("Opción inválida, intentá nuevamente.")
        pausar()

if __name__ == "__main__":
    main()