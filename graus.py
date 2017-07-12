#coding:UTF-8
from sympy import*
x,y,z=symbols('x y z')
import math
import numpy as np
def grauscon(angulo):
    
    angulo =(angulo*3.1416)/180
    return angulo
def log(logaritmo):
    logaritmo= logaritmo.split(',')
    logaritmo[0]=float(logaritmo[0])
    logaritmo[1]=float(logaritmo[1])
    logaritmo=math.log(logaritmo[0],logaritmo[1])
    return logaritmo
def ln(logn):
    logn=float(logn)
    loga=np.log(logn)
    return loga
def simples(simplif):
    simplif= apart(simplif)
    return simplif
def produtov(deter):
    i=0
    a=[]
    b=[]
    c=[]
    deter=deter.split('],[')
    deter[0]= deter[0].replace('[','')
    deter[2]=deter[2].replace(']','')
    a=deter[0].split(',')
    b=deter[1].split(',')
    c=deter[2].split(',')
    for i in range(len(b)):
        b[i]= float(b[i])
        i=i+1
    for i in range(len(c)):
        c[i]= float(c[i])
        i=i+1
    d=x*b[1]*c[2]+y*b[2]*c[0] +z*b[0]*c[1]-z*b[1]*c[0]-x*b[2]*c[1]-y*b[0]*c[2]
    return d
def det(deter):
    i=0
    a=[]
    b=[]
    c=[]
    d=[]
    if deter.count(']')==4:
        deter=deter.split('],[')
        deter[0]= deter[0].replace('[','')
        deter[2]=deter[2].replace(']','')
        a=deter[0].split(',')
        b=deter[1].split(',')
        c=deter[2].split(',')
        d=deter[3].split(',')
        for i in range(len(b)):
            b[i]= float(b[i])
            i=i+1
        for i in range(len(a)):
            a[i]=float(a[i])
            i=i+1
        for i in range(len(c)):
            c[i]= float(c[i])
            i=i+1
        for i in range(len(d)):
            c[i]= float(c[i])
            i=i+1
        resposta=np.array([a,b,c,d])
        resposta=np.linalg.det(resposta)
        return resposta
    if deter.count(']')==3:
        deter=deter.split('],[')
        deter[0]= deter[0].replace('[','')
        deter[2]=deter[2].replace(']','')
        a=deter[0].split(',')
        b=deter[1].split(',')
        c=deter[2].split(',')
        for i in range(len(b)):
            b[i]= float(b[i])
            i=i+1
        for i in range(len(a)):
            a[i]=float(a[i])
            i=i+1
        for i in range(len(c)):
            c[i]= float(c[i])
            i=i+1
        resposta=np.array([a,b,c])
        resposta=np.linalg.det(resposta)
        return resposta
    elif deter.count(']')<=2:
        deter=deter.split('],[')
        deter[0]= deter[0].replace('[','')
        deter[1]=deter[1].replace(']','')
        a=deter[0].split(',')
        b=deter[1].split(',')
        for i in range(len(b)):
            b[i]= float(b[i])
            i=i+1
        for i in range(len(a)):
            a[i]=float(a[i])
            i=i+1
        resposta=np.array([a,b])
        resposta=np.linalg.det(resposta)
        return resposta
def expi(exp):
    
    exp=eval(exp)
    exp=expand(exp)
    return exp
def simplificar(simp):
    simp=simplify(simp)
    return simp
def derivada(deriv):
    deriv=eval(deriv)
    deriv=diff(deriv,x)
    return deriv
def interpol(inter):
    d=0
    i=0
    
    
    a=inter[0]
    if a=='3':
        i=0
        inter=inter[inter.find('/')+1:len(inter)]
        inter=inter.split(',')
        for i in range(len(inter)):
             inter[i]=float(inter[i])
             i=i+1
        inter=interpolate([(inter[0],inter[1]), (inter[2], inter[3]),(inter[4],inter[5])], x)
        return( inter)
    elif a=='4':
        i=0
        inter=inter[inter.find('/')+1:len(inter)]
        inter=inter.split(',')
        for i in range(len(inter)):
             inter[i]=float(inter[i])
             inter[i]=round(inter[i],3)
             i=i+1
        inter=interpolate([(inter[0],inter[1]), (inter[2], inter[3]),(inter[4],inter[5]),(inter[6],inter[7])], x)
        return( inter)
    elif a=='5':
        i=0
        inter=inter[inter.find('/')+1:len(inter)]
        inter=inter.split(',')
        for i in range(len(inter)):
             inter[i]=float(inter[i])
             inter[i]=round(inter[i],3)
             i=i+1
        inter=interpolate([(inter[0],inter[1]), (inter[2], inter[3]),(inter[4],inter[5]),(inter[6],inter[7]),(inter[8],inter[9])], x)
        return( inter)
    
        
        
    
