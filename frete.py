def calcular_frete(tipo, peso_kg):
    if tipo == "PAC":
        return 10.00 + 2.00 * peso_kg
    elif tipo == "SEDEX":
        return 20.00 + 4.00 * peso_kg
    elif tipo == "RETIRADA":
        return 0.00
    else:
        raise ValueError(f"Tipo de entrega desconhecido: {tipo}")