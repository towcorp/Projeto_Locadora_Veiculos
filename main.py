from tkinter import*
import tkinter.messagebox as tkMessageBox
import random
import time;
import datetime

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
#===============================================================================================
#========================CALCULOS============================================================================
def CarRentalCost():
 NoofDays = float(NumberofDays.get())
 CarDiscount = float(Discount.get())
 DailyRate = float(DaysRented.get())

 RentalCost = ((NoofDays * DailyRate)* CarDiscount)/100
 CostofRental = "£", str('%.2f'%((NoofDays * DailyRate)- RentalCost))
 Total.set(CostofRental)


 ID = random.randint(51, 95)
 randomID = str (ID)
 CustomerID.set("Car"+ randomID)


 Inv = random.randint(15, 112)
 InvID = str(Inv)
 InvoiceID.set("INV"+ InvID)



#=====================================VARIAVEIS==============================================================
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Var4 = IntVar()
Var5 = IntVar()
Var6 = IntVar()
Var7 = IntVar()
Var8 = IntVar()
CustomerID = StringVar()
DaysRented = StringVar()
Discount = StringVar()
NumberofDays = StringVar()
InvoiceID = StringVar()
Total = StringVar()
Receipt_Ref = StringVar()
DateofOrder = StringVar()
EngineSize = StringVar()
Style = StringVar()
RegisteredYear = StringVar()
ClassID = StringVar()
CarDescription = StringVar()
MilesBefore = StringVar()
MilesAfter = StringVar()
Make = StringVar()
Model = StringVar()
CarColor = StringVar()
EngineMake = StringVar()
CarInsurance = StringVar()
Area = StringVar()
DailyRentalRate = StringVar()
RegistrationNo = StringVar()
IssueBy = StringVar()
IssueDate = StringVar()
LicenceN = StringVar()
Surname = StringVar()
Street = StringVar()
Firstname = StringVar()
Title = StringVar()
Customer = StringVar()
PostCode = StringVar()
#==================================BOTAO SAIR================================================================
def Exit():
    result = tkMessageBox.askquestion("LOCADORA LOCALTO :")
    if result == 'yes' :
        root.destroy()
        return

#============================================================================================================
def Reset():
    Var1.set(0)
    Var2.set(0)
    Var3.set(0)
    Var4.set(0)
    Var5.set(0)
    Var6.set(0)
    Var7.set(0)
    Var8.set(0)
    CustomerID.set("")
    DaysRented.set("")
    NumberofDays.set("")
    InvoiceID.set("")
    Total.set("")
    Receipt_Ref.set("")
    Discount.set("")
    DateofOrder.set("")
    EngineSize.set("")
    Style.set("")
    RegisteredYear.set("")
    ClassID.set("")
    CarDescription.set("")
    MilesBefore.set("")
    MilesAfter.set("")
    Make.set("")
    Model.set("")
    CarColor.set("")
    EngineMake.set("")
    CarInsurance.set("")
    Area.set("")
    DailyRentalRate.set("")
    RegistrationNo.set("")
    IssueBy.set("")
    IssueDate.set("")
    LicenceN.set("")
    Surname.set("")
    Street.set("")
    Firstname.set("")
    Title.set("")
    Customer.set("")
    PostCode.set("")
    txtRecibo.delete("1.0",END)
#========================================================Imprimir===================================
def retrive_imput():
    imputValue = txtRecibo.get("1.0","end-1c")
    print(imputValue)
#========================================================RECIBO======================================
def Receipt():
 txtRecibo.delete("1.0",END)
 x = random.randint(108, 506)
 randomRef = str(x)
 Receipt_Ref.set("BILL"+ randomRef)

 txtRecibo.insert(END,'RCIBO Ref:\t'+ Receipt_Ref.get()+'\n\nData:\t'+ DateofOrder.get()+"\n\n")
 txtRecibo.insert(END, "Servicos: \n\n")

 txtRecibo.insert(END, 'ClienteID: \t'+ CustomerID.get()+ "\n\n")

 txtRecibo.insert(END, 'Valor Diaria: \t\t'+ DaysRented.get()+ "\n\n")


 txtRecibo.insert(END, 'Qtos Dias: \t\t'+ NumberofDays.get()+ "\n\n")

 txtRecibo.insert(END, 'ReciboID: \t\t'+ InvoiceID.get()+ "\n\n")

 txtRecibo.insert(END, 'Disconto: \t\t'+ Discount.get()+ "\n\n")

 txtRecibo.insert(END, 'Total: \t'+ Total.get()+ "\n\n")

 #-------------------------------CAIXA DE TEXTO RECIBO------------------------------------
