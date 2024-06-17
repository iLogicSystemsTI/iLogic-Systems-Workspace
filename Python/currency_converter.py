import requests


def obtener_tasa_de_cambio(moneda_origen, moneda_destino):
    api_key = "TU_API_KEY"
    url = f"https://api.exchangerate-api.com/v4/latest/{moneda_origen}"
    response = requests.get(url)
    datos = response.json()
    tasa = datos.get("rates", {}).get(moneda_destino)
    return tasa


def convertir_moneda(cantidad, moneda_origen, moneda_destino):
    tasa = obtener_tasa_de_cambio(moneda_origen, moneda_destino)
    return cantidad * tasa


cantidad = 100
moneda_origen = "USD"
moneda_destino = "EUR"
resultado = convertir_moneda(cantidad, moneda_origen, moneda_destino)
print(f"{cantidad} {moneda_origen} son {resultado:.2f} {moneda_destino}")
