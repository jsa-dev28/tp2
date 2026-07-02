def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if lista[j].nombre.lower() > lista[j + 1].nombre.lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista


def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j].tipo_principal().lower() > actual.tipo_principal().lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista


def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]
    mayores = [p for p in lista if p.poder_combate > pivote.poder_combate]
    iguales = [p for p in lista if p.poder_combate == pivote.poder_combate]
    menores = [p for p in lista if p.poder_combate < pivote.poder_combate]

    return quick_sort(mayores) + iguales + quick_sort(menores)