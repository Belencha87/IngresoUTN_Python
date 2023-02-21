import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador = 0
        numero_txt = prompt(title="",prompt="Ingrese un número: ")
        numero_ingresado = int(numero_txt)
        lista_n_divisores = []
        listas_numeros = [1]

        for numero in listas_numeros:
            if(numero_ingresado % numero == 0):
                numero += 1
                listas_numeros.append(numero)
            
            if(numero_ingresado % numero  >= 0):
                lista_n_divisores.append(numero)
                contador += 1
            else:
                break
            mensaje = f"Los numeros pares encontrados son {contador} y son {lista_n_divisores}"
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()