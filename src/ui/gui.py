import tkinter as tk
from tkinter import Entry, Label, Button, messagebox, colorchooser
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

class GraphController:
    def __init__(self, temperatura_data_callback):
        self.root = tk.Tk()
        self.root.title("Controles de la Gráfica")

        self.min_escala_y = 0
        self.max_escala_y = 100
        self.nuevo_color = 'blue'
        self.pausado = False
        self.temperatura_data_callback = temperatura_data_callback

        # Configuración inicial de la gráfica
        self.figure = Figure(figsize=(6, 4))
        self.ax = self.figure.add_subplot(111)
        self.ax.set_ylim(self.min_escala_y, self.max_escala_y)
        self.ax.set_xlabel("Contador")
        self.ax.set_ylabel("Temperatura (°C)")
        self.linea, = self.ax.plot([], [], 'bo-', lw=2)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=3, pady=10)

        self.create_controls()

        self.ani = FuncAnimation(self.figure, self.actualizar, init_func=self.init_anim, blit=True, interval=1000, cache_frame_data=False)


    def create_controls(self):
        self.boton_pausa = Button(self.root, text="Pausar", command=self.pausar_reanudar)
        self.boton_pausa.grid(row=1, column=0, padx=5, pady=5)

        self.boton_color = Button(self.root, text="Cambiar Color", command=self.cambiar_color)
        self.boton_color.grid(row=1, column=1, padx=5, pady=5)

        Label(self.root, text="Escala Mínima Y:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_min_escala = Entry(self.root)
        self.entry_min_escala.grid(row=2, column=1, padx=5, pady=5)
        self.entry_min_escala.insert(0, str(self.min_escala_y))

        Label(self.root, text="Escala Máxima Y:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_max_escala = Entry(self.root)
        self.entry_max_escala.grid(row=3, column=1, padx=5, pady=5)
        self.entry_max_escala.insert(0, str(self.max_escala_y))

        self.boton_escala = Button(self.root, text="Aplicar Escala", command=self.cambiar_escala)
        self.boton_escala.grid(row=4, column=0, columnspan=2, pady=10)

    def init_anim(self):
        self.linea.set_data([], [])
        return self.linea,

    def actualizar(self, frame):
        if not self.pausado:
            contador_data, temperatura_data = self.temperatura_data_callback()
            if contador_data and temperatura_data:
                self.linea.set_data(contador_data, temperatura_data)
                self.ax.set_xlim(0, max(contador_data))
                self.ax.set_ylim(self.min_escala_y, self.max_escala_y)

        return self.linea,

    def pausar_reanudar(self):
        self.pausado = not self.pausado
        self.boton_pausa.config(text="Reanudar" if self.pausado else "Pausar")

    def cambiar_color(self):
        color = colorchooser.askcolor(title="Seleccionar color")[1]
        if color:
            self.nuevo_color = color
            self.linea.set_color(self.nuevo_color)

    def cambiar_escala(self):
        try:
            nuevo_min = float(self.entry_min_escala.get())
            nuevo_max = float(self.entry_max_escala.get())
            if nuevo_min < nuevo_max:
                self.min_escala_y = nuevo_min
                self.max_escala_y = nuevo_max
                self.ax.set_ylim(self.min_escala_y, self.max_escala_y)
                self.canvas.draw()
            else:
                messagebox.showerror("Error", "El valor mínimo debe ser menor que el máximo.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def run(self):
        self.root.mainloop()
