import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Belén
Apellido: Chacón
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
        
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        importe_uno_txt = self.txt_importe_1.get()
        importe_uno_float  = float(importe_uno_txt)
        importe_dos_txt = self.txt_importe_2.get()
        importe_dos_float  = float(importe_dos_txt)
        importe_tres_txt = self.txt_importe_3.get()
        importe_tres_float  = float(importe_tres_txt)
        suma_de_importe= importe_uno_float + importe_dos_float + importe_tres_float 
        mensaje = "La resultado de la suma es {0}".format(suma_de_importe)
        alert(title = "suma", message = mensaje) 

    def btn_promedio_on_click(self):
        importe_uno_txt = self.txt_importe_1.get()
        importe_uno_float = float(importe_uno_txt)
        importe_dos_txt = self.txt_importe_2.get()
        importe_dos_float = float(importe_dos_txt)
        importe_tres_txt = self.txt_importe_3.get()
        importe_tres_float = float(importe_tres_txt)
        suma_de_importe= importe_uno_float + importe_dos_float + importe_tres_float
        promedio = suma_de_importe / 3
        mensaje = "El promedio es {0}".format(promedio)
        alert(title = "promedio", message=mensaje)
        


    def btn_total_iva_on_click(self):
        importe_uno_txt = self.txt_importe_1.get()
        importe_uno_float = float(importe_uno_txt)
        importe_dos_txt = self.txt_importe_2.get()
        importe_dos_float = float(importe_dos_txt)
        importe_tres_txt = self.txt_importe_3.get()
        importe_tres_float = float(importe_tres_txt)
        suma_de_importe= importe_uno_float + importe_dos_float + importe_tres_float
        importe_con_iva = suma_de_importe * 1.21 
        mensaje = "El precio final más iva es {0}".format(importe_con_iva)
        alert(title = "Más iva", message=mensaje)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()