txtRecibo = Text(RigthMainFrame2,height=17, width=30, bd=8, font=('arial', 12, 'bold'))
txtRecibo.grid(row=0,column=0)

DateofOrder.set(time.strftime("%d/%m/%y"))
#===============================================================================================

 #==================================================================================================
#-------------------------------CAMPO FORMULARIO TOPO--------------------------------------------

lblCustomer=Label(LeftMainFrame1,font=('arial',11,'bold'),text='Cliente   :',bd=8)
lblCustomer.grid(row=0,column=0,sticky=W)
txtCustomer=Entry(LeftMainFrame1, font=('arial',10,'bold'),bd=2,textvariable=Customer,width=31,justify='left')
txtCustomer.grid(row=0,column=1)


lblTitle=Label(LeftMainFrame1,font=('arial',11,'bold'),text='Apelido   :',bd=8)
lblTitle.grid(row=0,column=2,sticky=W)
txtTitle=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Title, width=31,justify='left')
txtTitle.grid(row=0,column=3)


lblFirstname=Label(LeftMainFrame1,font=('arial',11,'bold'),text='Nome   :',bd=8)
lblFirstname.grid(row=0,column=4,sticky=W)
txtFirstname=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Firstname, width=31,justify='left')
txtFirstname.grid(row=0,column=5)


lblSurname=Label(LeftMainFrame1,font=('arial',11,'bold'),text='S-Nome   :',bd=8)
lblSurname.grid(row=1,column=0,sticky=W)
txtSurname=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Surname, width=31,justify='left')
txtSurname.grid(row=1,column=1)


lblStreet=Label(LeftMainFrame1,font=('arial',11,'bold'),text='Rua   :',bd=8)
lblStreet.grid(row=1,column=2,sticky=W)
txtStreet=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Street, width=31,justify='left')
txtStreet.grid(row=1,column=3)


lblArea=Label(LeftMainFrame1,font=('arial',11,'bold'),text='Area   :',bd=8)
lblArea.grid(row=1,column=4,sticky=W)
txtArea=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Area, width=31,justify='left')
txtArea.grid(row=1,column=5)



lblPostCode=Label(LeftMainFrame1,font=('arial',11,'bold'),text='Cod Postal  :',bd=8)
lblPostCode.grid(row=2,column=0,sticky=W)
txtPostCode=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=PostCode, width=31,justify='left')
txtPostCode.grid(row=2,column=1)


lblLicenceNo=Label(LeftMainFrame1,font=('arial',11,'bold'),text='N-CNH   :',bd=8)
lblLicenceNo.grid(row=2,column=2,sticky=W)
txtLicenceNo=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=LicenceN, width=31,justify='left')
txtLicenceNo.grid(row=2,column=3)


lblIssueDate=Label(LeftMainFrame1,font=('arial',11,'bold'),text='Data  :',bd=8)
lblIssueDate.grid(row=2,column=4,sticky=W)
txtIssueDate=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=IssueDate, width=31,justify='left')
txtIssueDate.grid(row=2,column=5)



lblIssueBy=Label(LeftMainFrame1,font=('arial',11,'bold'),text='Local   :',bd=8)
lblIssueBy.grid(row=3,column=0,sticky=W)
txtIssueBy=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=IssueBy, width=31,justify='left')
txtIssueBy.grid(row=3,column=1)


lblRegistrationNo=Label(LeftMainFrame1,font=('arial',11,'bold'),text='N-Doc-Carro   :',bd=8)
lblRegistrationNo.grid(row=3,column=2,sticky=W)
txtRegistrationNo=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=RegistrationNo, width=31,justify='left')
txtRegistrationNo.grid(row=3,column=3)


lblRentalRate=Label(LeftMainFrame1,font=('arial',11,'bold'),text='Total Dias   :',bd=8)
lblRentalRate.grid(row=3,column=4,sticky=W)
txtRentalRate=Entry(LeftMainFrame1,font=('arial',10,'bold'),bd=2,textvariable=DailyRentalRate, width=31,justify='left')
txtRentalRate.grid(row=3,column=5)
#===============================================================================================

#-------------------------------CAMPO FORMULARIO MEIO--------------------------------------------

