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

        self.root.mainloop()

Calculadora_lucro()
 
