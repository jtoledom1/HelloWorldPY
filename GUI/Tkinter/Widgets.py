import tkinter as tk
import tkinter.ttk as ttk
ventana = tk.Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")
l1.pack()
l2.pack()
ventana.mainloop()
