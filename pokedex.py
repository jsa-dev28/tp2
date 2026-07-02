import json
import os
from pokemon import Pokemon

RUTA_DATA = os.path.join(os.path.dirname(__file__), "data")

class Pokedex:
    def __init__(self, ruta_json="pokedex.json"):
        self.registro = {}
        self._cargar_desde_json(ruta_json)

    def _cargar_desde_json(self, ruta_json):
        ruta_completa = os.path.join(RUTA_DATA, ruta_json)
        with open(ruta_completa, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for item in datos:
            pkm = Pokemon(
                id_pokemon=item["id"],
                nombre=item["nombre"],
                tipo=item["tipo"],
                nivel=item.get("nivel", 1),
                hp=item.get("hp", 0),
                ataque=item.get("ataque", 0),
                defensa=item.get("defensa", 0),
                velocidad=item.get("velocidad", 0),
            )
            self.registro[pkm.id] = pkm

    def obtener(self, id_pokemon: int):
        return self.registro.get(id_pokemon)

    def existe(self, id_pokemon: int):
        return id_pokemon in self.registro

    def todos(self):
        return list(self.registro.values())

    def ids_ordenados(self):
        return sorted(self.registro.keys())

    def mostrar(self):
        print("\nPOKÉDEX NACIONAL")
        for pkm in sorted(self.registro.values(), key=lambda p: p.id):
            print(pkm)
        print(f"Total registrados: {len(self.registro)}")


class RegistroMedallas:
    def __init__(self, ruta_json="medallas.json"):
        self.medallas = set()
        self.medallas_totales = []
        self._cargar_desde_json(ruta_json)

    def _cargar_desde_json(self, ruta_json):
        ruta_completa = os.path.join(RUTA_DATA, ruta_json)
        with open(ruta_completa, "r", encoding="utf-8") as f:
            datos = json.load(f)

        self.medallas_totales = datos.get("medallas_totales", [])
        for medalla in datos.get("medallas_obtenidas", []):
            self.medallas.add(medalla)

    def agregar_medalla(self, nombre_medalla: str):
        if nombre_medalla in self.medallas:
            print(f"Ya tenés la '{nombre_medalla}'. No se admiten duplicados.")
            return False
        self.medallas.add(nombre_medalla)
        print(f"¡Conseguiste la {nombre_medalla}!")
        return True

    def mostrar(self):
        print("\nMEDALLAS OBTENIDAS")
        if not self.medallas:
            print("Aún no tenés medallas.")
        for m in self.medallas:
            print(f"- {m}")
        print(f"Progreso: {len(self.medallas)}/{len(self.medallas_totales)}")