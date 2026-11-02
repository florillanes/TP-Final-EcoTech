def limpiar_registro_sensor(registro_raw):
    """
    Limpia y normaliza un registro crudo de sensor.
    """

    # Limpia espacios del identificador
    sensor_id = registro_raw.get("sensor_id", "").strip()

    # Obtiene la temperatura y elimina la unidad
    temperatura_raw = str(
        registro_raw.get("temperatura", "0")
    ).strip()

    temperatura_limpia = (
        temperatura_raw
        .replace("°C", "")
        .replace("C", "")
        .strip()
    )

    # Convierte la temperatura a float
    temperatura = float(temperatura_limpia)

    # Obtiene la ubicación
    ubicacion = registro_raw.get("ubicacion")

    # Si no tiene ubicación, asigna un valor por defecto
    if ubicacion is None or str(ubicacion).strip() == "":
        ubicacion = "Ubicación desconocida"
    else:
        ubicacion = str(ubicacion).strip()

    # Devuelve un nuevo diccionario limpio
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


def generar_resumen_sensores(
    lista_sensores_limpios,
    umbral_temperatura
):
    """
    Genera el resumen solicitado por la consigna.

    Retorna una tupla:
    (
        lista de IDs de sensores en alerta,
        temperatura promedio
    )
    """

    sensores_alerta = []
    suma_temperaturas = 0

    # Recorremos todos los sensores
    for sensor in lista_sensores_limpios:

        temperatura = sensor["temperatura"]

        # Sumamos las temperaturas
        suma_temperaturas += temperatura

        # Comprobamos si supera el umbral
        if temperatura > umbral_temperatura:
            sensores_alerta.append(
                sensor["sensor_id"]
            )

    cantidad_sensores = len(
        lista_sensores_limpios
    )

    # Evita una división por cero
    if cantidad_sensores > 0:
        promedio_temperatura = (
            suma_temperaturas / cantidad_sensores
        )
    else:
        promedio_temperatura = 0

    # La consigna pide especificamente esta tupla
    return sensores_alerta, promedio_temperatura


def generar_estadisticas_adicionales(
    lista_sensores_limpios,
    umbral_temperatura
):
    """
    Genera informacion adicional para completar
    el reporte sin modificar la función pedida
    en la consigna.
    """

    cantidad_sensores = len(
        lista_sensores_limpios
    )

    # Si no existen sensores se devuelven valores vacíos
    if cantidad_sensores == 0:
        return {
            "cantidad_sensores": 0,
            "temperatura_minima": 0,
            "temperatura_maxima": 0,
            "sensor_mas_caliente": None,
            "cantidad_alertas": 0,
            "porcentaje_alerta": 0
        }

    temperaturas = []
    sensores_alerta = []

    temperatura_maxima = None
    sensor_mas_caliente = None

    # Analizamos cada sensor
    for sensor in lista_sensores_limpios:

        temperatura = sensor["temperatura"]

        temperaturas.append(temperatura)

        # Sensores por encima del umbral
        if temperatura > umbral_temperatura:
            sensores_alerta.append(
                sensor["sensor_id"]
            )

        # Busca la temperatura máxima
        if (
            temperatura_maxima is None
            or temperatura > temperatura_maxima
        ):
            temperatura_maxima = temperatura
            sensor_mas_caliente = sensor["sensor_id"]

    temperatura_minima = min(temperaturas)

    cantidad_alertas = len(
        sensores_alerta
    )

    porcentaje_alerta = (
        cantidad_alertas
        / cantidad_sensores
    ) * 100

    return {
        "cantidad_sensores": cantidad_sensores,
        "temperatura_minima": temperatura_minima,
        "temperatura_maxima": temperatura_maxima,
        "sensor_mas_caliente": sensor_mas_caliente,
        "cantidad_alertas": cantidad_alertas,
        "porcentaje_alerta": porcentaje_alerta
    }


# ------------------------------------------------
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ------------------------------------------------

