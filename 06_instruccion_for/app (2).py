import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt) o ingrese cero. 

Acumular los valores positivos y multiplicar entre si aquellos que son negativos (* informar por terminal) 

Luego determinar el máximo, el mínimo y el promedio de todos los numeros ingresados.
e informarlos en los cuadros de textos txt_maximo, txt_minimo y promedio respectivamente

-Resolver sin usar lista
-Resolver con lista
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_maximo.grid(row=2, padx=20, pady=20)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso sin Lista", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso con Lista", command=self.btn_comenzar_ingreso_lista_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_lista_on_click(self):
        acumulador_general =  0
        acumulador_positivos = 0
        acumulador_multiplos_negativos = None
        contador_numeros_ingresados = 0
        lista_numeros_ingresados = [1,2,-1,-2,1]
        maximo = None
        minimo = None
        promedio = None
        while (True):
            numero_texto =  prompt(title="Numero",prompt="Ingrese un número")
            if(numero_texto != None and numero_texto != "0"):
                numero_int = int(numero_texto)
                lista_numeros_ingresados.append(numero_int)
            else:
                break

        # -----------------------------------------------------------------------

        contador_numeros_ingresados = len(lista_numeros_ingresados)        
        for numero in lista_numeros_ingresados:
            acumulador_general += numero
        
            if(maximo == None or numero > maximo):
                maximo = numero
        
            if(minimo == None or numero < minimo):
                minimo = numero

            if(numero > 0):
                acumulador_positivos += numero
            else:
                if(acumulador_multiplos_negativos == None):
                    acumulador_multiplos_negativos = numero
                else:
                    acumulador_multiplos_negativos *= numero

        promedio = acumulador_general / contador_numeros_ingresados

        mensaje = "Acumulador General: {0}\nAcumuladr Positivos: {1}\nAcumulador Multiplos Negativos:{2}\nContador Ingresados:{3}\n Max:{4}\n Min:{5}\n Promedio:{6}"
        mensaje = mensaje.format(acumulador_general,acumulador_positivos,acumulador_multiplos_negativos,contador_numeros_ingresados,maximo,minimo,promedio)
        print(mensaje)





















    def btn_comenzar_ingreso_on_click(self):
        flag_continuar = True
        acumulador_positivos = 0
        acumulador_multiplos_negativos = None
        acumulador_general = 0
        contador_numeros_ingresados = 0
        maximo = None
        minimo = None
        while (flag_continuar):
            numero_texto = prompt(title="Numero",prompt="Ingrese un número")
            if(numero_texto == None or numero_texto=="0"):
                flag_continuar = False
            else:
                numero_int = int(numero_texto)
                acumulador_general = acumulador_general + numero_int
                contador_numeros_ingresados = contador_numeros_ingresados + 1 #contador_numeros_ingresados +=  1
                if(maximo == None or numero_int > maximo):
                    maximo = numero_int

                if(minimo == None  or numero_int < minimo):
                    minimo = numero_int

                if(numero_int > 0):
                    acumulador_positivos = acumulador_positivos + numero_int
                else:
                    if(acumulador_multiplos_negativos == None):
                        acumulador_multiplos_negativos = numero_int
                    else:
                        acumulador_multiplos_negativos = acumulador_multiplos_negativos * numero_int

        promedio_numeros_ingresados = acumulador_general / contador_numeros_ingresados       
        mensaje = "Acumulador positivos: {0} \nAcumulador Multiplo de Negativos: {1}\nAcumulador General:{2}\nContador:{3}\nPromedio:{4}".format(acumulador_positivos,acumulador_multiplos_negativos,acumulador_general,contador_numeros_ingresados,promedio_numeros_ingresados)
        print(mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()
