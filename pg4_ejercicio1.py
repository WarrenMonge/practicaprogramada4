def ingresar_notas():
    notas = []
    for i in range(3):
        curso = []
        print(f"Ingrese las notas del aula {i+1}:")
        for j in range(5):
            nota = float(input(f"Ingrese la nota del estudiante {j+1}: "))
            curso.append(nota)
        notas.append(curso)
    return notas

def promedio_por_grupo(notas):
    promedios_por_grupo = []
    for curso in notas:
        promedio = sum(curso) / len(curso)
        promedios_por_grupo.append(promedio)
    return promedios_por_grupo

def promedio_total(notas):
    total_notas = [nota for curso in notas for nota in curso]
    promedio = sum(total_notas) / len(total_notas)
    return promedio


def aprobados(notas):
    porcentaje_aprobados = []
    for curso in notas:
        aprobados = sum(1 for nota in curso if nota >= 70)
        porcentaje = (aprobados / len(curso)) * 100
        porcentaje_aprobados.append(porcentaje)
    return porcentaje_aprobados

def nota_mayor_menor(notas):
    resultados = []
    for curso in notas:
        mayor = max(curso)
        menor = min(curso)
        resultados.append((mayor, menor))
    return resultados

def mostrar_resultados(notas):
    promedio_total = promedio_total(notas)
    print("El promedio total de notas es:", promedio_total)

    promedios_por_grupo = promedio_por_grupo(notas)
    for i, promedio in enumerate(promedios_por_grupo):
        print(f"El promedio del grupo {i+1} es:", promedio)

    porcentaje_aprobados = aprobados(notas)
    for i, porcentaje in enumerate(porcentaje_aprobados):
        print(f"El porcentaje de aprobados en el grupo {i+1} es:", porcentaje, "%")

    resultados = nota_mayor_menor(notas)
    for i, (mayor, menor) in enumerate(resultados):
        print(f"En el grupo {i+1}, la nota mayor es:", mayor, "y la nota menor es:", menor)

notas = ingresar_notas()
mostrar_resultados(notas)

