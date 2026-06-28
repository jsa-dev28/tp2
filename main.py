import random

from pokedex import Pokedex, RegistroMedallas
from entrenadores import Entrenador, GIMNASIOS
from ordenamientos import bubble_sort_por_nombre, insertion_sort_por_tipo, quick_sort_por_poder
from busquedas import busqueda_lineal_en_equipo, busqueda_binaria_en_pokedex


def pausar():
    input("\nPresiona ENTER para continuar...")

def menu_capturar(pokedex, entrenador):
    print("\n--- CAPTURAR NUEVO POKEMON ---")
    print("Elegi un Pokemon de la Pokedex por su ID, o '0' para capturar uno al azar.")
    entrada = input("ID a capturar: ").strip()

    if entrada == "0":
        pokemon_base = random.choice(pokedex.todos())
    else:
        if not entrada.isdigit():
            print(">> ID invalido.")
            return
        pokemon_base = pokedex.obtener(int(entrada))
        if pokemon_base is None:
            print(">> No existe ese ID en la Pokedex.")
            return

    entrenador.capturar_pokemon(pokemon_base)


def submenu_ordenar_pc(entrenador):
    if entrenador.pc.esta_vacia():
        print(">> La PC esta vacia, no hay nada para ordenar.")
        return

    print("\n--- ORDENAR PC ---")
    print("1. Alfabetico")
    print("2. Por Tipo")
    print("3. Por Poder de Combate")
    opcion = input("Elegi una opcion: ").strip()

    lista_temporal = entrenador.pc.convertir_lista_python()

    if opcion == "1":
        lista_temporal = bubble_sort_por_nombre(lista_temporal)
        print(">> PC ordenada alfabeticamente.")
    elif opcion == "2":
        lista_temporal = insertion_sort_por_tipo(lista_temporal)
        print(">> PC ordenada por tipo.")
    elif opcion == "3":
        lista_temporal = quick_sort_por_poder(lista_temporal)
        print(">> PC ordenada por poder de combate (mayor a menor).")
    else:
        print(">> Opcion invalida.")
        return

    entrenador.pc.reconstruir_desde_lista(lista_temporal)
    entrenador.mostrar_pc()


def menu_buscar_equipo(entrenador):
    nombre = input("Nombre del Pokemon a buscar en tu Equipo: ").strip()
    indice, pokemon = busqueda_lineal_en_equipo(entrenador.equipo_principal, nombre)
    if pokemon:
        print(f">> Encontrado en la posicion {indice + 1} del equipo! {pokemon}")
    else:
        print(">> Ese Pokemon no esta en tu Equipo Principal.")


def menu_consultar_pokedex(pokedex):
    ids_ordenados = pokedex.ids_ordenados()
    entrada = input("Ingresa el ID a consultar en la Pokedex: ").strip()
    if not entrada.isdigit():
        print(">> ID invalido.")
        return
    resultado = busqueda_binaria_en_pokedex(ids_ordenados, pokedex, int(entrada))
    if resultado:
        print(f">> Encontrado: {resultado}")
    else:
        print(">> Ese ID no existe en la Pokedex Nacional.")


def menu_centro_pokemon(entrenador):
    print("\n--- CENTRO POKEMON ---")
    print("1. Enviar un Pokemon del equipo a la cola")
    print("2. Procesar cola de curacion (sanar a todos)")
    opcion = input("Elegi una opcion: ").strip()

    if opcion == "1":
        entrenador.mostrar_equipo()
        nombre = input("Nombre del Pokemon a enviar: ").strip()
        _, pokemon = busqueda_lineal_en_equipo(entrenador.equipo_principal, nombre)
        if pokemon:
            entrenador.enviar_a_centro_pokemon(pokemon)
        else:
            print(">> No se encontro ese Pokemon en el equipo.")
    elif opcion == "2":
        entrenador.procesar_centro_pokemon()
    else:
        print(">> Opcion invalida.")


def menu_transferir_oak(entrenador):
    entrenador.mostrar_pc()
    if entrenador.pc.esta_vacia():
        return
    nombre = input("Nombre del Pokemon (de la PC) a transferir al Profesor Oak: ").strip()
    pokemon_encontrado = None
    for pkm in entrenador.pc:
        if pkm.nombre.lower() == nombre.lower():
            pokemon_encontrado = pkm
            break
    if pokemon_encontrado:
        entrenador.transferir_al_profesor_oak(pokemon_encontrado)
    else:
        print(">> No se encontro ese Pokemon en la PC.")


def menu_gimnasios():
    print("\n--- GIMNASIOS DISPONIBLES ---")
    for i, g in enumerate(GIMNASIOS, start=1):
        print(f"{i}. {g['nombre']} - Lider: {g['lider']} - {g['medalla']}")


def mostrar_menu_principal():
    print("POKEMON HUERGO - MENU PRINCIPAL")
    print("1. Ver Pokédex")
    print("2. Ver Equipo Principal")
    print("3. Ver PC")
    print("4. Ver Medallas")
    print("5. Capturar nuevo Pokemon")
    print("6. Ordenar PC")
    print("7. Buscar Pokemon en Equipo")
    print("8. Centro Pokemon (enviar/curar)")
    print("9. Transferir Pokemon al Profesor Oak")
    print("10. Deshacer ultima transferencia")
    print("11. Desafiar Lider de Gimnasio")
    print("12. Consultar Pokedex por ID")
    print("0. Salir del sistema")


def main():
    pokedex = Pokedex("pokedex.json")
    registro_medallas = RegistroMedallas("medallas.json")
    entrenador = Entrenador(registro_medallas)

    while True:
        mostrar_menu_principal()
        opcion = input("Elegi una opcion: ").strip()

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
            menu_gimnasios()
            seleccion = input("Elegi el numero de gimnasio a desafiar: ").strip()
            if seleccion.isdigit():
                entrenador.desafiar_gimnasio(int(seleccion) - 1)
            else:
                print(">> Opción inválida.")
        elif opcion == "12":
            menu_consultar_pokedex(pokedex)
        elif opcion == "0":
            print("\nGracias por jugar!")
            break
        else:
            print(">> Opción inválida, intenta nuevamente.")

        pausar()


if __name__ == "__main__":
    main()