from os import system 
import sympy as sp
CYAN = '\033[0;36m'
print(" ")#Este print junto con el system clear inicializa la consola en 0.
system("cls")
print(f"""
{CYAN} 
\t Bienvenido, a continuación 
Introduce una función en x (ej. x**2 - 4*x + 4):
""")
funcion_input = input("f(x)=")

# Definimos x como la variable
x = sp.symbols('x')

# El contenido (cadena) de la variable function_input que realizamos al inicio 
# la vamos a convertir en una función
f = sp.sympify(funcion_input)

# Calculamos la derivada de la función
f_derivada = sp.diff(f, x)

# Encontramos los puntos críticos resolviendo la ecuación f'(x) = 0
puntos_criticos = sp.solve(f_derivada, x)

print("Puntos críticos:", puntos_criticos)


#A partir de aquí usé código de chatgpt

# Evaluamos la función en cada punto crítico
resultados = {p: f.subs(x, p) for p in puntos_criticos}

# Mostramos los resultados de la evaluación
for punto, valor in resultados.items():
    print(f"f({punto}) = {valor}")
