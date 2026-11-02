# TP Final EcoTech Solutions

**Alumna: Andrea Florencia Illanes**

Este trabajo práctico final está hecho en Python y Django.

La idea fue resolver los tres ejercicios por separado, tratando de mantener el proyecto ordenado y que cada parte se pueda ejecutar sin problemas.

## Estructura del proyecto

```text
TP-Final-EcoTech/
│
├── ejercicio_1/
│   └── sensores.py
│
├── ejercicio_2/
│   ├── inventario.py
│   └── catalogo_ecotech.json
│
├── ejercicio_3/
│   ├── manage.py
│   ├── ecotech/
│   └── sustentabilidad/
│
├── README.md
└── .gitignore
```

## Ejercicio 1

### Sanitización y análisis de sensores

En este ejercicio se trabaja con registros de sensores que pueden venir con datos desordenados o incompletos.

Lo que hace el programa es:

- limpiar los espacios del identificador;
- convertir la temperatura a un valor numérico;
- colocar una ubicación por defecto si no viene informada;
- calcular el promedio de temperatura;
- detectar qué sensores superan el umbral definido;
- mostrar un reporte final por consola.

### Para ejecutarlo

```bash
cd ejercicio_1
python sensores.py
```

## Ejercicio 2

### Productos, stock y archivo JSON

En este ejercicio se armó un pequeño catálogo de dispositivos ecológicos usando programación orientada a objetos.

Se trabajó con:

- una clase base llamada `DispositivoEcologico`;
- una clase `PanelSolar` que hereda de la anterior;
- control del stock para evitar valores negativos;
- una excepción personalizada `StockInvalidoError`;
- polimorfismo en la ficha técnica;
- guardado de los productos en un archivo JSON.

### Para ejecutarlo

```bash
cd ejercicio_2
python inventario.py
```

Al ejecutarlo se genera el archivo:

```text
catalogo_ecotech.json
```

Ese archivo guarda la informacion de los productos creados en el programa.

## Ejercicio 3

### Tests y panel web con Django

En el tercer ejercicio se trabaja con el cálculo de emisiones de carbono y después se muestra esa información en una página hecha con Django.

Incluye:

- función `calcular_emisiones_carbono`;
- control de consumos negativos;
- tests unitarios con `unittest`;
- cálculo de emisiones totales;
- búsqueda de la planta con mayor consumo;
- vista en Django;
- panel web de sustentabilidad.

### Ejecutar los tests

```bash
cd ejercicio_3
python manage.py test
```

### Levantar el servidor

```bash
python manage.py runserver
```

Después abrir en el navegador:

```text
http://127.0.0.1:8000/sustentabilidad/
```

## Tecnologías usadas

- Python
- JSON
- unittest
- Django
- HTML
- CSS

## Comentario final

El objetivo del trabajo fue aplicar varios de los temas vistos durante la cursada en un mismo proyecto. Cada ejercicio apunta a algo distinto, pero todos están relacionados con el caso de EcoTech Solutions.

Se intento mantener el código simple y entendible, sin agregar funcionalidades que no fueran necesarias para cumplir con la consigna.