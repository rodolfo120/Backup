from tkinter import *
from tkinter import filedialog
import funciones

class backup:
    def __init__(self,Ventana):
        self.Ventana = Ventana
        self.Ventana.geometry("1280x720+300+100")
        self.Ventana.resizable(False, False)

        self.Origen = ""
        self.Destino = ""

        self.frm_inicio = Frame(self.Ventana,background="#ffffff",width=1280,height=720)
        self.frm_inicio.place(x=0, y=0)
        self.lbl_lugar_origen = Label(self.frm_inicio,font=("Console", 20), background="#ffffff")
        self.lbl_lugar_origen.place(x=420,y=50)
        self.btn_lugar_origen = Button(self.frm_inicio,text="Lugar de origen", command= self.Directorio_Origen)
        self.btn_lugar_origen.place(x=600,y=150)
        self.lbl_lugar_destino = Label(self.frm_inicio,font=("Console", 20), background="#ffffff")
        self.lbl_lugar_destino.place(x=420,y=250)
        self.btn_lugar_destino = Button(self.frm_inicio,text="Lugar de destino", command= self.Directorio_Destino)
        self.btn_lugar_destino.place(x=600,y=350)
        self.btn_mover = Button(self.frm_inicio,text="Mover",command= lambda: funciones.mover(self.Origen,self.Destino))
        self.btn_mover.place(x=520,y=500)
        self.btn_copy = Button(self.frm_inicio,text="Copiar", command= lambda: funciones.copy(self.Origen,self.Destino))
        self.btn_copy.place(x=740,y=500)

    def Directorio_Origen(self):
        self.Origen = filedialog.askdirectory()
        self.lbl_lugar_origen.config(text=self.Origen)

    def Directorio_Destino(self):
        self.Destino = filedialog.askdirectory()
        self.lbl_lugar_destino.config(text=self.Destino)

if __name__=="__main__":
    ventana = Tk()
    backup(ventana)
    ventana.mainloop()