lblEngineSize=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Tipo Motor:',bd=8)
lblEngineSize.grid(row=0,column=0,sticky=W)
txtEngineSize=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=EngineSize,
                   width=31,justify='left')
txtEngineSize.grid(row=0,column=1)


lblStyle=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Estilo:',bd=8)
lblStyle.grid(row=0,column=2,sticky=W)
txtStyle=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=Style,
                   width=31,justify='left')
txtStyle.grid(row=0,column=3)


lblRegisteredYear=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Carro-Ano:',bd=8)
lblRegisteredYear.grid(row=0,column=4,sticky=W)
txtRegisteredYear=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=RegisteredYear,
                   width=31,justify='left')
txtRegisteredYear.grid(row=0,column=5)


lblClassID=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Clase-Carro:',bd=8)
lblClassID.grid(row=1,column=0,sticky=W)
txtClassID=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=ClassID,
                   width=31,justify='left')
txtClassID.grid(row=1,column=1)


lblCarDescription=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Desc-Carro:',bd=8)
lblCarDescription.grid(row=1,column=2,sticky=W)
txtCarDescription=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=CarDescription,
                   width=31,justify='left')
txtCarDescription.grid(row=1,column=3)


lblMilesBefore=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Km-Anterior:',bd=8)
lblMilesBefore.grid(row=1,column=4,sticky=W)
txtMilesBefore=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=MilesBefore,
                   width=31,justify='left')
txtMilesBefore.grid(row=1,column=5)



lblMilesAfter=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Km-Entrega:',bd=8)
lblMilesAfter.grid(row=2,column=0,sticky=W)
txtMilesAfter=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=MilesAfter,
                   width=31,justify='left')
txtMilesAfter.grid(row=2,column=1)


lblMake=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Fab-Carro:',bd=8)
lblMake.grid(row=2,column=2,sticky=W)
txtMake=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=Make,
                   width=31,justify='left')
txtMake.grid(row=2,column=3)


lblModel=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Modelo:',bd=8)
lblModel.grid(row=2,column=4,sticky=W)
txtModel=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=Model,
                   width=31,justify='left')
txtModel.grid(row=2,column=5)



lblEngineMake=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Fab-Motor:',bd=8)
lblEngineMake.grid(row=3,column=0,sticky=W)
txtEngineMake=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=EngineMake,
                   width=31,justify='left')
txtEngineMake.grid(row=3,column=1)


lblCarColor=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Cor-Carro:',bd=8)
lblCarColor.grid(row=3,column=2,sticky=W)
txtCarColor=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=CarColor,
                   width=31,justify='left')
txtCarColor.grid(row=3,column=3)


lblCarInsurance=Label(LeftMainFrame2,font=('arial',11,'bold'),text='Seguro-Carro:',bd=8)
lblCarInsurance.grid(row=3,column=4,sticky=W)
txtCarInsurance=Entry(LeftMainFrame2,font=('arial',10,'bold'),bd=2,textvariable=CarInsurance,
                   width=31,justify='left')
txtCarInsurance.grid(row=3,column=5)
#===============================================================================================

#-------------------------------CAMPO FORMULARIO RODAPE--------------------------------------------

lblCustomerID=Label(LeftMainFrame3,font=('arial',11,'bold'),text='Cliente ID :',bd=8)
lblCustomerID.grid(row=0,column=0,sticky=W)
txtCustomerID=Entry(LeftMainFrame3,font=('arial',10,'bold'),bd=2,textvariable=CustomerID,
                   width=31,justify='left')
txtCustomerID.grid(row=0,column=1)


lblDaysRented=Label(LeftMainFrame3,font=('arial',11,'bold'),text='Total-D-Alugado :',bd=8)
lblDaysRented.grid(row=0,column=2,sticky=W)
txtDaysRented=Entry(LeftMainFrame3,font=('arial',10,'bold'),bd=2,textvariable=DaysRented,
                   width=31,justify='left')
txtDaysRented.grid(row=0,column=3)


lblDiscount=Label(LeftMainFrame3,font=('arial',11,'bold'),text='Disconto :',bd=8)
lblDiscount.grid(row=0,column=4,sticky=W)
txtDiscount=Entry(LeftMainFrame3,font=('arial',10,'bold'),bd=2,textvariable=Discount,
                   width=31,justify='left')
txtDiscount.grid(row=0,column=5)


