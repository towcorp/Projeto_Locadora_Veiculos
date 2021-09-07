from tkinter import * 

#==============================CRIACAO DA TELA PRINCIPAL=================================
root = Tk()
root.title("Locação de Veiculos Localto")
root.geometry("1350x680+0+0")
root.configure(bg='SteelBlue')

#-------------------------------PRINCIPAL ESQUERDO------------------------------------------

LeftMainFrame = Frame(root,width=1000,height=650,bd=2,relief="raise", bg='LightSteelBlue')
LeftMainFrame.pack(side=LEFT)

#-------------------------------PRINCIPAL DIREITO-------------------------------------------

RigthMainFrame = Frame(root,width=350,height=650,bd=2,relief="raise")
RigthMainFrame.pack(side=RIGHT)

#-------------------------------CABECALHO TOPO----------------------------------------------

LeftMainFrame0 = Frame(LeftMainFrame, bg='LightSteelBlue', width=1000,height=100,bd=1,relief="raise")
LeftMainFrame0.pack(side=TOP)

labelTitle = Label(LeftMainFrame0, font=('arial',55,'bold'), text='Locação de Veiculos Localto', bd=8, bg='LightSteelBlue', fg='SteelBlue')
labelTitle.grid(row=0, column=0, sticky=W)

#-------------------------------FRAME DIV ESQUERDO--------------------------------------

LeftMainFrame1 = Frame(LeftMainFrame,width=1000,height=225,bd=4,relief="raise")
LeftMainFrame1.pack(side=TOP)
LeftMainFrame2 = Frame(LeftMainFrame,width=1000,height=225,bd=4,relief="raise")
LeftMainFrame2.pack(side=TOP)
LeftMainFrame3 = Frame(LeftMainFrame,width=1000,height=100,bd=4,relief="raise")
LeftMainFrame3.pack(side=TOP)
LeftMainFrame4 = Frame(LeftMainFrame,width=1000,height=100,bd=8,relief="raise")
LeftMainFrame4.pack(side=TOP)

#-------------------------------FRAME DIV DIREITO---------------------------------------

RigthMainFrame1 = Frame(RigthMainFrame,width=350,height=325,bd=8,relief="raise")
RigthMainFrame1.pack(side=TOP)
RigthMainFrame2 = Frame(RigthMainFrame,width=350,height=325,bd=8,relief="raise")
RigthMainFrame2.pack(side=BOTTOM)

#-------------------------------CAMPO FORMULARIO TOPO--------------------------------------------

labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Cliente :', bd=8)
labelClienteID.grid(row=0, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=2, width=31, justify='left')
txtClienteID.grid(row=0, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Apelido :', bd=8)
labelClienteID.grid(row=0, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Nome :', bd=8)
labelClienteID.grid(row=0, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Sobrenome :', bd=8)
labelClienteID.grid(row=1, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Endereco :', bd=8)
labelClienteID.grid(row=1, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Area :', bd=8)
labelClienteID.grid(row=1, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='CEP :', bd=8)
labelClienteID.grid(row=2, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='CNH :', bd=8)
labelClienteID.grid(row=2, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Validade :', bd=8)
labelClienteID.grid(row=2, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Local :', bd=8)
labelClienteID.grid(row=3, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Doc Veiculo :', bd=8)
labelClienteID.grid(row=3, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',12,'bold'), text='Total Dias :', bd=8)
labelClienteID.grid(row=3, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=5)




#-------------------------------CAMPO FORMULARIO MEIO--------------------------------------------

labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Tipo Motor :', bd=8)
labelClienteID.grid(row=0, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Estilo :', bd=8)
labelClienteID.grid(row=0, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Ano :', bd=8)
labelClienteID.grid(row=0, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Classe :', bd=8)
labelClienteID.grid(row=1, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Desc Veiculo :', bd=8)
labelClienteID.grid(row=1, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Km Atual :', bd=8)
labelClienteID.grid(row=1, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Km Final :', bd=8)
labelClienteID.grid(row=2, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Fab Veiculo :', bd=8)
labelClienteID.grid(row=2, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Modelo :', bd=8)
labelClienteID.grid(row=2, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Fab Motor :', bd=8)
labelClienteID.grid(row=3, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Cor Veiculo :', bd=8)
labelClienteID.grid(row=3, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',12,'bold'), text='Seguro N. :', bd=8)
labelClienteID.grid(row=3, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=5)


#-------------------------------CAMPO FORMULARIO RODAPE--------------------------------------------

labelClienteID = Label(LeftMainFrame3, font=('arial',11,'bold'), text='Cliente ID :', bd=8)
labelClienteID.grid(row=0, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=1)

labelClienteID = Label(LeftMainFrame3, font=('arial',11,'bold'), text='Dias Contratados :', bd=8)
labelClienteID.grid(row=0, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=3)

labelClienteID = Label(LeftMainFrame3, font=('arial',11,'bold'), text='Desconto :', bd=8)
labelClienteID.grid(row=0, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame3, font=('arial',11,'bold'), text='Total Dias :', bd=8)
labelClienteID.grid(row=1, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=1)

labelClienteID = Label(LeftMainFrame3, font=('arial',11,'bold'), text='Id fatura :', bd=8)
labelClienteID.grid(row=1, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=3)

labelClienteID = Label(LeftMainFrame3, font=('arial',11,'bold'), text='Total :', bd=8)
labelClienteID.grid(row=1, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=5)


#-------------------------------CAIXA DE TEXTO RECIBO------------------------------------
txtRecibo = Text(RigthMainFrame2,height=10, width=24, bd=8, font=('arial', 12, 'bold')).grid(row=0, column=0)


#-------------------------------BOTOES PRINCIPAIS----------------------------------------
cmdTotal = Button(LeftMainFrame4,text='TOTAL',padx=2,bd=4,fg='SteelBlue4',bg='LightSteelBlue', font=('arial',16,'bold'), width=19, height=2).grid(row=0, column=0)
cmdRecibo = Button(LeftMainFrame4,text='RECIBO',padx=2,bd=4,fg='SteelBlue4',bg='LightSteelBlue', font=('arial',16,'bold'), width=19, height=2).grid(row=0, column=2)
cmdLimpar = Button(LeftMainFrame4,text='LIMPAR',padx=2,bd=4,fg='SteelBlue4',bg='LightSteelBlue', font=('arial',16,'bold'), width=19, height=2).grid(row=0, column=3)
cmdSair = Button(LeftMainFrame4,text='SAIR',padx=2,bd=4,fg='DarkRed',bg='RosyBrown1', font=('arial',16,'bold'), width=19, height=2).grid(row=0, column=4)






#-------------------------------MAIN----------------------------------------
root.mainloop()