import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Belen CHacon
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt(title="", prompt="Ingrese un número: ")
        int_numero = int (numero)
        
        for num in range (2,int_numero):
            if(int_numero % num !=0):
                mensaje = "Es primo"
            else:
                mensaje = "No es primo"
                break
        alert(title="",message=mensaje)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()