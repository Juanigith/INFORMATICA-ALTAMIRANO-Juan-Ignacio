3
lado_a = float(input("Lado A del triángulo: "))
lado_b = float(input("Lado B del triángulo: "))
lado_c = float(input("Lado C del triángulo: "))

equilatero = lado_a == lado_b and lado_b == lado_c

isoceles = lado_a == lado_b or lado_b == lado_c or lado_c == lado_a

triangulo_valido = (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_b) and (lado_c < lado_a + lado_b)

print(f"triangulo válido: {triangulo_valido}, equilatero: {equilatero}, isóceles: {isoceles}")