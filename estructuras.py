class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class LinkedList:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamaño += 1

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1

    def eliminar(self, pokemon):
        actual = self.cabeza
        previo = None
        while actual is not None:
            if actual.dato is pokemon:
                if previo is None:
                    self.cabeza = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
                self.tamaño -= 1
                return True
            previo = actual
            actual = actual.siguiente
        return False

    def convertir_lista_python(self):
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def reconstruir_desde_lista(self, lista_python):
        self.cabeza = None
        self.tamaño = 0
        for dato in lista_python:
            self.insertar_al_final(dato)

    def esta_vacia(self):
        return self.cabeza is None

    def __len__(self):
        return self.tamaño

class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, pokemon):
        self._queue.append(pokemon)

    def dequeue(self):
        if self.esta_vacia():
            return None
        return self._queue.pop(0)

    def esta_vacia(self):
        return len(self._queue) == 0

    def __len__(self):
        return len(self._queue)
    
    def convertir_lista_python(self):
        return list(self._queue)

class Stack:
    LIMITE = 5

    def __init__(self):
        self._stack = []

    def push(self, pokemon):
        if len(self._stack) >= self.LIMITE:
            self._stack.pop(0)
        self._stack.append(pokemon)

    def pop(self):
        if self.esta_vacia():
            return None
        return self._stack.pop()

    def esta_vacia(self):
        return len(self._stack) == 0

    def __len__(self):
        return len(self._stack)
