import tkinter as tk
from timer import timer
from window import window

root = tk.Tk()

title = "Interval Timer"
window(root,title)

label_title = tk.Label(root, text="Interval Timer", background="lightblue")
label_title.pack()


# Inicio
frame_rondas = tk.Frame(root, background="lightblue")
frame_rondas.pack()

entry_ronda = tk.Entry(frame_rondas)
entry_ronda.pack(side="left")

entry_inicial = tk.Entry(root)
entry_inicial.pack()

entry_terminal = tk.Entry(root)
entry_terminal.pack()



def tiempoIniciar():
    inicio = int(entry_inicial.get())
    timer(inicio)

def tiempoTerminar():
    terminar = int(entry_terminal.get())
    timer(terminar)

b_inicial = tk.Button(root, text="Tiempo de inicio", command = tiempoIniciar)
b_inicial.pack()
b_terminar = tk.Button(root, text="Tiempo de terminar", command=tiempoTerminar)
b_terminar.pack()

def rondas():
    ronda = int(entry_ronda.get())
    timer(ronda)





add_button = tk.Button(frame_rondas, text="Agregar Rondas", command=rondas)
add_button.pack(side="left")


root.mainloop()
