
# Python program for creating an application to switch pages using trinket.

import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class Principal(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Inicio, Pagina01, Pagina02):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(Inicio)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Inicio(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Página de Inicio", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visitar Página 1",
                           command=lambda: controller.show_frame(Pagina01))
        button.pack()

        button2 = tk.Button(self, text="Visitar Página 2",
                            command=lambda: controller.show_frame(Pagina02))
        button2.pack()


class Pagina01(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Página 1!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Regresar a Inicio",
                            command=lambda: controller.show_frame(Inicio))
        button1.pack()

        button2 = tk.Button(self, text="Ir a página 2",
                            command=lambda: controller.show_frame(Pagina02))
        button2.pack()


class Pagina02(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Página 2", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Regresar a Inicio",
                            command=lambda: controller.show_frame(Inicio))
        button1.pack()

        button2 = tk.Button(self, text="It a página 1",
                            command=lambda: controller.show_frame(Pagina01))
        button2.pack()


app = Principal()
app.mainloop()

