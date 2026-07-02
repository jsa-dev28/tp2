def busqueda_lineal(equipo, nombre_buscado):
    nombre_buscado = nombre_buscado.lower()
    for indice, pokemon in enumerate(equipo):
        if pokemon.nombre.lower() == nombre_buscado:
            return indice, pokemon
    return -1, None


def busqueda_binaria(ids, pokedex, id_buscado):
    izquierda = 0
    derecha = len(ids) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        id_medio = ids[medio]

        if id_medio == id_buscado:
            return pokedex.obtener(id_medio)
        elif id_medio < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None