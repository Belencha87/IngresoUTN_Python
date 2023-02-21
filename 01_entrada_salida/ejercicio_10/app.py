import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Belén   
apellido: Chacón
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txt_importe y txt_descuento), 
transformarlos en números y mostrar el importe actualizado con el descuento utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Importe")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Descuento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_descuento = customtkinter.CTkEntry(master=self)
        self.txt_descuento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
#arreglado

    def btn_mostrar_on_click(self):
        sueldo_texto = self.txt_sueldo.get ()
        descuento_texto = self.txt_descuento.get ()
        sueldo_numero = float (sueldo_texto)
        descuento_numero= float (descuento_texto)
        descuento = (sueldo_numero * descuento_numero) / 100
        sueldo_con_descuento=  sueldo_numero - descuento
        
        
        
        mensaje = "El nuevo sueldo es {0}".format(sueldo_con_descuento)
        alert (title="SUELDO", message=mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()