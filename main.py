#Imports das bibliotecas

from tkinter import *
from tkinter import ttk, messagebox

import numpy as np
import pandas as pd
import openpyxl as xl


#Criando a interface
class Calculadora_lucro():
    def __init__(self):
        self.root =Tk()
        self.root.title("Mercado do Tatu")
        self.root.geometry("1100x650")
        self.root.resizable(False,False)

        
        #Variaveis iniciais
        self.color_green = '#2ca063'
        self.color_yellow = '#e6a04b'
        self.color_branco = '#f8f8f8'



        #Inicializando funções
        self.containers()
        self.itens_container01()
        self.root.mainloop()


    def containers(self):
        self.fr_container01 = Frame(
            self.root,
            width=1050,
            height=30,
            bg='green'
        )
        self.fr_container02 = Frame(
            self.root,
            width=1050,
            height=250
        )
        self.fr_container03 = Frame(
            self.root,
            width=1100,
            height=370,
            bg=self.color_green
        )

        #Posicionar os elementos
        self.fr_container01.propagate(0)
        self.fr_container01.propagate(0)
        self.fr_container01.propagate(0)
        self.fr_container01.pack()
        self.fr_container02.pack()
        self.fr_container03.pack()

    #Itens do container 01
    def itens_container01(self):
        self.lb_title = Label(
            self.fr_container01,
            text='Calculadora de Lucro',
            font='Verdana 20',
            bg= self.fr_container01.cget('bg')
        )

        self.lb_title.pack()





Calculadora_lucro()
 
