def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")

    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    emisiones_totales = 0
    consumo_total = 0
    planta_mayor_consumo = None
    consumo_maximo = -1

    registros_procesados = []

    for registro in registros:
        consumo = registro["consumo_kwh"]

        emisiones = calcular_emisiones_carbono(consumo)

        consumo_total += consumo
        emisiones_totales += emisiones

        registros_procesados.append({
            "planta": registro["planta"],
            "consumo_kwh": consumo,
            "emisiones": emisiones
        })

        if consumo > consumo_maximo:
            consumo_maximo = consumo
            planta_mayor_consumo = registro["planta"]

    cantidad_plantas = len(registros)

    if cantidad_plantas > 0:
        consumo_promedio = consumo_total / cantidad_plantas
    else:
        consumo_promedio = 0

    return {
        "emisiones_totales": emisiones_totales,
        "consumo_total": consumo_total,
        "consumo_promedio": consumo_promedio,
        "cantidad_plantas": cantidad_plantas,
        "planta_mayor_consumo": planta_mayor_consumo,
        "consumo_maximo": consumo_maximo,
        "factor_emision": 0.4,
        "registros": registros_procesados
    }