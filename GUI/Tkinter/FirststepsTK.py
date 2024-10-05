#Ejercicio obtenido de https://realpython.com/python-gui-tkinter/ 
import tkinter as tk
ventana = tk.Tk()
etiqueta = tk.Label(text="Python rocks!")
etiqueta.pack() #Instrucción .pack ayuda a añadir widget a la pantalla
ventana.mainloop()