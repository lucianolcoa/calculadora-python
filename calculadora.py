from tkinter import*
#coding: UTF-8
import math
import graus
from sympy  import*
x,y,z = symbols('x y z')

class janela:

    def __init__(self,argumento):
        self.anss=0
        self.acalcula=0
        self.aderiva=0
        self.aintegra=0
        self.aresposta=0
        self.muda=0
        self.entra=""
        self.botaocalcula=Button(raiz,text=" simples",command=self.calcula,width=10)
        self.botaocalcula.configure(font="Arial 12",background="black",foreground="white")
        self.botaocalcula.grid(row=0,column=0)
        self.botaointegral=Button(raiz,text=" integral",command=self.integral,width=10)
        self.botaointegral.configure(font="Arial 12",background="black",foreground="white")
        self.botaointegral.grid(row=0,column=1)
        self.botaoderivada=Button(raiz,text=" derivada",command=self.derivada,width=10)
        self.botaoderivada.configure(font="Arial 12",background="black",foreground="white")
        self.botaoderivada.grid(row=0,column=2)
        self.botaonum1=Button(raiz,text="1",width=1)
        self.botaonum1.configure(font="Arial 11",background="black",foreground="white",command=self.letra1)
        self.botaonum1.grid(row=0,column=4,rowspan=1)
        self.botaonum2=Button(raiz,text="2",width=1)
        self.botaonum2.configure(font="Arial 11",background="black",foreground="white",command=self.letra2)
        self.botaonum2.grid(row=0,column=5,rowspan=1)
        self.botaonum3=Button(raiz,text="3",width=1)
        self.botaonum3.configure(font="Arial 11",background="black",foreground="white",command=self.letra3)
        self.botaonum3.grid(row=0,column=6,rowspan=1)
        self.botaonum4=Button(raiz,text="4",width=1)
        self.botaonum4.configure(font="Arial 11",background="black",foreground="white",command=self.letra4)
        self.botaonum4.grid(row=0,column=7,rowspan=1)
        self.botaonum5=Button(raiz,text="5",width=1)
        self.botaonum5.configure(font="Arial 11",background="black",foreground="white",command=self.letra5)
        self.botaonum5.grid(row=0,column=8,rowspan=1)
        self.botaonum6=Button(raiz,text="6",width=1)
        self.botaonum6.configure(font="Arial 11",background="black",foreground="white",command=self.letra6)
        self.botaonum6.grid(row=0,column=9,rowspan=1)
        self.botaonum7=Button(raiz,text="7",width=1)
        self.botaonum7.configure(font="Arial 11",background="black",foreground="white",command=self.letra7)
        self.botaonum7.grid(row=1,column=4,rowspan=2)
        self.botaonum8=Button(raiz,text="8",width=1)
        self.botaonum8.configure(font="Arial 11",background="black",foreground="white",command=self.letra8)
        self.botaonum8.grid(row=1,column=5,rowspan=2)
        self.botaonum9=Button(raiz,text="9",width=1)
        self.botaonum9.configure(font="Arial 11",background="black",foreground="white",command=self.letra9)
        self.botaonum9.grid(row=1,column=6,rowspan=2)
        self.botaonum9=Button(raiz,text="0",width=1)
        self.botaonum9.configure(font="Arial 11",background="black",foreground="white",command=self.letra0)
        self.botaonum9.grid(row=1,column=7,rowspan=2)
        self.botaonumm=Button(raiz,text="*",width=1)
        self.botaonumm.configure(font="Arial 11",background="black",foreground="white",command=self.letramu)
        self.botaonumm.grid(row=1,column=8)
        self.botaonumma=Button(raiz,text="+",width=1)
        self.botaonumma.configure(font="Arial 11",background="black",foreground="white",command=self.letrama)
        self.botaonumma.grid(row=1,column=9)
        self.botaonumme=Button(raiz,text="-",width=1)
        self.botaonumme.configure(font="Arial 11",background="black",foreground="white",command=self.letrame)
        self.botaonumme.grid(row=2,column=4,rowspan=2)
        self.botaonumdi=Button(raiz,text="/",width=1)
        self.botaonumdi.configure(font="Arial 11",background="black",foreground="white",command=self.letraba)
        self.botaonumdi.grid(row=2,column=5,rowspan=2)
        self.botaonumcos=Button(raiz,text="co",width=1)
        self.botaonumcos.configure(font="Arial 11",background="black",foreground="white",command=self.letraco)
        self.botaonumcos.grid(row=2,column=6,rowspan=2)
        self.botaonumsin=Button(raiz,text="si",width=1)
        self.botaonumsin.configure(font="Arial 11",background="black",foreground="white",command=self.letrasi)
        self.botaonumsin.grid(row=2,column=7,rowspan=2)
        self.botaonumln=Button(raiz,text="ln",width=1)
        self.botaonumln.configure(font="Arial 11",background="black",foreground="white",command=self.letraln)
        self.botaonumln.grid(row=2,column=8,rowspan=2)
        self.botaonumlog=Button(raiz,text="lo",width=1)
        self.botaonumlog.configure(font="Arial 11",background="black",foreground="white",command=self.letralo)
        self.botaonumlog.grid(row=2,column=9,rowspan=2)
        self.botaonumex=Button(raiz,text="ex",width=1)
        self.botaonumex.configure(font="Arial 11",background="black",foreground="white",command=self.letraexp)
        self.botaonumex.grid(row=0,column=10)
        self.botaonumpoll=Button(raiz,text="in",width=1,command=self.letrainterpol)
        self.botaonumpoll.configure(font="Arial 10",background="black",foreground="white")
        self.botaonumpoll.grid(row=0,column=11)
        self.botaonumdet=Button(raiz,text="de",width=1,command=self.letradeter)
        self.botaonumdet.configure(font="Arial 10",background="black",foreground="white")
        self.botaonumdet.grid(row=0,column=12)
        self.botaonumpard=Button(raiz,text="(",width=1,command=self.letrapard)
        self.botaonumpard.configure(font="Arial 11",background="black",foreground="white")
        self.botaonumpard.grid(row=1,column=10)
        self.botaonumpare=Button(raiz,text=")",width=1)
        self.botaonumpare.configure(font="Arial 11",background="black",foreground="white",command=self.letrapare)
        self.botaonumpare.grid(row=1,column=11)
        self.botaonumpp=Button(raiz,text=".")
        self.botaonumpp.configure(font="Arial 11",background="black",foreground="white",command=self.letrapt)
        self.botaonumpp.grid(row=1,column=12)
        self.botaonumcold=Button(raiz,text="[")
        self.botaonumcold.configure(font="Arial 10",background="black",foreground="white",command=self.letracold)
        self.botaonumcold.grid(row=3,column=10)
        self.botaonumcole=Button(raiz,text="]")
        self.botaonumcole.configure(font="Arial 10",background="black",foreground="white",command=self.letracole)
        self.botaonumcole.grid(row=3,column=11)
        self.botaonumvi=Button(raiz,text=",")
        self.botaonumvi.configure(font="Arial 10",background="black",foreground="white",command=self.letravir)
        self.botaonumvi.grid(row=3,column=12)
        self.botaonumdel=Button(raiz,text="dl",width=1)
        self.botaonumdel.configure(font="Arial 10",background="black",foreground="white",command=self.letradel)
        self.botaonumdel.grid(row=0,column=13)
        self.botaonumx=Button(raiz,text="x",width=1)
        self.botaonumx.configure(font="Arial 10",background="black",foreground="white",command=self.letrax)
        self.botaonumx.grid(row=4,column=4)
        self.botaonumy=Button(raiz,text="y",width=1)
        self.botaonumy.configure(font="Arial 10",background="black",foreground="white",command=self.letray)
        self.botaonumy.grid(row=4,column=5)
        self.botaonumz=Button(raiz,text="z",width=1)
        self.botaonumz.configure(font="Arial 10",background="black",foreground="white",command=self.letraz)
        self.botaonumz.grid(row=4,column=6)
        self.botaonumder=Button(raiz,text="d/t",width=1)
        self.botaonumder.configure(font="Arial 10",background="black",foreground="white",command=self.derivad)
        self.botaonumder.grid(row=4,column=7,rowspan=1)
        self.botaonumprin=Button(raiz,text="prin",width=1)
        self.botaonumprin.configure(font="Arial 8",background="black",foreground="white",command=self.princ)
        self.botaonumprin.grid(row=5,column=7,columnspan=1,rowspan=1)
        self.botaonumint=Button(raiz,text="lx")
        self.botaonumint.configure(font="Arial 9",background="black",foreground="white",command=self.int)
        self.botaonumint.grid(row=4,column=8)
        self.botaonumlimy=Button(raiz,text="l.y")
        self.botaonumlimy.configure(font="Arial 8",background="black",foreground="white",command=self.limy)
        self.botaonumlimy.grid(row=5,column=4)
        self.botaonumlimz=Button(raiz,text="lz")
        self.botaonumlimz.configure(font="Arial 8",background="black",foreground="white",command=self.limz)
        self.botaonumlimz.grid(row=5,column=5)
        self.botaonume=Button(raiz,text="e",width=1)
        self.botaonume.configure(font="Arial 11",background="black",foreground="white",command=self.lime)
        self.botaonume.grid(row=1,column=13,columnspan=2,rowspan=1)
        self.botaonumprv=Button(raiz,text="pv")
        self.botaonumprv.configure(font="Arial 8",background="black",foreground="white",command=self.prv)
        self.botaonumprv.grid(row=5,column=6,rowspan=1)
        self.botaonumans=Button(raiz,text="as")
        self.botaonumans.configure(font="Arial 8",background="black",foreground="white",command=self.ans)
        self.botaonumans.grid(row=4,column=9)
        self.botaonumsimp=Button(raiz,text="si")
        self.botaonumsimp.configure(font="Arial 8",background="black",foreground="white",command=self.simplis)
        self.botaonumsimp.grid(row=4,column=10)
        self.botaonumbi=Button(raiz,text="bi")
        self.botaonumbi.configure(font="Arial 8",background="black",foreground="white",command=self.binario)
        self.botaonumbi.grid(row=4,column=11)
        self.botaonumbb=Button(raiz,text="bd")
        self.botaonumbb.configure(font="Arial 8",background="black",foreground="white",command=self.decimal)
        self.botaonumbb.grid(row=4,column=12)
        self.botaonumhh=Button(raiz,text="hd")
        self.botaonumhh.configure(font="Arial 8",background="black",foreground="white",command=self.hexadecima)
        self.botaonumhh.grid(row=4,column=13)
    def princ(self):
        self.entra=self.enter
    def derivad(self):
        self.entra=self.enterdefineintegral
    def int(self):
        self.entra=self.enterlimite1
    def limy(self):
        self.entra=self.enterlimite2
    def limz(self):
        self.entra=self.enterlimite3
    def calcula(self):
        self.acalcula=1
        if self.aderiva==1:
            self.enter.grid_remove()
            self.labelintegral1.grid_remove()
            self.enterdefineintegral.grid_remove()
            self.botaointegral.grid_remove()
            self.aderiva=0
        elif self.aintegra==1:
            self.labelintegral.grid_remove()
            self.labelintegral.grid_remove()
            self.enterdefineintegral.grid_remove()
            self.enter.grid_remove()
            self.enterlimite1.grid_remove()
            self.enterlimite2.grid_remove()
            self.enterlimite3.grid_remove()
            self.labelimite1.grid_remove()
            self.labelimite2.grid_remove()
            self.labelimite3.grid_remove()
            self.botaointegral.grid_remove()
            self.aintegra=0
        if self.aresposta==1:
            self.labelresposta.grid_remove()
            self.labelresposta1.grid_remove()
            self.aresposta=0
        self.enter=Entry(raiz,text="digite a expressão para calcular",width=33)
        self.enter.configure(font="Arial 12",background="black",foreground="white")
        self.enter.grid(row=1,column=0,columnspan=3,rowspan=1)
        self.botaocalcula1=Button(raiz,text="clique para obter o resultado",command=self.calcula1,width=32)
        self.botaocalcula1.configure(font="Arial 12",background="black",foreground="white")
        self.botaocalcula1.grid(row=3,column=0,columnspan=3)
    def decimal(self):
        self.entra.insert(INSERT,"bd(")
    def hexadecima(self):
        self.entra.insert(INSERT,"hd(")
    def binario(self):
        self.entra.insert(INSERT,"bin(")
    def simplis(self):
        self.entra.insert(INSERT,"div.p(")
    def lime(self):
        self.entra.insert(INSERT,"e")
    def ans(self):
        self.entra.insert(INSERT,str(self.anss))
    def letra1(self):
        self.entra.insert(INSERT,"1")
    def letra2(self):
        self.entra.insert(INSERT,"2")
    def prv(self):
        self.entra.insert(INSERT,"prv(")
    def letra3(self):
        self.entra.insert(INSERT,"3")
    def letra4(self):
        self.entra.insert(INSERT,"4")
    def letra5(self):
        self.entra.insert(INSERT,"5")
    def letra6(self):
        self.entra.insert(INSERT,"6")
    def letra7(self):
        self.entra.insert(INSERT,"7")
    def letra8(self):
        self.entra.insert(INSERT,"8")
    def letra9(self):
        self.entra.insert(INSERT,"9")
    def letra0(self):
        self.entra.insert(INSERT,"0")
    def letramu(self):
        self.entra.insert(INSERT,"*")
    def letrama(self):
        self.entra.insert(INSERT,"+")
    def letrame(self):
        self.enter.insert(INSERT,"-")
    def letraba(self):
        self.entra.insert(INSERT,"/")
    def letraco(self):
        self.entra.insert(INSERT,"cos(")
    def letraln(self):
        self.entra.insert(INSERT,"ln(")
    def letralo(self):
        self.entra.insert(INSERT,"log(")
    def letraexp(self):
        self.entra.insert(INSERT,"expand(")
    def letrasi(self):
        self.entra.insert(INSERT,"sin(")
    def letradel(self):
        self.entra.delete(0,END)
    def letrainterpol(self):
        self.entra.insert(INSERT,"interpol(")
    def letradeter(self):
        self.entra.insert(INSERT,"det(")
    def letrapard(self):
        self.entra.insert(INSERT,"(")
    def letrapare(self):
        self.entra.insert(INSERT,")")
    def letrapt(self):
        self.entra.insert(INSERT,".")
    def letracold(self):
        self.entra.insert(INSERT,"[")
    def letracole(self):
        self.entra.insert(INSERT,"]")
    def letravir(self):
        self.entra.insert(INSERT,",")
    def letrax(self):
        self.entra.insert(INSERT,"x")
    def letray(self):
        self.entra.insert(INSERT,"y")
    def letraz(self):
        self.entra.insert(INSERT,"z")
    def derivada(self):
        self.aderiva=1
        if self.acalcula==1:
            self.enter.grid_remove()
            self.botaocalcula1.grid_remove()
            self.acalcula=0
        elif self.aintegra==1:
            self.labelintegral.grid_remove()
            self.labelintegral.grid_remove()
            self.enterdefineintegral.grid_remove()
            self.enter.grid_remove()
            self.enterlimite1.grid_remove()
            self.enterlimite2.grid_remove()
            self.enterlimite3.grid_remove()
            self.labelimite1.grid_remove()
            self.labelimite2.grid_remove()
            self.labelimite3.grid_remove()
            self.botaointegral.grid_remove()
            self.aintegra=0
        if self.aresposta==1:
            self.labelresposta.grid_remove()
            self.labelresposta1.grid_remove()
            self.aresposta=0
        self.labelintegral1=Label(raiz,text="digite quantas vezes voce deseja derivar",width=31)
        self.labelintegral1.configure(font="Arial 10",background="grey",foreground="black")
        self.labelintegral1.grid(row=1,column=0,columnspan=3,rowspan=1)
        self.enterdefineintegral=Entry(raiz,width=2)
        self.enterdefineintegral.configure(background="black",foreground="white")
        self.enterdefineintegral.grid(row=1,column=3)
        self.enter=Entry(raiz,text="",width=35)
        self.enter.configure(font="Arial 12",background="black",foreground="white")
        self.enter.grid(row=2,column=0,columnspan=4,rowspan=2)
        self.botaointegral=Button(raiz,text="derivar",command=self.derivada1)
        self.botaointegral.configure(font="Arial 10",background="black",foreground="white")
        self.botaointegral.grid(row=4,column=1,rowspan=1)
    def derivada1(self):
        self.aresposta=1
        b=self.enterdefineintegral.get()
        a=self.enter.get()
        a=eval(a)
        b=int(b)
        a=diff(a,x,b)
        self.labelresposta=Label(raiz,text=str(a))
        self.labelresposta.configure(font="Arial 12",background="grey",foreground="black")
        self.labelresposta.grid(row=5,column=0,columnspan=4)
        self.labelresposta1=Label(raiz,text="")
        self.labelresposta1.configure(font="Arial 12",background="grey")
        self.labelresposta1.grid(row=6,column=0)

    def calcula1(self):
        self.aresposta=1
        self.resposta=self.enter.get()
        b=""
        if self.resposta.count('prv')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a=graus.produtov(a)
            a=str(a)
            b=self.resposta[self.resposta.find('prv'):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('det')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a=graus.det(a)
            a=str(a)
            b=self.resposta[self.resposta.find('det'):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('hd(')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a= int(a,16)
            a=str(a)
            b=self.resposta[self.resposta.find('hd('):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('bd(')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a= int(a,2)
            a=str(a)
            b=self.resposta[self.resposta.find('bd('):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('bin(')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a=int(a)
            a=bin(a)
            a=str(a)
            b=self.resposta[self.resposta.find('bin('):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('interpol')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a=graus.interpol(a)
            a=str(a)
            b=self.resposta[self.resposta.find('interpol'):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('cos')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a=float(a)
            a=graus.grauscon(a)
            a=math.cos(a)
            a=round(a,6)
            a=str(a)
            b=self.resposta[self.resposta.find('cos'):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('div.p')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find('))')+1]
            a=eval(a)
            a=graus.simples(a)
            a=str(a)
            b=self.resposta[self.resposta.find('div.p'):self.resposta.find('))')+2]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('sin')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a=float(a)
            a=graus.grauscon(a)
            a=math.sin(a)
            a=round(a,6)
            a=str(a)
            b=self.resposta[self.resposta.find('sin'):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('log')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a=graus.log(a)
            a=round(a,6)
            a=str(a)
            b=self.resposta[self.resposta.find('log'):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('ln')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]

            a=graus.ln(a)
            a=round(a,6)
            a=str(a)
            b=self.resposta[self.resposta.find('ln'):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)

        if self.resposta.count('expand')>=1:
            a=self.resposta[self.resposta.find('((')+1:self.resposta.find('))')+1]
            a=graus.expi(a)
            a=str(a)
            b=self.resposta[self.resposta.find('expand'):self.resposta.find('))')+2]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('simpl')>=1:
            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            a=graus.simplificar(a)
            a=str(a)
            b=self.resposta[self.resposta.find('simpl'):self.resposta.find(')')+1]
            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('deriv')>=1:

            a=self.resposta[self.resposta.find('(')+1:self.resposta.find(')')]
            b=self.resposta[self.resposta.find('deriv'):self.resposta.find(')')+1]
            a=graus.derivada(a)
            a=str(a)

            self.resposta=self.resposta.replace(b,a)
        if self.resposta.count('e')>=1:
            self.resposta=self.resposta.replace('e','2.718281828459045235360287')
        if b.count('bin')!=1:
            self.resposta=eval(self.resposta)
        else:
            self.resposta=self.resposta
        self.anss=self.resposta
        self.labelresposta=Label(raiz,text=str(self.resposta))
        self.labelresposta.configure(font="Arial 12",background="grey",foreground="black")
        self.labelresposta.grid(row=4,column=0,columnspan=3)
        self.labelresposta1=Label(raiz,text="")
        self.labelresposta1.configure(font="Arial 12",background="grey")
        self.labelresposta1.grid(row=5,column=0)

    def integral(self):
        self.aintegra=1
        if self.acalcula==1:
            self.enter.grid_remove()
            self.botaocalcula1.grid_remove()
            self.acalcula=0
        elif self.aderiva==1:
            self.enter.grid_remove()
            self.labelintegral1.grid_remove()
            self.enterdefineintegral.grid_remove()
            self.botaointegral.grid_remove()
            self.aderiva=0
        if self.aresposta==1:
            self.labelresposta.grid_remove()
            self.labelresposta1.grid_remove()
            self.aresposta=0
        self.labelintegral=Label(raiz,text="digite a integral")
        self.labelintegral.configure(font="Arial 11",background="grey",foreground="black")
        self.labelintegral.grid(row=1,column=1)
        self.labelintegral1=Label(raiz,text="1-x,2-y,3-z")
        self.labelintegral1.configure(font="Arial 11",background="grey",foreground="black")
        self.labelintegral1.grid(row=3,column=1)
        self.labelimite1=Label(raiz,text="lim x")
        self.labelimite1.configure(font="Arial 10",background="grey",foreground="black")
        self.labelimite1.grid(row=6,column=0)
        self.enterlimite1=Entry(raiz,width=9)
        self.enterlimite1.configure(font="Arial 10",background="black",foreground="white")
        self.enterlimite1.grid(row=7,column=0)
        self.labelimite2=Label(raiz,text="lim y")
        self.labelimite2.configure(font="Arial 10",background="grey",foreground="black")
        self.labelimite2.grid(row=6,column=1)
        self.enterlimite2=Entry(raiz,width=9)
        self.enterlimite2.configure(font="Arial 10",background="black",foreground="white")
        self.enterlimite2.grid(row=7,column=1)
        self.labelimite3=Label(raiz,text="lim z")
        self.labelimite3.configure(font="Arial 10",background="grey",foreground="black")
        self.labelimite3.grid(row=6,column=2)
        self.enterlimite3=Entry(raiz,width=9)
        self.enterlimite3.configure(font="Arial 10",background="black",foreground="white")
        self.enterlimite3.grid(row=7,column=2)
        self.enterdefineintegral=Entry(raiz,width=3)
        self.enterdefineintegral.configure(background="black",foreground="white")
        self.enterdefineintegral.grid(row=3,column=2)
        self.enter=Entry(raiz,text="",width=34)
        self.enter.configure(font="Arial 12",background="black",foreground="white")
        self.enter.grid(row=4,column=0,columnspan=3)
        self.botaointegral=Button(raiz,text="integrar",command=self.integral1)
        self.botaointegral.configure(font="Arial 12",background="black",foreground="white")
        self.botaointegral.grid(row=5,column=1,columnspan=1)
    def integral1(self):
        self.aresposta=1
        self.direciona=self.enterdefineintegral.get()
        if self.direciona=='1':
            limite=self.enterlimite1.get()
            limite=limite.split(',')
            a=limite[0]
            a=eval(a)
            b=limite[1]
            b=eval(b)

            self.calculaintegral=self.enter.get()
            self.calculaintegral=eval(self.calculaintegral)
            self.aa=integrate(self.calculaintegral,(x,a,b))
            self.a=integrate(self.calculaintegral,x)
            self.labelresposta=Label(raiz,text=str(self.a))
            self.labelresposta.configure(font="Arial 12",background="grey",foreground="black")
            self.labelresposta.grid(row=8,column=0,columnspan=3)
            self.labelresposta1=Label(raiz,text=str(self.aa))
            self.labelresposta1.configure(font="Arial 12",background="grey",foreground="black")
            self.labelresposta1.grid(row=9,column=0)
        elif self.direciona=='2':
            limite=self.enterlimite1.get()
            limite=limite.split(',')
            a=limite[0]
            a=eval(a)
            b=limite[1]
            b=eval(b)
            limite=self.enterlimite2.get()
            limite=limite.split(',')
            c=limite[0]
            c=eval(c)
            d=limite[1]
            d=eval(d)
            self.calculaintegral=self.enter.get()
            self.calculaintegral=eval(self.calculaintegral)
            self.a=integrate(self.calculaintegral,x,y)
            self.aa=integrate(self.calculaintegral,(x,a,b),(y,c,d))
            self.labelresposta=Label(raiz,text=str(self.a))
            self.labelresposta.configure(font="Arial 12",background="grey",foreground="black")
            self.labelresposta.grid(row=8,column=0,columnspan=3)
            self.labelresposta1=Label(raiz,text=str(self.aa))
            self.labelresposta1.configure(font="Arial 12",background="grey",foreground="black")
            self.labelresposta1.grid(row=9,column=0,columnspan=3)
        elif self.direciona=='3':
            limite=self.enterlimite1.get()
            limite=limite.split(',')
            a=limite[0]
            a=eval(a)
            b=limite[1]
            b=eval(b)
            limite=self.enterlimite2.get()
            limite=limite.split(',')
            c=limite[0]
            c=eval(c)
            d=limite[1]
            d=eval(d)
            limite=self.enterlimite3.get()
            limite=limite.split(',')
            e=limite[0]
            e=eval(e)
            f=limite[1]
            f=eval(f)
            self.calculaintegral=self.enter.get()
            self.calculaintegral=eval(self.calculaintegral)
            self.a=integrate(self.calculaintegral,x,y,z)
            self.aa=integrate(self.calculaintegral,(x,a,b),(y,c,d),(z,e,f))
            self.ab=integrate(self.calculaintegral,(x,a,b),(y,c,d),(z))
            self.ac=str(self.aa)+'//'+ str(self.ab)
            self.labelresposta=Label(raiz,text=str(self.a))
            self.labelresposta.configure(font="Arial 12",background="grey",foreground="black")
            self.labelresposta.grid(row=8,column=0,columnspan=3)
            self.labelresposta1=Label(raiz,text=self.ac)
            self.labelresposta1.configure(font="Arial 12",background="grey",foreground="black")
            self.labelresposta1.grid(row=9,column=0)
raiz=Tk()
raiz.geometry("505x260+200+50")
raiz["background"]="grey"
janela(raiz)

raiz.mainloop()