if __name__ == "__main__":

    # Datos crudos recibidos desde los sensores
    registros_crudos = [
        {
            "sensor_id": " SENSOR-001 ",
            "temperatura": "24.5C",
            "ubicacion": "Planta Norte"
        },
        {
            "sensor_id": "SENSOR-002",
            "temperatura": " 31.2°C ",
            "ubicacion": "Planta Sur"
        },
        {
            "sensor_id": " SENSOR-003 ",
            "temperatura": "28C",
            "ubicacion": ""
        },
        {
            "sensor_id": "SENSOR-004",
            "temperatura": "35.7C"
        },
        {
            "sensor_id": " SENSOR-005 ",
            "temperatura": "26.8C",
            "ubicacion": "Depósito"
        },
        {
            "sensor_id": " SENSOR-006 ",
            "temperatura": "33.4°C",
            "ubicacion": "Área de Producción"
        }
    ]

    sensores_limpios = []

    # ------------------------------------------------
    # LIMPIEZA DE LOS REGISTROS
    # ------------------------------------------------

    for registro in registros_crudos:

        sensor_limpio = limpiar_registro_sensor(
            registro
        )

        sensores_limpios.append(
            sensor_limpio
        )


    # ------------------------------------------------
    # MOSTRAR REGISTROS NORMALIZADOS
    # ------------------------------------------------

    print("\n======================================")
    print("       REGISTROS NORMALIZADOS")
    print("======================================")

    for sensor in sensores_limpios:

        print(
            f"ID: {sensor['sensor_id']} | "
            f"Temperatura: {sensor['temperatura']} °C | "
            f"Ubicación: {sensor['ubicacion']}"
        )


    # ------------------------------------------------
    # CONFIGURACIÓN DEL UMBRAL
    # ------------------------------------------------

    umbral = 30


    # ------------------------------------------------
    # RESUMEN PEDIDO POR LA CONSIGNA
    # ------------------------------------------------

    sensores_alerta, promedio = (
        generar_resumen_sensores(
            sensores_limpios,
            umbral
        )
    )


    # ------------------------------------------------
    # ESTADÍSTICAS ADICIONALES
    # ------------------------------------------------

    estadisticas = (
        generar_estadisticas_adicionales(
            sensores_limpios,
            umbral
        )
    )


    # ------------------------------------------------
    # REPORTE FINAL
    # ------------------------------------------------

    print("\n======================================")
    print("           REPORTE GENERAL")
    print("======================================")

    print(
        f"Cantidad total de sensores: "
        f"{estadisticas['cantidad_sensores']}"
    )

    print(
        f"Umbral de temperatura: "
        f"{umbral} °C"
    )

    print(
        f"Temperatura promedio: "
        f"{promedio:.2f} °C"
    )

    print(
        f"Temperatura mínima: "
        f"{estadisticas['temperatura_minima']} °C"
    )

    print(
        f"Temperatura máxima: "
        f"{estadisticas['temperatura_maxima']} °C"
    )

    print(
        f"Sensor con mayor temperatura: "
        f"{estadisticas['sensor_mas_caliente']}"
    )


    # ------------------------------------------------
    # ALERTAS
    # ------------------------------------------------

    print("\n======================================")
    print("                ALERTAS")
    print("======================================")

    if len(sensores_alerta) > 0:

        print(
            f"Sensores que superan "
            f"{umbral} °C:"
        )

        for sensor_id in sensores_alerta:
            print(f"- {sensor_id}")

    else:
        print(
            "No existen sensores por encima "
            "del umbral."
        )

    print(
        f"\nCantidad de sensores en alerta: "
        f"{estadisticas['cantidad_alertas']}"
    )

    print(
        f"Porcentaje de sensores en alerta: "
        f"{estadisticas['porcentaje_alerta']:.2f}%"
    )


    # ------------------------------------------------
    # ESTADO INDIVIDUAL DE CADA SENSOR
    # ------------------------------------------------

    print("\n======================================")
    print("       ESTADO DE LOS SENSORES")
    print("======================================")

    for sensor in sensores_limpios:

        if sensor["temperatura"] > umbral:
            estado = "ALERTA"
        else:
            estado = "NORMAL"

        print(
            f"{sensor['sensor_id']} | "
            f"{sensor['temperatura']} °C | "
            f"{estado}"
        )


    print("\n======================================")
    print("       FIN DEL REPORTE")
    print("======================================")