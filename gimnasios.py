LIDERES = [
    {"nombre": "Brock", "tipo": "Roca", "pc_total": 800, "medalla": "Medalla Roca"},
    {"nombre": "Misty", "tipo": "Agua", "pc_total": 1000, "medalla": "Medalla Cascada"},
    {"nombre": "Teniente Surge", "tipo": "Eléctrico", "pc_total": 1200, "medalla": "Medalla Rayo"},
    {"nombre": "Erika", "tipo": "Planta", "pc_total": 1400, "medalla": "Medalla Pétalo"},
    {"nombre": "Koga", "tipo": "Veneno", "pc_total": 1600, "medalla": "Medalla Veneno"},
    {"nombre": "Sabrina", "tipo": "Psíquico", "pc_total": 1800, "medalla": "Medalla Marsh"},
    {"nombre": "Blaine", "tipo": "Fuego", "pc_total": 2000, "medalla": "Medalla Volcán"},
    {"nombre": "Giovanni", "tipo": "Tierra", "pc_total": 2200, "medalla": "Medalla Tierra"},
]


def obtener_lider_por_indice(indice):
    if 0 <= indice < len(LIDERES):
        return LIDERES[indice]
    return None