from pywebio.input import *
from pywebio.output import *


def exam():
    c=0

    
    name= input("enter your name to start the exam",type="text")
    pa=input("enter hallticket:",type="password")
    if ("21kh1a6" in pa)or ("21KH1A6" in pa):
        a=open("p1.txt","r")
        q1=radio(a.readline(),[str(a.readline()).strip(),str(a.readline()),str(a.readline()).strip(),str(a.readline())])
        if q1=="list":
            c+=1


        q2=radio(a.readline(),[str(a.readline()).strip(),str(a.readline()).strip(),str(a.readline()).strip(),str(a.readline()).strip()])
        if q2=="html":
            c+=1


        q3=radio(a.readline(),[str(a.readline()).strip(),str(a.readline()).strip(),str(a.readline()).strip(),str(a.readline()).strip()])
        if q3=="ROM":
            c+=1

        q4=radio(a.readline(),[str(a.readline()).strip(),str(a.readline()).strip()])
        if q4=="YES":
            c+=1


        q5=radio(a.readline(),[str(a.readline()).strip(),str(a.readline()).strip(),str(a.readline()).strip(),str(a.readline()).strip()])
        if q5=="JAVASCRIPT":
            c+=1



    #CHECKS FOR PASS / FAIL
    if c>3:
        put_text(name+" , your score is "+str(c))
        style(put_text("Results: passed"),"color:green")
    else:
        put_text(name+" , your score is "+str(c))
        style(put_text("Results: failed"),"color:red")

    put_text("thank you for participation")
exam()

        

