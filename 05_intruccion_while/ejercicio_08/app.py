import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Belen Chacon
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        bandera_continuar= True
        numeros_negativos = None
        suma_num_positivos = 0
        
        while(bandera_continuar == True):
            num_txt = prompt(title="", prompt=" Ingreso un número:")
            if( num_txt == None or num_txt == 0):
                bandera_continuar = False
            else:
                num_int = int (num_txt)
                if(num_int >0):
                    suma_num_positivos = num_int + suma_num_positivos
                else:
                    if(numeros_negativos == None):
                        numeros_negativos = num_int
                    else:
                        numeros_negativos = numeros_negativos * num_int
                        
                        
                        
                
        self.txt_suma_acumulada.delete(0,100) 
        self.txt_suma_acumulada.insert(0,suma_num_positivos)
        self.txt_producto.delete(0,100)
        self.txt_producto.insert(0,numeros_negativos)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
