from django.shortcuts import render
from .emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):

    registros = [
        {
            "planta": "Planta Norte",
            "consumo_kwh": 1200
        },
        {
            "planta": "Planta Sur",
            "consumo_kwh": 1800
        },
        {
            "planta": "Planta Centro",
            "consumo_kwh": 950
        }
    ]

    metricas = obtener_metricas_consumo(registros)

    contexto = {
        "emisiones_totales": metricas["emisiones_totales"],
        "consumo_total": metricas["consumo_total"],
        "consumo_promedio": metricas["consumo_promedio"],
        "cantidad_plantas": metricas["cantidad_plantas"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "consumo_maximo": metricas["consumo_maximo"],
        "factor_emision": metricas["factor_emision"],
        "registros": metricas["registros"]
    }

    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )