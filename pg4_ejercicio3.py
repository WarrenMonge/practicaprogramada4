def calcular_total_salarios():
    salarios_jugadores = []
    for i in range(25):
        salario = float(input(f"Ingrese el salario mensual del jugador {i+1}: "))
        salarios_jugadores.append(salario)
    total_salarios = sum(salarios_jugadores)
    return total_salarios

def calcular_suma(total_salarios):
    billetes_monedas = [50000, 20000, 10000, 5000, 2000, 1000, 500, 100, 50, 25,10, 5]
    cantidad_billetes_monedas = {}
    for can_billetes_monedas in billetes_monedas:
        cantidad = total_salarios // can_billetes_monedas
        total_salarios %= can_billetes_monedas
        cantidad_billetes_monedas[can_billetes_monedas] = int(cantidad)
    return cantidad_billetes_monedas

def mostrar_resultado(cantidad_billetes_monedas):
    print("Para realizar el pago exacto en efectivo a cada jugador, se necesitaran las siguientes cantidades de billetes y monedas:")
    for can_billetes_monedas, cantidad in cantidad_billetes_monedas.items():
        if cantidad > 0:
            print(f"{cantidad} billetes ó monedas de {can_billetes_monedas}")

total_salarios = calcular_total_salarios()
print("El total a pagar a los jugadores es:", total_salarios)
cantidad_billetes_monedas = calcular_suma(total_salarios)
mostrar_resultado(cantidad_billetes_monedas)

