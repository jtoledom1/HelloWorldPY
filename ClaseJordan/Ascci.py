def draw_ascii_bar_chart(values):
    # Encuentra el valor máximo para escalar el gráfico
    max_value = max(values)
    
    # Define el ancho máximo de las barras
    max_width = 50
    
    # Imprime el gráfico en ASCII
    for i, value in enumerate(values):
        # Calcula la longitud de la barra en función del valor
        bar_length = int((value / max_value) * max_width)
        # Crea la barra y la imprime
        bar = '#' * bar_length
        print(f"Item {i+1}: {bar} ({value})")

# Ejemplo de datos
values = [10, 20, 30, 40, 50]
draw_ascii_bar_chart(values)

print("""
 /\_/\  
( o.o ) 
 > ^ <      
      """)
# Define color codes
RED = '\033[0;31m'
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color

# Print ASCII art with colors
print(f"""{RED}
 /\_/\  
{NC}{GREEN}
( o.o ) 
{NC}{BLUE}
 > ^ <      
{NC}""")

 