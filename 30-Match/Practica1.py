"""Crea un programa que pida al usuario dos números y una operación (suma, resta, multiplicación, división).
Utiliza match-case para realizar la operación correspondiente y muestra el resultado."""

# Pedir al usuario dos números y una operación
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (suma, resta, multiplicación, división): ").strip().lower()

# Realizar la operación correspondiente usando match-case
match operacion:
    case "suma":
        resultado = numero1 + numero2
        print(f"El resultado de la suma es: {resultado}")
    case "resta":
        resultado = numero1 - numero2
        print(f"El resultado de la resta es: {resultado}")
    case "multiplicación" | "multiplicacion":
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicación es: {resultado}")
    case "división" | "division":
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    case _:
        print("Operación no reconocida.")