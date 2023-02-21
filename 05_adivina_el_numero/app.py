import time
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random
import time


'''
Beln Chacon 


Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón "Mostrar", si el número ingresado es el mismo que el número secreto se dará por terminado
el juego con un mensaje similar a este: 

“Ganaste en X intentos”.
de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
        self.btn_reset = customtkinter.CTkButton(master=self, text="Reset", command=self.btn_reset_on_click)
        self.btn_reset.grid(row=3, pady=20, columnspan=2, sticky="nsew")


        self.inicio_juego()

    def btn_reset_on_click(self):
        self.inicio_juego()

        
    def btn_mostrar_on_click(self):
        if(self.flag_play == True):
            self.numero_intento = self.numero_intento + 1
            numero_jugador_texto = self.txt_numero.get()
            numero_jugador_int = int (numero_jugador_texto)
            if(numero_jugador_int == self.numero_secreto):
                ts_fin_juego = time.time() 
                tiempo_de_juego = ts_fin_juego - self.ts_inicio_juego
                
                
                mensaje= "Ganaste en {0} intentos - En {1} segundos".format(self.numero_intento,tiempo_de_juego)
                self.flag_play= False
            elif(numero_jugador_int > self.numero_secreto ):  
                mensaje= "Se pasó"
            else: 
                mensaje= "Falta"

            alert(title="info", message=mensaje)

    def inicio_juego(self):
        self.numero_secreto = random.randrange(1, 100)
        self.numero_intento = 0
        self.flag_play = True
        print(self.numero_secreto)
        self.ts_inicio_juego = time.time()

if __name__ == "__main__":
    app = App() 
    app.mainloop()