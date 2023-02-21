import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Belen Chacon

Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        estacion = self.combobox_estaciones.get()
        destino = self.combobox_destino.get()
        descuento = 0
        aumento= 0
        match(estacion):
            case "Invierno":
                match(destino):
                    case "Bariloche":
                        aumento = 20
                    case "Cataratas" | "Cordoba":
                        descuento = 10
                    case _:
                        descuento = 20
        match (estacion):
            case "Verano":
                match(destino):
                    case "Bariloche":
                        descuento = 20
                    case "Cataratas" | "Cordoba":
                        descuento = 10
                    case _:
                        descuento = 20 
        match(estacion):
            case "Primavera" | "Otoño":
                match(destino):
                    case "Bariloche" | "Cataratas" | "Mar del plata":
                        aumento= 10
                    case _:
                        aumento =0
                        
        precio_base= 15000
        
        if(descuento !=0): 
            calculo_de_descuento = precio_base * descuento /100
            calculo_total_con_descuento = precio_base  - calculo_de_descuento
            mensaje_descuento = f'El total a abonar es {calculo_total_con_descuento}'
            alert(message=mensaje_descuento)
        else:
            calculo_del_aumento = precio_base * aumento /100
            calculo_total_con_aumento = precio_base + calculo_del_aumento
            mensaje_aumento = f'El total a abonar es {calculo_total_con_aumento}'
            alert(message=mensaje_aumento)
        
#en este todavia me cuesta entender la lógica de por que "si, descuento no es 0"....por lo tanto "aumento es"... tarde 2 dias con este. así funciona pero me volvio loca razonar que si descuesto es tal cosa entonces aumento  (siendo otra variable) es...
    
if __name__ == "__main__":
    app = App()
    app.mainloop()