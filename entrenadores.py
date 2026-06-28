import random
from estructuras import ListaEnlazada, QueueCentroPokemon, StackTransferencias

GIMNASIOS = [
    {"nombre": "Ciudad Plateada", "lider": "Brock", "medalla": "Medalla Roca"},
    {"nombre": "Ciudad Celeste", "lider": "Misty", "medalla": "Medalla Cascada"},
    {"nombre": "Ciudad Carmín", "lider": "Teniente Surge", "medalla": "Medalla Trueno"},
    {"nombre": "Ciudad Azulona", "lider": "Erika", "medalla": "Medalla Arcoiris"},
    {"nombre": "Ciudad Azafran", "lider": "Sabrina", "medalla": "Medalla Pantano"},
    {"nombre": "Ciudad Fucsia", "lider": "Koga", "medalla": "Medalla Alma"},
    {"nombre": "Ciudad Canela", "lider": "Blaine", "medalla": "Medalla Volcan"},
    {"nombre": "Ciudad Verde", "lider": "Giovanni", "medalla": "Medalla Tierra"},
]

LIMITE_EQUIPO = 6

class Entrenador:
    def __init__(self, registro_medallas):
        self.equipo_principal = []
        self.pc = ListaEnlazada()
        self.centro_pokemon = QueueCentroPokemon()
        self.pila_transferencias = StackTransferencias()
        self.medallas = registro_medallas

    def capturar_pokemon(self, pokemon):
        if len(self.equipo_principal) < LIMITE_EQUIPO:
            self.equipo_principal.append(pokemon)
            print(f">> {pokemon.nombre} se unio al Equipo Principal ({len(self.equipo_principal)}/{LIMITE_EQUIPO}).")
        else:
            self.pc.insertar_al_final(pokemon)
            print(f">> Equipo Principal lleno (6/6). {pokemon.nombre} fue derivado automaticamente a la PC.")

    def enviar_a_centro_pokemon(self, pokemon):
        if pokemon not in self.equipo_principal:
            print(">> Ese Pokemon no esta en tu Equipo Principal.")
            return
        self.centro_pokemon.enqueue(pokemon)
        print(f">> {pokemon.nombre} ingreso a la fila del Centro Pokemon.")

    def procesar_centro_pokemon(self):
        if self.centro_pokemon.esta_vacia():
            print(">> No hay Pokemon esperando en el Centro Pokemon.")
            return
        print("\n===== CURANDO EQUIPO =====")
        while not self.centro_pokemon.esta_vacia():
            pkm = self.centro_pokemon.dequeue()
            print(f"Curando a {pkm.nombre}... ¡Listo! {pkm.nombre} esta totalmente sano.")
        print("===== Todo el equipo en cola ha sido sanado =====")

    def transferir_al_profesor_oak(self, pokemon):
        if not self.pc.eliminar(pokemon):
            print(">> Ese Pokemon no se encuentra en la PC.")
            return
        self.pila_transferencias.push(pokemon)
        print(f">> {pokemon.nombre} fue transferido al Profesor Oak.")

    def deshacer_ultima_transferencia(self):
        pokemon = self.pila_transferencias.pop()
        if pokemon is None:
            print(">> No hay transferencias recientes para deshacer.")
            return
        self.pc.insertar_al_final(pokemon)
        print(f">> Se recupero a {pokemon.nombre} y volvio a la PC.")

    def desafiar_gimnasio(self, indice_gimnasio):
        if indice_gimnasio < 0 or indice_gimnasio >= len(GIMNASIOS):
            print(">> Gimnasio invalido.")
            return
        gimnasio = GIMNASIOS[indice_gimnasio]
        print(f"\n>> Desafiando a {gimnasio['lider']} en el Gimnasio de {gimnasio['nombre']}...")
        gano = random.choice([True, False])
        if gano:
            print(f">> ¡Has derrotado a {gimnasio['lider']}!")
            self.medallas.agregar_medalla(gimnasio["medalla"])
        else:
            print(f">> Has sido derrotado por {gimnasio['lider']}. Intenta de nuevo mas tarde.")

    def mostrar_equipo(self):
        print("\n===== EQUIPO PRINCIPAL =====")
        if not self.equipo_principal:
            print("No tienes Pokemon en tu equipo.")
        for i, pkm in enumerate(self.equipo_principal, start=1):
            print(f"{i}. {pkm}")

    def mostrar_pc(self):
        print("\n===== PC =====")
        if self.pc.esta_vacia():
            print("La PC esta vacia.")
        for i, pkm in enumerate(self.pc, start=1):
            print(f"{i}. {pkm}")
        print(f"Total en PC: {len(self.pc)}")