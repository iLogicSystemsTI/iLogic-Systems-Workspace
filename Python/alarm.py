import time
from datetime import datetime, timedelta


def configurar_alarma():
    print("Configura la alarma:")
    hora = int(input("Hora (0-23): "))
    minuto = int(input("Minuto (0-59): "))

    return hora, minuto


def calcular_tiempo_restante(hora_alarma, minuto_alarma):
    ahora = datetime.now()
    alarma = ahora.replace(hour=hora_alarma, minute=minuto_alarma, second=0)
    if ahora > alarma:
        alarma += timedelta(days=1)
    tiempo_restante = alarma - ahora
    return tiempo_restante


def mostrar_tiempo_restante(tiempo_restante):
    minutos, segundos = divmod(tiempo_restante.seconds, 60)
    horas, minutos = divmod(minutos, 60)
    print(
        "Tiempo restante para la alarma: %d horas, %d minutos y %d segundos."
        % (horas, minutos, segundos)
    )


def activar_alarma():
    hora_alarma, minuto_alarma = configurar_alarma()
    while True:
        tiempo_restante = calcular_tiempo_restante(hora_alarma, minuto_alarma)
        mostrar_tiempo_restante(tiempo_restante)
        if tiempo_restante.total_seconds() < 5:
            print("Despierta! Es hora de levantarse.")
            break
        time.sleep(10)


activar_alarma()
