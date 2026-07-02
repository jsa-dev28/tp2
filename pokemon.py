class Pokemon:
    def __init__(self, id_pokemon: int, nombre: str, tipo, nivel: int = 1, hp: int = 0, ataque: int = 0, defensa: int = 0, velocidad: int = 0):
        self.id = id_pokemon
        self.nombre = nombre
        self.tipo = tipo if isinstance(tipo, list) else [tipo]
        self.nivel = nivel
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.poder_combate = hp + ataque + defensa + velocidad
        
    def tipo_principal(self):
        return self.tipo[0] if self.tipo else "Desconocido"

    def tipo_str(self):
        return "/".join(self.tipo)

    def __repr__(self):
        return (f"#{self.id} {self.nombre} ({self.tipo_str()}) "
                f"Nv.{self.nivel} - PC:{self.poder_combate} "
                f"(HP:{self.hp} ATK:{self.ataque} DEF:{self.defensa} VEL:{self.velocidad})")

    def __str__(self):
        return self.__repr__()

    def dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "nivel": self.nivel,
            "hp": self.hp,
            "ataque": self.ataque,
            "defensa": self.defensa,
            "velocidad": self.velocidad,
            "poder_combate": self.poder_combate,
        }