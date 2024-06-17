import pyautogui, pyperclip
import time

# Código que queremos escribir
code = """import requests


def obtener_tasa_de_cambio(moneda_origen, moneda_destino):
    api_key = 'TU_API_KEY'
    url = f'https://api.exchangerate-api.com/v4/latest/{moneda_origen}'
    response = requests.get(url)
    datos = response.json()
    tasa = datos.get('rates', {}).get(moneda_destino)
    return tasa


def convertir_moneda(cantidad, moneda_origen, moneda_destino):
    tasa = obtener_tasa_de_cambio(moneda_origen, moneda_destino)
    return cantidad * tasa


cantidad = 100
moneda_origen = "USD"
moneda_destino = "EUR"
resultado = convertir_moneda(cantidad, moneda_origen, moneda_destino)
print(f'{cantidad} {moneda_origen} son {resultado:.2f} {moneda_destino}')"""


def type_code(code, typing_speed=0.001):
    for char in code:
        if char in "+<#{}[]":
            # Copiar el carácter al portapapeles y pegarlo
            pyperclip.copy(char)
            time.sleep(
                0.1
            )  # Pausa breve para asegurar que el portapapeles se actualice
            pyautogui.hotkey("ctrl", "v")
            # pyautogui.press("backspace")
        else:
            pyautogui.write(char)
        time.sleep(typing_speed)


# Ajustar el tiempo de inicio para prepararse
time.sleep(5)

# Ejecutar la función para escribir el código
type_code(code, typing_speed=0.001)  # Ajusta el typing_speed según sea necesario
