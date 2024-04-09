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
        self.itens_container02()
        self.root.mainloop()


    def containers(self):
        self.fr_container01 = Frame(
            self.root,
            width=1050,
            height=30
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


    #Itens do container 02
    def itens_container02(self):
        
        #Subcontainers
        self.fr_subcontainer01 = Frame(
            self.fr_container02,
            bg='white',
            highlightthickness=1,
            highlightcolor='gray'
        )
        self.fr_subcontainer02 = Frame(
            self.fr_container02,
            bg='white',
            highlightthickness=1,
            highlightcolor='gray'
        )
        self.fr_subcontainer03 = Frame(
            self.fr_container02,
            bg='white',
            highlightthickness=1,
            highlightcolor='gray'
        )

        self.fr_container_btn = Frame(
            self.fr_subcontainer01,
            bg=self.fr_subcontainer01.cget('bg')
        )

        #Itens do subcontainer 01
        self.lb_title_section01 = Label(
            self.fr_subcontainer01,
            text='Cadastro de Produto',
            font='Verdana 15',
            bg=self.fr_subcontainer01.cget('bg')
        )

        #Nome do produto
        self.lb_nome_produto = Label(
            self.fr_subcontainer01,
            text='Nome do Produto *',
            font='Verdana',
            bg=self.fr_subcontainer01.cget('bg')
        )
        self.en_nome_produto= Entry(
            self.fr_subcontainer01,
            font='Verdana',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor= self.color_green,
            bg=self.fr_container01.cget('bg')
        )


        #Quantidade do produto
        self.lb_qtd_produto = Label(
            self.fr_subcontainer01,
            text='Quantidade do Produto *',
            font='Verdana',
            bg=self.fr_subcontainer01.cget('bg')
        )
        self.en_qtd_produto= Entry(
            self.fr_subcontainer01,
            font='Verdana',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor= self.color_green,
            bg=self.fr_container01.cget('bg')
        )

        #Preço de compra
        self.lb_preco_compra = Label(
            self.fr_subcontainer01,
            text='Preço de Compra *',
            font='Verdana',
            bg=self.fr_subcontainer01.cget('bg')
        )
        self.en_preco_compra= Entry(
            self.fr_subcontainer01,
            font='Verdana',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor= self.color_green,
            bg=self.fr_container01.cget('bg')
        )


        #Preço de venda
        self.lb_preco_venda = Label(
            self.fr_subcontainer01,
            text='Preço de Venda *',
            font='Verdana',
            bg=self.fr_subcontainer01.cget('bg')
        )
        self.en_preco_venda= Entry(
            self.fr_subcontainer01,
            font='Verdana',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor= self.color_green,
            bg=self.fr_container01.cget('bg')
        )


        # Custo do frete
        self.lb_custo_frete = Label(
            self.fr_subcontainer01,
            text='Custo do Frete *',
            font='Verdana',
            bg=self.fr_subcontainer01.cget('bg')
        )
        self.en_custo_frete= Entry(
            self.fr_subcontainer01,
            font='Verdana',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor= self.color_green,
            bg=self.fr_container01.cget('bg')
        )


        # Custo adicional
        self.lb_custo_adicional = Label(
            self.fr_subcontainer01,
            text='Custo Adicional *',
            font='Verdana',
            bg=self.fr_subcontainer01.cget('bg')
        )
        self.en_custo_adicional= Entry(
            self.fr_subcontainer01,
            font='Verdana',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor= self.color_green,
            bg=self.fr_container01.cget('bg')
        )

        
        # Botões
        self.btn_calcular = Button(
            self.fr_container_btn,
            text='Calcular',
            fg='white',
            bg='#0097b2',
            command=None
        )
        self.btn_salvar = Button(
            self.fr_container_btn,
            text='Salvar',
            fg='white',
            bg= self.color_green,
            command=None
        )
        self.btn_deletar = Button(
            self.fr_container_btn,
            text='Deletar',
            fg='white',
            bg='#ff3131',
            command=None
        )

        # Itens subcontainer 02
        self.lb_title_section02 = Label(
            self.fr_subcontainer02,
            text='Operação:',
            font= "Verdana 15",
            bg=self.fr_subcontainer02.cget('bg')
        )

        self.lb_texto_resultado_operacao=Label(
            self.fr_subcontainer02,
            text='O resultado aparecerá aqui assim que calcular um produto',
            wraplength=250,
            justify=LEFT,
            bg=self.fr_subcontainer02.cget('bg')
        )

        # Resultado do lucro liquido
        self.lb_title_lucro_liquido = Label(
            self.fr_subcontainer02,
            text='Lucro Liquido',
            font='Verdana',
            bg=self.fr_subcontainer02.cget('bg')
        )

        self.lb_resultado_lucro_liquido = Label(
            self.fr_subcontainer02,
            text='R$ 00,00',
            font='Verdana',
            width=5,
            padx=100,
            pady=5,
            highlightthickness=1,
            highlightbackground='gray',
            bg=self.fr_subcontainer02.cget('bg')
        )


        # Resultado da margem de lucro 
        self.lb_title_margem_lucro = Label(
            self.fr_subcontainer02,
            text='Margem de Lucro',
            font='Verdana',
            bg=self.fr_subcontainer02.cget('bg')
        )

        self.lb_resultado_margem_lucro = Label(
            self.fr_subcontainer02,
            text='0,00 %',
            font='Verdana',
            width=5,
            padx=100,
            pady=5,
            highlightthickness=1,
            highlightbackground='gray',
            bg=self.fr_subcontainer02.cget('bg')
        )



        # Alocando os containers
        self.fr_subcontainer01.grid(row= 0, column= 0, padx= 10, pady= 7, sticky= N)
        self.fr_subcontainer02.grid(row= 0, column= 1, padx= 10, pady= 7, sticky= N)
        self.fr_subcontainer03.grid(row= 0, column= 2, padx= 10, pady= 7, sticky= N)

        # Posicionamento itens do subcontainer 01
        self.lb_title_section01.grid(row= 0, columnspan= 2, pady=10)
        self.lb_nome_produto.grid(row= 1, column= 0, sticky= W, padx= 5, pady= 5)
        self.en_nome_produto.grid(row= 1, column= 1, sticky= W, padx= 5)
        self.lb_qtd_produto.grid(row= 2, column= 0, sticky= W, padx= 5, pady= 5)
        self.en_qtd_produto.grid(row= 2, column= 1, sticky= W, padx= 5)
        self.lb_preco_compra.grid(row= 3, column= 0, sticky= W, padx= 5, pady= 5)
        self.en_preco_compra.grid(row= 3, column= 1, sticky= W, padx= 5)
        self.lb_preco_venda.grid(row= 4, column= 0, sticky= W, padx= 5, pady= 5)
        self.en_preco_venda.grid(row= 4, column= 1, sticky= W, padx= 5)
        self.lb_custo_frete.grid(row= 5, column= 0, sticky= W, padx= 5, pady= 5)
        self.en_custo_frete.grid(row= 5, column= 1, sticky= W, padx= 5)
        self.lb_custo_adicional.grid(row= 6, column= 0, sticky= W, padx= 5, pady= 5)
        self.en_custo_adicional.grid(row= 6, column= 1, sticky= W, padx= 5)


        self.fr_container_btn.grid(row= 7, columnspan= 2, padx= 5)
        self.btn_salvar.grid(row= 7, column= 0, pady = 5, padx = 3)
        self.btn_calcular.grid(row= 7, column= 1, padx = 3)
        self.btn_deletar.grid(row= 7, column= 2, padx = 5)

        
        # Posicionamento itens do subcontainer 02
        self.lb_title_section02.grid(row=0, column=0, pady=10)
        self.lb_texto_resultado_operacao.grid(row=1, column=0, pady=30)
        self.lb_title_lucro_liquido.grid(row=2, column=0)
        self.lb_resultado_lucro_liquido.grid(row=3, column=0, padx=5)
        self.lb_title_margem_lucro.grid(row=4, column=0)
        self.lb_resultado_margem_lucro.grid(row=5, column=0, padx=5, pady=(0,60))




Calculadora_lucro()
 
