def pasajeros():
    pasajeros_semana = []
    for dia in range(5):
        pasajeros_dia = []
        print(f"Ingrese la cantidad de pasajeros para el día de la semana{dia + 1}:")
        for servicio in range(4):
            while True:
                cantidad = int(input(f"Ingrese la cantidad de pasajeros para el servicio {servicio + 1}: "))
                if cantidad <= 60:
                    break
                else:
                    print("La cantidad maxima de pasajeros es 60!!!")
            pasajeros_dia.append(cantidad)
        pasajeros_semana.append(pasajeros_dia)
    return pasajeros_semana

def promedio_por_dia(pasajeros_semana):
    promedios = []
    for dia in pasajeros_semana:
        promedio_dia = sum(dia) / len(dia)
        promedios.append(promedio_dia)
    return promedios

def promedio_total(pasajeros_semana):
    total_pasajeros = sum(sum(dia) for dia in pasajeros_semana)
    promedio_general = total_pasajeros / (5 * 4)
    return promedio_general

def mejor_servicio(pasajeros_semana):
    max_pasajeros = max(sum(servicio) for servicio in zip(*pasajeros_semana))
    for dia, servicios in enumerate(pasajeros_semana, start=1):
        for servicio, pasajeros in enumerate(servicios, start=1):
            if pasajeros == max_pasajeros:
                return f"El mejor servicio es el {servicio} en el día {dia} con {pasajeros} pasajeros."

def menos_pasajeros(pasajeros_semana):
    min_pasajeros = min(min(dia) for dia in pasajeros_semana)
    for dia, servicios in enumerate(pasajeros_semana, start=1):
        for servicio, pasajeros in enumerate(servicios, start=1):
            if pasajeros == min_pasajeros:
                return f"Menor cantidad de pasajeros es en el servicio {servicio} en el día {dia} con {pasajeros} pasajeros."


pasajeros_semana = pasajeros()

promedios_dia = promedio_por_dia(pasajeros_semana)
for i, promedio in enumerate(promedios_dia, start=1):
    print(f"El promedio de pasajeros para el día de la semana {i} es: {promedio}")

promedio_general = promedio_total(pasajeros_semana)
print(f"El promedio de todos los días y servicios es: {promedio_general}")

best_servicio = mejor_servicio(pasajeros_semana)
print(best_servicio)

menos_pasajeros_ = menos_pasajeros(pasajeros_semana)
print(menos_pasajeros_)
