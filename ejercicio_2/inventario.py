import json


class StockInvalidoError(Exception):
    """Error para valores de stock negativos."""
    pass


class DispositivoEcologico:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(
                "El stock no puede ser negativo."
            )

        self._stock = valor

    def ficha_tecnica(self):
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio} | "
            f"Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "tipo": "DispositivoEcologico",
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }


class PanelSolar(DispositivoEcologico):
    def __init__(
        self,
        nombre,
        precio,
        stock,
        potencia_watts,
        eficiencia,
        marca
    ):
        super().__init__(
            nombre,
            precio,
            stock
        )

        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia
        self.marca = marca

    # Se redefine la ficha tecnica para el panel solar
    def ficha_tecnica(self):
        return (
            f"Panel: {self.nombre} | "
            f"Marca: {self.marca} | "
            f"Potencia: {self.potencia_watts} W | "
            f"Eficiencia: {self.eficiencia}% | "
            f"Precio: ${self.precio} | "
            f"Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "tipo": "PanelSolar",
            "nombre": self.nombre,
            "marca": self.marca,
            "precio": self.precio,
            "stock": self.stock,
            "potencia_watts": self.potencia_watts,
            "eficiencia": self.eficiencia,
            "disponible": self.stock > 0
        }


class GestorInventario:

    def guardar_catalogo_json(
        self,
        lista_dispositivos,
        ruta_archivo
    ):
        datos = []

        for dispositivo in lista_dispositivos:
            datos.append(
                dispositivo.to_dict()
            )

        with open(
            ruta_archivo,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )


if __name__ == "__main__":

    # Creamos algunos productos para probar el catalogo
    catalogo = []

    panel_1 = PanelSolar(
        "EcoPanel 400",
        250000,
        10,
        400,
        21.5,
        "EcoTech"
    )

    panel_2 = PanelSolar(
        "EcoPanel 550",
        340000,
        5,
        550,
        22.3,
        "EcoTech"
    )

    panel_3 = PanelSolar(
        "EcoPanel 300",
        190000,
        8,
        300,
        20.8,
        "SolarGreen"
    )

    catalogo.append(panel_1)
    catalogo.append(panel_2)
    catalogo.append(panel_3)

    print("\nCATALOGO ECOTECH")
    print("------------------------------")

    for dispositivo in catalogo:
        print(dispositivo.ficha_tecnica())


    # Probamos que no se pueda guardar un stock negativo
    print("\nPRUEBA DE STOCK INVALIDO")
    print("------------------------------")

    try:
        panel_1.stock = -4

    except StockInvalidoError as error:
        print(f"Error controlado: {error}")


    # Guardamos los productos validos en el archivo json
    gestor = GestorInventario()

    gestor.guardar_catalogo_json(
        catalogo,
        "catalogo_ecotech.json"
    )

    print("\nEXPORTACION")
    print("------------------------------")

    print(
        "Catálogo guardado correctamente "
        "en catalogo_ecotech.json"
    )