lblNumberofDays=Label(LeftMainFrame3,font=('arial',11,'bold'),text='Total-Dias :',bd=8)
lblNumberofDays.grid(row=1,column=0,sticky=W)
txtNumberofDays=Entry(LeftMainFrame3,font=('arial',10,'bold'),bd=2,textvariable=NumberofDays,
                   width=31,justify='left')
txtNumberofDays.grid(row=1,column=1)


lblInvoiceID=Label(LeftMainFrame3,font=('arial',11,'bold'),text='ID-Fatura :',bd=8)
lblInvoiceID.grid(row=1,column=2,sticky=W)
txtInvoiceID=Entry(LeftMainFrame3,font=('arial',10,'bold'),bd=2,textvariable=InvoiceID,
                   width=31,justify='left')
txtInvoiceID.grid(row=1,column=3)


lblTotal=Label(LeftMainFrame3,font=('arial',11,'bold'),text='Total  :',bd=8)
lblTotal.grid(row=1,column=4,sticky=W)
txtTotal=Entry(LeftMainFrame3,font=('arial',10,'bold'),bd=2,textvariable=Total,
                   width=31,justify='left')
txtTotal.grid(row=1,column=5)
#===============================================================================================





#-------------------------------BOTOES PRINCIPAIS----------------------------------------
cmdTotal = Button(LeftMainFrame4,text='TOTAL',padx=2,bd=4,fg='SteelBlue4',bg='LightSteelBlue', font=('arial',16,'bold'), width=15, height=2,command=CarRentalCost).grid(row=0,column=0)
cmdRecibo = Button(LeftMainFrame4,text='RECIBO',padx=2,bd=4,fg='SteelBlue4',bg='LightSteelBlue', font=('arial',16,'bold'), width=15, height=2,command=Receipt).grid(row=0,column=2)
cmdLimpar = Button(LeftMainFrame4,text='LIMPAR',padx=2,bd=4,fg='SteelBlue4',bg='LightSteelBlue', font=('arial',16,'bold'), width=15, height=2,command=Reset).grid(row=0,column=3)
cmdImprimir = Button(LeftMainFrame4,text='IMPRIMIR',padx=2,bd=4,fg='SteelBlue4',bg='LightSteelBlue', font=('arial',16,'bold'), width=15, height=2,command=lambda:  retrive_imput()).grid(row=0,column=4)
cmdSair = Button(LeftMainFrame4,text='SAIR',padx=2,bd=4,fg='DarkRed',bg='RosyBrown1', font=('arial',16,'bold'), width=15, height=2,command=Exit).grid(row=0,column=5)

#===============================================================================================


#=====================CAMPO DA DIREITA TOPO=====================================================
style = Checkbutton(RigthMainFrame1, text='style\t\t\t', onvalue=1, offvalue=0,bg='LightSteelBlue', font=('arial', 15, 'bold')).grid(row=0, sticky=W)
style = Checkbutton(RigthMainFrame1, text='Classe ID\t\t', onvalue=1, offvalue=0,bg='LightSteelBlue', font=('arial', 15, 'bold')).grid(row=1, sticky=W)
style = Checkbutton(RigthMainFrame1, text='Fatura ID\t\t\t', onvalue=1, offvalue=0,bg='LightSteelBlue', font=('arial', 15, 'bold')).grid(row=2, sticky=W)
style = Checkbutton(RigthMainFrame1, text='Diária\t\t\t', onvalue=1, offvalue=0,bg='LightSteelBlue', font=('arial', 15, 'bold')).grid(row=3, sticky=W)
style = Checkbutton(RigthMainFrame1, text='Automático\t\t', onvalue=1, offvalue=0,bg='LightSteelBlue', font=('arial', 15, 'bold')).grid(row=4, sticky=W)
style = Checkbutton(RigthMainFrame1, text='Ar Condicionado\t\t', onvalue=1, offvalue=0,bg='LightSteelBlue', font=('arial', 15, 'bold')).grid(row=5, sticky=W)
style = Checkbutton(RigthMainFrame1, text='Seguro Incluso\t\t', onvalue=1, offvalue=0,bg='LightSteelBlue', font=('arial', 15, 'bold')).grid(row=6, sticky=W)
style = Checkbutton(RigthMainFrame1, text='Detalhes Cliente\t\t', onvalue=1, offvalue=0,bg='LightSteelBlue', font=('arial', 15, 'bold')).grid(row=7, sticky=W)







#-------------------------------MAIN----------------------------------------
root.mainloop()