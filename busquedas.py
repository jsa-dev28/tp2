def busqueda_lineal_en_equipo(equipo, nombre_buscado):
    nombre_buscado = nombre_buscado.lower()
    for indice, pokemon in enumerate(equipo):
        if pokemon.nombre.lower() == nombre_buscado:
            return indice, pokemon
    return -1, None


def busqueda_binaria_en_pokedex(ids_ordenados, pokedex, id_buscado):
    izquierda = 0
    derecha = len(ids_ordenados) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        id_medio = ids_ordenados[medio]

        if id_medio == id_buscado:
            return pokedex.obtener(id_medio)
        elif id_medio < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None