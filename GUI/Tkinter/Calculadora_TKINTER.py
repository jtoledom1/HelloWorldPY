import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = operacion_var.get()
        
        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        elif operacion == 'exponenciacion':
            resultado = num1 ** num2
        else:
            resultado = "Operación no válida."

        label_resultado.config(text=f"Resultado: {resultado}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Error: División por cero.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear entradas
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

# Crear opción de operación
operacion_var = tk.StringVar(value='suma')
label_operacion = tk.Label(ventana, text="Seleccione la operación:")
label_operacion.pack()

opciones = ['suma', 'resta', 'multiplicacion', 'division', 'exponenciacion']
for op in opciones:
    rb = tk.Radiobutton(ventana, text=op.capitalize(), variable=operacion_var, value=op)
    rb.pack(anchor='w')

# Botón de calcular
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.pack()

# Label para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Ejecutar la aplicación
ventana.mainloop()
