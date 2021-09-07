from tkinter import * 

#-------------------------------CRIACAO DA TELA PRINCIPAL-------------------------------
root = Tk()
root.title("Locação de Veiculos Localto")
root.geometry("1350x670+0+0")

#-------------------------------FRAME ESQUERDO------------------------------------------
LeftMainFrame = Frame(root,width=1000,height=850,bd=2,relief="raise")
LeftMainFrame.pack(side=LEFT)

#-------------------------------FRAME DIREITO-------------------------------------------
RigthMainFrame = Frame(root,width=350,height=850,bd=2,relief="raise")
RigthMainFrame.pack(side=RIGHT)

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

#-------------------------------CAIXA DE TEXTO RECIBO------------------------------------
txtRecibo = Text(RigthMainFrame2,height=16, width=37, bd=3, font=('arial', 12, 'bold')).grid(row=0, column=0)

#-------------------------------CAMPO FORMULARIO RODAPE--------------------------------------------
labelClienteID = Label(LeftMainFrame3, font=('arial',10,'bold'), text='Cliente ID', bd=8)
labelClienteID.grid(row=0, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=1)

labelClienteID = Label(LeftMainFrame3, font=('arial',10,'bold'), text='Dias Contratados', bd=8)
labelClienteID.grid(row=0, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=3)

labelClienteID = Label(LeftMainFrame3, font=('arial',10,'bold'), text='Desconto', bd=8)
labelClienteID.grid(row=0, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=5)

labelClienteID = Label(LeftMainFrame3, font=('arial',10,'bold'), text='Total Dias', bd=8)
labelClienteID.grid(row=1, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=1)

labelClienteID = Label(LeftMainFrame3, font=('arial',10,'bold'), text='Id fatura', bd=8)
labelClienteID.grid(row=1, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=3)

labelClienteID = Label(LeftMainFrame3, font=('arial',10,'bold'), text='Total', bd=8)
labelClienteID.grid(row=1, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame3,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=5)


#-------------------------------CAMPO FORMULARIO MEIO--------------------------------------------
labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='1', bd=8)
labelClienteID.grid(row=0, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='2', bd=8)
labelClienteID.grid(row=0, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='3', bd=8)
labelClienteID.grid(row=0, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=5)



labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='4', bd=8)
labelClienteID.grid(row=1, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='5', bd=8)
labelClienteID.grid(row=1, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='6', bd=8)
labelClienteID.grid(row=1, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=5)




labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='7', bd=8)
labelClienteID.grid(row=2, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='8', bd=8)
labelClienteID.grid(row=2, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='9', bd=8)
labelClienteID.grid(row=2, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=5)



labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='10', bd=8)
labelClienteID.grid(row=3, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=1)

labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='11', bd=8)
labelClienteID.grid(row=3, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=3)

labelClienteID = Label(LeftMainFrame2, font=('arial',10,'bold'), text='12', bd=8)
labelClienteID.grid(row=3, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=5)



#-------------------------------CAMPO FORMULARIO TOPO--------------------------------------------
labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='1', bd=8)
labelClienteID.grid(row=0, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='2', bd=8)
labelClienteID.grid(row=0, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='3', bd=8)
labelClienteID.grid(row=0, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=0, column=5)



labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='4', bd=8)
labelClienteID.grid(row=1, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='5', bd=8)
labelClienteID.grid(row=1, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='6', bd=8)
labelClienteID.grid(row=1, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=1, column=5)




labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='7', bd=8)
labelClienteID.grid(row=2, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='8', bd=8)
labelClienteID.grid(row=2, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='9', bd=8)
labelClienteID.grid(row=2, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=2, column=5)



labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='10', bd=8)
labelClienteID.grid(row=3, column=0, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=1)

labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='11', bd=8)
labelClienteID.grid(row=3, column=2, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=3)

labelClienteID = Label(LeftMainFrame1, font=('arial',10,'bold'), text='12', bd=8)
labelClienteID.grid(row=3, column=4, sticky=W)
txtClienteID = Entry(LeftMainFrame1,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtClienteID.grid(row=3, column=5)


#-------------------------------BOTOES PRINCIPAIS----------------------------------------
cmdTotal = Button(LeftMainFrame4,text='Total',padx=1,bd=2,fg='blue',bg='grey', font=('arial',12,'bold'), width=20, height=3).grid(row=0, column=0)
cmdRecibo = Button(LeftMainFrame4,text='Recibo',padx=1,bd=2,fg='blue',bg='grey', font=('arial',12,'bold'), width=20, height=3).grid(row=0, column=1)
cmdLimpar = Button(LeftMainFrame4,text='Limpar',padx=1,bd=2,fg='blue',bg='grey', font=('arial',12,'bold'), width=20, height=3).grid(row=0, column=2)
cmdSair = Button(LeftMainFrame4,text='Sair',padx=1,bd=2,fg='red',bg='grey', font=('arial',12,'bold'), width=20, height=3).grid(row=0, column=3)






#-------------------------------MAIN----------------------------------------
root.mainloop()