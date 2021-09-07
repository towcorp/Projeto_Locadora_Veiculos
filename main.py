from tkinter import * 

#==============================CRIACAO DA TELA PRINCIPAL=================================
root = Tk()
root.title("Locação de Veiculos Localto")
root.geometry("1350x670+0+0")



#-------------------------------FRAME ESQUERDO------------------------------------------

LeftMainFrame = Frame(root,width=1000,height=650,bd=2,relief="raise")
LeftMainFrame.pack(side=LEFT)

#-------------------------------FRAME DIREITO-------------------------------------------

RigthMainFrame = Frame(root,width=350,height=650,bd=2,relief="raise")
RigthMainFrame.pack(side=RIGHT)

#-------------------------------FRAME TOPO----------------------------------------------

LeftMainFrame0 = Frame(LeftMainFrame, bg='light blue', width=1000,height=200,bd=1,relief="raise")
LeftMainFrame0.pack(side=TOP)


#-------------------------------FRAME DIV ESQUERDO--------------------------------------

LeftMainFrame1 = Frame(LeftMainFrame,width=1000,height=225,bd=2,relief="raise")
LeftMainFrame1.pack(side=TOP)
LeftMainFrame2 = Frame(LeftMainFrame,width=1000,height=225,bd=2,relief="raise")
LeftMainFrame2.pack(side=TOP)
LeftMainFrame3 = Frame(LeftMainFrame,width=1000,height=100,bd=2,relief="raise")
LeftMainFrame3.pack(side=TOP)
LeftMainFrame4 = Frame(LeftMainFrame,width=1000,height=100,bd=2,relief="raise")
LeftMainFrame4.pack(side=TOP)

#-------------------------------FRAME DIV DIREITO---------------------------------------

RigthMainFrame1 = Frame(RigthMainFrame,width=350,height=325,bd=2,relief="raise")
RigthMainFrame1.pack(side=TOP)
RigthMainFrame2 = Frame(RigthMainFrame,width=350,height=325,bd=2,relief="raise")
RigthMainFrame2.pack(side=BOTTOM)

#-------------------------------CAMPO FORMULARIO TOPO--------------------------------------------

labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Cliente:', bd=8)
labelClienteID.grid(row=0, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Apelido:', bd=8)
labelClienteID.grid(row=0, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Nome:', bd=8)
labelClienteID.grid(row=0, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Sobrenome:', bd=8)
labelClienteID.grid(row=1, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Endereco:', bd=8)
labelClienteID.grid(row=1, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Area:', bd=8)
labelClienteID.grid(row=1, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='CEP:', bd=8)
labelClienteID.grid(row=2, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='CNH:', bd=8)
labelClienteID.grid(row=2, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Validade:', bd=8)
labelClienteID.grid(row=2, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Local:', bd=8)
labelClienteID.grid(row=3, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Doc Veiculo:', bd=8)
labelClienteID.grid(row=3, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',11,'bold'), text='Dias contratados:', bd=8)
labelClienteID.grid(row=3, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=5)




#-------------------------------CAMPO FORMULARIO MEIO--------------------------------------------

labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Tipo Motor:', bd=8)
labelClienteID.grid(row=0, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Estilo:', bd=8)
labelClienteID.grid(row=0, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Ano Veiculo:', bd=8)
labelClienteID.grid(row=0, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Classe Veiculo:', bd=8)
labelClienteID.grid(row=1, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Desc Veiculo:', bd=8)
labelClienteID.grid(row=1, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Km Atual:', bd=8)
labelClienteID.grid(row=1, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Km Final:', bd=8)
labelClienteID.grid(row=2, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Fab Veiculo:', bd=8)
labelClienteID.grid(row=2, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Modelo:', bd=8)
labelClienteID.grid(row=2, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Fab Motor:', bd=8)
labelClienteID.grid(row=3, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Cor Veiculo:', bd=8)
labelClienteID.grid(row=3, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',11,'bold'), text='Seguro Veiculo:', bd=8)
labelClienteID.grid(row=3, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=5)


#-------------------------------CAMPO FORMULARIO RODAPE--------------------------------------------

labelClienteID = Label(LeftMainFrame3, font=('arial',13,'bold'), text='Cliente ID:', bd=8)
labelClienteID.grid(row=0, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=1)

labelClienteID = Label(LeftMainFrame3, font=('arial',13,'bold'), text='Dias Contratados:', bd=8)
labelClienteID.grid(row=0, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=3)

labelClienteID = Label(LeftMainFrame3, font=('arial',13,'bold'), text='Desconto:', bd=8)
labelClienteID.grid(row=0, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=5)
#-------------------------------------------------------------------------------------------------
labelClienteID = Label(LeftMainFrame3, font=('arial',13,'bold'), text='Total Dias:', bd=8)
labelClienteID.grid(row=1, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=1)

labelClienteID = Label(LeftMainFrame3, font=('arial',13,'bold'), text='Id fatura:', bd=8)
labelClienteID.grid(row=1, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=3)

labelClienteID = Label(LeftMainFrame3, font=('arial',13,'bold'), text='Total:', bd=8)
labelClienteID.grid(row=1, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=5)


#-------------------------------CAIXA DE TEXTO RECIBO------------------------------------
txtRecibo = Text(RigthMainFrame2,height=10, width=24, bd=8, font=('arial', 12, 'bold')).grid(row=0, column=0)


#-------------------------------BOTOES PRINCIPAIS----------------------------------------
cmdTotal = Button(LeftMainFrame4,text='Total',padx=4,bd=2,fg='blue',bg='grey', font=('arial',12,'bold'), width=18, height=3).grid(row=0, column=0)
cmdRecibo = Button(LeftMainFrame4,text='Recibo',padx=4,bd=2,fg='blue',bg='grey', font=('arial',12,'bold'), width=18, height=3).grid(row=0, column=2)
cmdLimpar = Button(LeftMainFrame4,text='Limpar',padx=4,bd=2,fg='blue',bg='grey', font=('arial',12,'bold'), width=18, height=3).grid(row=0, column=3)
cmdSair = Button(LeftMainFrame4,text='Sair',padx=4,bd=2,fg='red',bg='grey', font=('arial',12,'bold'), width=18, height=3).grid(row=0, column=4)






#-------------------------------MAIN----------------------------------------
root.mainloop()