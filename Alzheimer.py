# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:29:01 2024

@author: chino
"""

import tkinter as tk

class Examen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Test de Alzheimer")
        self.geometry("500x400")

        self.preguntas = [
            "¿Cuántos años tienes?",
            "¿En qué mes estamos?",
            "¿Cuál año es este?",
            "¿En qué estado estamos?",
            "¿Alguien de tu familia cercana fue diagnosticado con Alzheimer?",
            "¿Tuviste alguna lesión grave en la cabeza?",
            "¿Sufres de problemas cardiacos?",
            "¿Tienes diabetes?",
            "¿Tu dieta es balanceada?",
            "¿Con qué frecuencia ejercitas?",
            "¿Se te dificulta recordar fechas o eventos?",
            "¿Tiendes a perderte al estar en la calle?",
            "¿Cuál de estos no es un medio de transporte?",
            "¿Cuál de estos no es un animal doméstico?",
            "¿Cuál de estos no es un ejemplo de postre?",
            "¿Cuál de las siguientes preguntas fue repetida en el cuestionario?",
            "¿Cuál de las siguientes preguntas fue repetida en el cuestionario?",
            "¿Cuál de las siguientes preguntas fue repetida en el cuestionario?",
            "¿Cuál de las siguientes preguntas fue repetida en el cuestionario?",
            "¿Cuál de las siguientes preguntas fue repetida en el cuestionario?"
        ]
        self.respuestas = [
            ["60 años o más", "18 a 35 años", "Menor de 18 años", "36 a 59 años"],
            ["octubre", "marzo", "enero", "julio"],
            ["2023", "2024", "2022", "2021"],
            ["Aguascalientes", "Guerrero", "Jalisco", "Sinaloa"],
            ["Si", "No", "No lo se", "Es posible"],
            ["Si", "No", "No lo se", "Nunca me he lastimado"],
            ["Si", "No", "No lo se", "Nunca he tenido problemas"],
            ["Si", "No", "No lo se", "Nunca me he sentido mal"],
            ["No", "Si", "Intento comer bien", "No tengo dieta"],
            ["Casi siempre", "Con frecuencia", "Casi Nunca", "Nunca"],
            ["Si", "No", "Solo recuerdo fechas importantes", "Suelo recordar bien las fechas"],
            ["A veces", "No", "Siempre puedo recordar donde estoy", "Si"],
            ["Carro", "Autobús", "Barco", "Árbol"],
            ["Ballena", "Perro", "Gato", "Loro"],
            ["Pastel", "Bicicleta", "Pan dulce", "Helado"],
            ["¿Tienes mascotas?", "¿Tuviste alguna lesión grave en la cabeza?", "Ninguna fue repetida", "¿Tienes hijos?"],
            ["Ninguna fue repetida", "¿Cuantos hermanos tienes?", "¿Trabajas?", "¿Duermes bien?"],
            ["¿Cuantos años tienes?", "¿Eres casado?", "¿Tienes problemas de salud?", "Ninguna pregunta fue repetida"],
            ["Ninguna fue repetida", "¿En que mes estamos?", "¿Tienes televisión?", "¿Tomas vino?"],
            ["¿Con qué frecuencia ejercitas?", "¿Tiendes a perderte al estar en la calle?", "¿Con qué frecuencia ejercitas?", "Todas están repetidas"]
        ]
        self.respuestas_seleccionadas = [""] * len(self.preguntas)
        self.posicion = 0

        self.create_widgets()

    def create_widgets(self):
        self.label_pregunta = tk.Label(self, text="Test de Alzheimer", font=("Segoe UI", 24))
        self.label_pregunta.pack()

        self.label_pregunta_actual = tk.Label(self, text=self.preguntas[self.posicion], font=("Segoe UI", 18))
        self.label_pregunta_actual.pack()

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self, text=self.respuestas[self.posicion][i], variable=self.radio_var, value=i)
            rb.pack()
            self.radio_buttons.append(rb)

        self.button_siguiente = tk.Button(self, text="Siguiente pregunta >>", command=self.siguiente_pregunta)
        self.button_siguiente.pack()

        self.button_anterior = tk.Button(self, text="<< Regresar", command=self.pregunta_anterior)
        self.button_anterior.pack()
        self.button_anterior.config(state=tk.DISABLED)

        self.button_terminar = tk.Button(self, text="Terminar prueba", command=self.terminar_prueba)
        self.button_terminar.pack()
        self.button_terminar.config(state=tk.DISABLED)

    def siguiente_pregunta(self):
        if self.posicion == 18:
            self.button_siguiente.config(state=tk.DISABLED)
            self.button_terminar.config(state=tk.NORMAL)
        if self.posicion < 19:
            self.button_anterior.config(state=tk.NORMAL)
            self.respuestas_seleccionadas[self.posicion] = self.respuestas[self.posicion][int(self.radio_var.get())]
            self.posicion += 1
            self.label_pregunta_actual.config(text=self.preguntas[self.posicion])
            for i, rb in enumerate(self.radio_buttons):
                rb.config(text=self.respuestas[self.posicion][i])

    def pregunta_anterior(self):
        if self.posicion == 1:
            self.button_anterior.config(state=tk.DISABLED)
        elif self.posicion < 20:
            self.button_terminar.config(state=tk.DISABLED)

        if self.posicion > -1:
            self.posicion -= 1
            self.button_siguiente.config(state=tk.NORMAL)
            self.label_pregunta_actual.config(text=self.preguntas[self.posicion])
            for i, rb in enumerate(self.radio_buttons):
                rb.config(text=self.respuestas[self.posicion][i])

    def terminar_prueba(self):
        calificacion = sum(1 for i in range(20) if self.respuestas_seleccionadas[i] != self.respuestas[i][0])
        print(f"Puntos: {calificacion}")
        if calificacion > 15:
            print("Resultado: Eres propenso a tener Alzheimer")
        else:
            print("Resultado: Estás bien")
        self.destroy()

if __name__ == "__main__":
    app = Examen()
    app.mainloop()
