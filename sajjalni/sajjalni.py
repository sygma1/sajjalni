from PyQt5 import QtWidgets, uic 
from PyQt5.QtWidgets import QMessageBox

def sais():
    num=u.number.text()
    if(len(num)<8 and len(num)>8):
        msgBox = QMessageBox()
        msgBox.setText("pas un nombre")
        msgBox.exec_()
    else:
        notlngth=0
        lngth1=0
        f = open("numbers.txt", "r")
        for x in f:
            linee = x.strip()
            lngth1=lngth1+1
            if (num == linee) :
                E = open("state.txt", "r")
                a=0
                for i in E:
                    linee2 = i.strip()
                    a=a+1
                    if (a == lngth1):
                        statee = linee2
                        break
                E.close()
                msgBox = QMessageBox()
                msgBox.setText("le nombre deja existe et il est ",statee)
                msgBox.exec_()
                break
            else:
                notlngth=notlngth+1
        f.close
        if (lngth1 == notlngth):
            msgBox = QMessageBox()
            msgBox.setText("le nombre n'existe pas")
            msgBox.exec_()
#---------------------------------------------------------
def plus():
    num= u.number.text()
    imei= u.IMEI.text()
    if((len(num)<8 and len(num)>8) and(len(imei)<15 or len(imei)>15)):
        msgBox1 = QMessageBox()
        msgBox1.setText("pas bon")
        msgBox1.exec_() 
    else:
        f = open("numbers.txt", "r")
        lngth2=0
        notlngth=0
        for x in f:
            linee = x.strip()
            lngth2=lngth2+1
            if (num == linee) :
                msgBox = QMessageBox()
                msgBox.setText("le nombre deja existe")
                msgBox.exec_()
                break
            else:
                notlngth=notlngth+1
        f.close()
        if (lngth2 == notlngth):
            f = open("numbers.txt", "a")
            f.write(num)
            f.close
            f = open("IMEI.txt", "a")
            f.write(imei)
            f.close
            f = open("state.txt", "a")
            f.write("true")
            f.close 
#---------------------------------------------
def blok():
    imei= u.IMEI.text()
    imei= imei+"0"
    L1=[]
    L2=[]
    L3=[]
    L4=[]
    for i in range(16):
        if i <=4:
            L1.append(imei[i])
        if i <=8 and i>4 :
            L2.append(imei[i])
        if i <=12 and i>8:
            L3.append(imei[i])
        if i >12:
            L4.append(imei[i])
    p1=int(L1[0])+int(L1[3])
    p2=int(L2[1])+int(L2[2])
    p3=int(L3[2])+int(L3[1])
    p4=int(L4[3])+int(L4[0])
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cont=0
    for i in abc:
        cont=cont+1
        if (cont==p1):
            code=i
        if (cont==p2):
            code=code+i
        if (cont==p3):
            code=code+i
        if (cont==p4):
            code=code+i
    num= u.number.text()
    f = open("numbers.txt", "r")
    lngth3=0
    for x in f:
        linee = x.strip()
        lngth3=lngth3+1
        if (num == linee[0,8]) :
            break
    msgBox = QMessageBox()
    msgBox.setText(code)
    msgBox.exec_()
    bar= u.codebar.text()
    if(bar == code):
        f = open("state.txt" ,"r")
        liste=[]
        for i in f :
            linee = i.strip()
            liste.append(linee)
        f.close()
        liste[lngth3]="false"
        f = open("state.txt" ,"w")
        for i in liste:
            f.write(i)
        f.close()
    else:
        msgBox = QMessageBox()
        msgBox.setText("wrong")
        msgBox.exec_()
    





            
                


app = QtWidgets.QApplication([])
u=uic.loadUi("sajjalni.ui")
u.show()
u.verifier.clicked.connect(sais)
u.add.clicked.connect(plus)
u.block.clicked.connect(blok)
app.exec_()
