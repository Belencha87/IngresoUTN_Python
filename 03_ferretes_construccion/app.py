import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Belen Chacon 

Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (V)Poste Quebracho Fino de 2.2 mts
    (F)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)
        
        self.btn_calcular = customtkinter.CTkButton(master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        

    def btn_calcular_on_click(self):
        #A Informar los metros cuadrados del terreno y los metros lineales del perimetro
        largo_del_terreno=self.txt_largo.get()
        largo_en_num=float(largo_del_terreno)
        ancho_del_terreno=self.txt_ancho.get()
        ancho_en_num=float(ancho_del_terreno)
        metros_cuadrados =int (largo_en_num * ancho_en_num)
        metros_lineales=int (largo_en_num * 2) + (ancho_en_num * 2)


        #B Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
        quebracho_grueso_largo= int(((largo_en_num-1)//250))*2
        quebracho_grueso_ancho= int(((ancho_en_num-1)//250))*2
        quebrachogrueso_suma= quebracho_grueso_largo*2 +quebracho_grueso_ancho*2
        quebracho_grueso_total_txt= str(quebrachogrueso_suma)
        
        #C   Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
        fino_largo_total= largo_en_num - quebracho_grueso_largo
        quebracho_fino_largo= int((fino_largo_total-1)//12)
        fino_ancho_total= ancho_en_num - quebracho_grueso_ancho
        quebracho_fino_ancho= int(fino_ancho_total//12)
        total_quebracho_fino= quebracho_fino_largo*2 + quebracho_fino_ancho*2
        quebracho_fino_total_txt=str(total_quebracho_fino)
    
        #D  Informar la cantidad de varillas (van cada 2 mts lineales).
        largo_varilla_total= fino_largo_total - quebracho_fino_largo
        varilla_largo= int((largo_varilla_total-1)//2)
        ancho_varilla_total= fino_ancho_total - quebracho_fino_ancho
        varilla_ancho= int((ancho_varilla_total-1)//2)
        varilla_suma= varilla_largo*2 + varilla_ancho*2
        varilla_txt= str(varilla_suma)
        
        #E Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.
        alambre= metros_lineales *7
        alambre_txt= str(alambre)
        
        mensaje= f"Los metros cuadrados del terreno son {metros_cuadrados}, los metros lineales del perímetro son {metros_lineales}, la cantidad de postes de quebrachos gruesos es {quebracho_grueso_total_txt}, la cantidad de postes de quebrachos fnos es {quebracho_fino_total_txt}, la cantida de varillas es {varilla_txt}, la cantidad de alambre alta resistencia 17/15 es {alambre_txt}"
        alert(title="Materiales necesarios", message=mensaje)
#en este asumo que algo mal está, pero lo hice hace bastante. y no sé ya que es. 
        
if __name__ == "__main__":
    app = App()
    app.mainloop()