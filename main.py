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

#-------------------------------BOTOES PRINCIPAIS----------------------------------------
cmdTotal = Button(LeftMainFrame4,text='Total',padx=1,bd=2,fg='blue',bg='grey', font=('arial',12,'bold'), width=20, height=3).grid(row=0, column=0)
cmdRecibo = Button(LeftMainFrame4,text='Recibo',padx=1,bd=2,fg='blue',bg='grey', font=('arial',12,'bold'), width=20, height=3).grid(row=0, column=1)
cmdLimpar = Button(LeftMainFrame4,text='Limpar',padx=1,bd=2,fg='blue',bg='grey', font=('arial',12,'bold'), width=20, height=3).grid(row=0, column=2)
cmdSair = Button(LeftMainFrame4,text='Sair',padx=1,bd=2,fg='red',bg='grey', font=('arial',12,'bold'), width=20, height=3).grid(row=0, column=3)



#-------------------------------MAIN----------------------------------------
root.mainloop()