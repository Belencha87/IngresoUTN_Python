import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        ingreso_bandera =  True
        num_txt = 0
        num_int = int (num_txt)
        cantidad_num_positivos = num_int > 0
        cantidad_num_negativos = num_int < 0 
        suma_num_positivos = 0
        suma_num_negativos = 0
        cantidad_num_positivos = 0
        cantidad_num_negativos = 0
        cantidad_ceros = 0
        
        while (ingreso_bandera == True):
            num_txt = prompt(title="", prompt="Ingrese número: ")
            if (num_txt == None):
                ingreso_bandera = False
            else: 
                num_int = int (num_txt)
            if (num_txt  >0 ):
                suma_num_positivos = num_int + suma_num_positivos
            else:
                (num_txt  <0 )
                suma_num_negativos = num_int + suma_num_negativos
                    
        cantidad_ceros= 0 + 1 
        dif_cant_posit_negat= cantidad_num_positivos - cantidad_num_negativos
                    
        mensaje= "La suma acumulada de los negativos es de; {0} \n La suma acumulada de los positivos es de: {1} \n La cantidad de los números positivos ingresados es de: {2} La cantidad de números negativoss ingresados es de: {3} \n La cantidad de ceros es de: {4} \n La difernecia entre la  cantidad de los números positivos ingresaods y los negativos es de: {5} ".format(suma_num_negativos, suma_num_positivos, cantidad_num_positivos, cantidad_num_negativos, cantidad_ceros, dif_cant_posit_negat )
        alert(title="", message= mensaje)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
