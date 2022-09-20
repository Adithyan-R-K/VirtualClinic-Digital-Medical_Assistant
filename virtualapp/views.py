from django.shortcuts import render
import mysql.connector
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def index(request):
    return render(request,'virtualapp/index.html')
def index1(request):
    return render(request,'virtualapp/index-1.html')
def alogin(request):
    return render(request,'virtualapp/admin_login.html')
def drlogin(request):
    return render(request,'virtualapp/dr_login.html')
def plogin(request):
    return render(request,'virtualapp/patient_login.html')
def llogin(request):
    return render(request,'virtualapp/lab_login.html')
def clogin(request):
    return render(request,'virtualapp/chemist_login.html')
def manage_doctor(request):
    return render(request,'virtualapp/admindoctor.html')
def manage_disease(request):
    return render(request,'virtualapp/adminpannel/dislist.html')
def adddoc(request):
    return render(request,'virtualapp/ADDDOCTOR.html')
def adddis(request):
    return render(request,'virtualapp/adddisease.html')
def addpat(request):
    return render(request,'virtualapp/patient_register.html')
def addchem(request):
    return render(request,'virtualapp/add chemist.html')
def manage_patient(request):
    return render(request,'virtualapp/adminpaitent.html')
def manage_lab(request):
    return render(request,'virtualapp/adminlab.html')
def manage_chemist(request):
    return render(request,'virtualapp/admin pannel.html')
def searchid(request):
    return render(request,'virtualapp/search.html')
#def doctorhome(request):
   # return render(request,'virtualapp/home/doctorhome.html')
def adminshome(request):
    return render(request,'virtualapp/home/adminhome.html')
def labhome(request):
    return render(request,'virtualapp/home/labhome.html')
def doclist(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `id`, `name`, `gender`, `qualification`, `phone`, `joiningdate`, `timing`, `email`, `address`, `dob` FROM `tbl_doctor` WHERE 1 "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/doctor1.html',{'mess':'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request,'virtualapp/adminpannel/doctlist.html',{'records':records})

def dislist(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `diseasename`, `symptom1`, `symptom2`, `symptom3`, `diseaseid`FROM `adddisease` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/doctor1.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/adminpannel/dislist.html', {'records': records})

def patientlist(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `name`, `emailid`, `phone`, `dob`, `password` FROM `addpaitent` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/doctor1.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/adminpannel/patientlist.html', {'records': records})

def lablist(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `name`, `email`, `password`, `img` FROM `addlab` WHERE 1 "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/home/adminhome.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/adminpannel/lablist.html', {'records': records})

def chemlist(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `name`, `emailid`, `password`, `img`, `phone` FROM `addchemist` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/doctor1.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/adminpannel/chemlist.html', {'records': records})
def fedback(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT  `name`, `message`FROM `feedback` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/viewfeedbacks.html', {'mess': 'No feedbacks found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/viewfeedbacks.html', {'records': records})


def sendfeed(request):
    if request.method == "POST":
       # id = request.POST["id"]
        name = request.POST["feedbackform"]
        mess = request.POST["feedbackmessage"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "INSERT INTO `feedback`( `name`, `message`) VALUES ('"+name+"','"+mess+"')"
        mycursor.execute(q)
        conn.commit()
    return render(request,'virtualapp/SENDFEEDBACK.html')
def chatbot(request):
    return render(request,'virtualapp/chatbot.html')
def docabout(request):
    return render(request,'virtualapp/adminpannel/aboutdoc.html')
def uploadtest(request):
    return render(request,'virtualapp/UPLOADMEDICAL.html')
def addreport(request):
    if request.method == "POST":
        r1 = request.POST["r1"]
        r2 = request.POST["r2"]
        r3 = request.POST["r3"]
        r4 = request.POST["r4"]
        r5 = request.POST["r5"]
        r6 = request.POST["r6"]
        r7 = request.POST["r7"]
        r8 = request.POST["r8"]
        r9 = request.POST["r9"]
        r10 = request.POST["r10"]

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "INSERT INTO `report`(`r1`, `r2`, `r3`, `r4`, `r5`, `r6`, `r7`, `r8`, `r9`, `r10`) VALUES ('"+r1+"','"+r2+"','"+r3+"','"+r4+"','"+r5+"','"+r6+"','"+r7+"','"+r8+"','"+r9+"','"+r10+"')"
        mycursor.execute(q)
        conn.commit()
    return render(request,'virtualapp/reportadd.html')

def adminlogin(request):
    uname=request.POST["email"]
    pas=request.POST["password"]
    print(uname + pas)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor=conn.cursor()
    utype="Admin"
    query="select*from tbl_login where username='" + uname + "' and password='" + pas + "' and utype='"+utype+"'  "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request,'virtualapp/admin_login.html',{'mes':'invalid username and password'})
    else:
        return render(request,'virtualapp/home/adminhome.html')

def dr_login(request):
        uname = request.POST["email"]
        pas = request.POST["password"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        query = "select * from tbl_doctor where email='" + uname + "' and password='" + pas + "' "
        mycursor.execute(query)
        mycursor.fetchall()
        print(mycursor.rowcount)
        if mycursor.rowcount == 0:
            return render(request, 'virtualapp/dr_login.html', {'mes': 'invalid username and password'})
        else:
            query1 = "select name from tbl_doctor where email='" + uname + "' and password='" + pas + "' "
            mycursor.execute(query1)
            ((i,),) = mycursor.fetchall()
            print(i)
            request.session['email'] = uname
            request.session['name'] = i
            return render(request, 'virtualapp/home/doctorhome.html',{'name':i})

def patient_login(request):
    uname=request.POST["pnam"]
    pas=request.POST["password"]
    print(uname + pas)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor=conn.cursor()
    query = "select * from addpaitent where emailid='" + uname + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request,'virtualapp/patient_login.html',{'mes':'invalid username and password'})
    else:
        return render(request,'virtualapp/home/paitenthome.html')

def searchdisease(request):
    return render(request, 'virtualapp/DOCTORLIST.html')
def showdoc(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `id`, `name`, `gender`, `qualification`, `phone`, `joiningdate`, `timing`, `email`, `address`, `dob` FROM `tbl_doctor` WHERE 1 "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/doctor1.html',{'mess':'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/admin/doctor1.html',{'records':records})
def showp(request):
    if request.method == "POST":
        pp = request.POST["p"]
        m11 = request.POST["m1"]
        m22 = request.POST["m2"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = " INSERT INTO `addprescription` VALUES ('"+pp+"','"+m11+"','"+m22+"')"
        mycursor.execute(q)
        conn.commit()
    return render(request, 'virtualapp/padd.html')
#hey rk look here
#page edited ,database edited
def addappointment(request):
    if request.method == "POST":
        name = request.POST["patient-id"]
        dep = request.POST["department"]
        dname = request.POST["doctor-name"]
        adate = request.POST["appointment-date"]
        timeslot = request.POST["time-slot"]
        problem = request.POST["problem"]
        a = request.POST["1"]
        m = request.POST["2"]
        p = request.POST["3"]
        e = request.POST["4"]
        r = request.POST["5"]
        t = request.POST["6"]
        tt = "pending"

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "INSERT INTO `addappoinment`(`paitentname`, `department`, `doctorname`, `appoinmentdate`, `time`, `problem`,`cost`,`type`, `cvv`, `edate`, `cardno`, `paytime`,`pin`,`status`) VALUES ('"+name+"','"+dep+"','"+dname+"','"+adate+"','"+timeslot+"','"+problem+"','"+a+"','"+m+"','"+e+"','"+r+"', AES_ENCRYPT('"+p+"', '123'), CURRENT_DATE(), AES_ENCRYPT('"+t+"', '123'),'"+tt+"')"
        mycursor.execute(q)
        conn.commit()
    return render(request, 'virtualapp/admin/add-appointment.html')

def feedback(request):
    return render(request, 'virtualapp/feedback.html')
#hey rk look
#page edited
def showappointment(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `Aid`,`doctorname`, `problem`, `appoinmentdate`, `time`,`status` FROM `addappoinment` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/appointments.html', {'mess': 'No Appointments found'})
    else:
        records = mycursor.fetchall()
    return render(request, 'virtualapp/admin/appointments.html', {'records': records})
def docapprove(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    drname=request.session["name"]
    query = "SELECT `Aid`,`paitentname`, `problem`, `appoinmentdate`, `time` FROM `addappoinment` where doctorname='"+drname+"' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/appointments.html', {'mess': 'No Appointments found'})
    else:
        records = mycursor.fetchall()
    return render(request, 'virtualapp/admin/appointmentsdoc.html', {'records': records})
def docA(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    id = request.POST["did"]
    s = "Accepted"
    s1 = "Rejected"

    if request.method == 'POST':
        if request.POST.get("a"):
            query = "update addappoinment set status='" + s + "' where Aid =" + id + " "
            mycursor.execute(query)
            conn.commit()
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "SELECT `Aid`,`paitentname`, `problem`, `appoinmentdate`, `time` FROM `addappoinment` "
            mycursor.execute(query)
            if mycursor.rowcount == 0:
                return render(request, 'virtualapp/admin/appointments.html', {'mess': 'No Appointments found'})
            else:
                records = mycursor.fetchall()
            return render(request, 'virtualapp/admin/appointmentsdoc.html', {'records': records})
        elif request.POST.get("r"):
            query = "update addappoinment set status='" + s1 + "' where Aid =" + id + " "
            mycursor.execute(query)
            conn.commit()
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "SELECT `Aid`,`paitentname`, `problem`, `appoinmentdate`, `time` FROM `addappoinment` "
            mycursor.execute(query)
            if mycursor.rowcount == 0:
                return render(request, 'virtualapp/admin/appointments.html', {'mess': 'No Appointments found'})
            else:
                records = mycursor.fetchall()
            return render(request, 'virtualapp/admin/appointmentsdoc.html', {'records': records})

###rk lok
def delA(request):
    v = request.POST["id"]
    print(v)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "DELETE FROM `addappoinment` WHERE Aid = "+v+" "
    mycursor.execute(query)
    conn.commit()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `Aid`,`doctorname`, `problem`, `appoinmentdate`, `time`,`status` FROM `addappoinment` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/appointments.html', {'mess': 'No Appointments found'})
    else:
        records = mycursor.fetchall()
    return render(request, 'virtualapp/admin/appointments.html', {'records': records})
def homep(request):
    return render(request, 'virtualapp/home/paitenthome.html')
def addpay(request):
    return render(request, 'virtualapp/admin/add-payment.html')


#heyrk look
#page edited
def payp(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `paitentname`, `cost`, `paytime`, `time` FROM `addappoinment` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/doctor1.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
    return render(request, 'virtualapp/admin/payments.html',{'records':records})
#here rk look
#page paymentsp edited
def showpay(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `doctorname`, `cost`, `paytime`, `type` FROM `addappoinment` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/doctor1.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
    return render(request, 'virtualapp/admin/paymentsp.html',{'records': records})
def chat(request):
    return render(request, 'virtualapp/chatchat.html')
def patientlist(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `name`, `emailid`, `phone`, `dob` FROM `addpaitent` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/doctor1.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/adminpannel/patientlist.html', {'records': records})

def chatread(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `to`, `subject`, `message`, `date` FROM `chat` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/doctor1.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/email-read.html', {'records': records})

def addmed(request):
    if request.method == "POST":
        medimg = request.POST["medimg"]
        medname = request.POST["medname"]
        medf = request.POST["medf"]
        mede = request.POST["mede"]
        medno = request.POST["medno"]
        medc = request.POST["medcost"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "INSERT INTO `medstock`(`medid`, `medname`, `medfa`,`medex`,`medno`,`medcost`) VALUES ('" +medimg + "','"+medname+"','"+mede+"','" + medf+ "','"+medno+"','"+medc+"')"
        mycursor.execute(q)
        conn.commit()
    return render(request, 'virtualapp/admin/add-room.html')

def medstock(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT medid,medname,medno,medcost,medfa,medex FROM medstock "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/add-room.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/admin/medstocklist.html', {'records': records})
    return render(request, 'virtualapp/admin/medstocklist.html')
def pres(request):
    return render(request, 'virtualapp/prescription.html')
def updatestock(request):
    return render(request, 'virtualapp/admin/updatestockmed.html')
def updatestock1(request):
    if request.method == "POST":
        medid = request.POST["medid"]
        medstock = request.POST["medstock"]
        medcost = request.POST["medcost"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q ="select medno from medstock where medid='"+medid+"'"
        mycursor.execute(q)
        ((qty,),)=mycursor.fetchall()
        inqty= int(qty)
        instock=int(medstock)
        finalstock=instock+inqty
        finalstock1=str(finalstock)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "UPDATE `medstock` SET `medno`= '"+finalstock1+"' ,`medcost`='"+medcost+"' WHERE medid= '"+medid+"' "
        mycursor.execute(q)
        conn.commit()
    return render(request, 'virtualapp/admin/updatestockmed.html')
def delmed(request):
    v = request.POST["medname"]
    print(v)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "DELETE FROM `medstock` WHERE medid = "+v+" "
    mycursor.execute(query)
    conn.commit()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT medid,medname,medno,medcost,medfa,medex FROM medstock "
    mycursor.execute(query)
    records = mycursor.fetchall()
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/admin/medstocklist.html', {'mess': 'No doctors found'})
    else:
        return render(request, 'virtualapp/admin/medstocklist.html', {'records': records})


def chatview(request):
    return render(request, 'virtualapp/viewchat.html')
def pred(request):
    return render(request, 'virtualapp/PREDICTION.html')
def chemisthome(request):
    return render(request, 'virtualapp/home/chemisthome.html')
def cart(request):
    return render(request, 'virtualapp/chemist/cart.html')
def check(request):
    return render(request, 'virtualapp/chemist/checkout.html')
def checkship(request):
    return render(request, 'virtualapp/chemist/checkout-shipping.html')
def checkpay(request):
    return render(request, 'virtualapp/chemist/checkout-payment.html')








def lab_login(request):
    uname=request.POST["email"]
    pas=request.POST["password"]
    print(uname + pas)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor=conn.cursor()
    query="select*from lab where username='" + uname + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request,'virtualapp/admin_login.html',{'mes':'invalid username and password'})
    else:
        return render(request,'virtualapp/home/adminhome.html')
def chemist_login(request):
    uname=request.POST["email"]
    pas=request.POST["password"]
    print(uname + pas)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor=conn.cursor()
    query="select*from chemist where username='" + uname + "' and password='" + pas + "' "
    mycursor.execute(query)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        return render(request,'virtualapp/admin_login.html',{'mes':'invalid username and password'})
    else:
        return render(request,'virtualapp/home/adminhome.html')
def reg_doctor(request):
    if request.method == "POST":
        #id = request.POST["id"]
        name = request.POST["docname"]
        gender = request.POST["gender"]
        qualification = request.POST["quali"]
        phone = request.POST["phoneno"]
        joiningdate = request.POST["join"]
        timing = request.POST["time1"]
        email = request.POST["email"]
        address = request.POST["address"]
        dob = request.POST["dob"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "INSERT INTO `tbl_doctor`(`name`, `gender`, `qualification`, `phone`, `joiningdate`, `timing`, `email`, `address`, `dob`) VALUES ('"+name+"','"+gender+"','"+qualification+"',"+phone+",'"+joiningdate+"','"+timing+"','"+email+"','"+address+"','"+dob+"')"
        mycursor.execute(q)
        conn.commit()
        conn.commit()
    return render(request,'virtualapp/ADDDOCTOR.html',{'mes':'Doctor added Succesfully'})
def editdoc(request):
    if request.method == 'POST':
        if request.POST.get('edit'):
            id = request.POST["docid"]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "SELECT `id`, `name`, `gender`, `qualification`, `phone`, `joiningdate`, `timing`, `email`, `address`, `dob` FROM `tbl_doctor` WHERE id = '"+id+"' "
            mycursor.execute(query)
            if mycursor.rowcount == 0:
                return render(request, 'virtualapp/admin/doctlist.html', {'mess': 'No doctors found'})
            else:
                records = mycursor.fetchall()
                return render(request, 'virtualapp/addoctor12.html', {'records': records})
        elif request.POST.get('delete'):
            id = request.POST["docid"]
            print(id)
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "DELETE FROM `tbl_doctor` WHERE id="+id+" "
            mycursor.execute(query)
            conn.commit()
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "SELECT `id`, `name`, `gender`, `qualification`, `phone`, `joiningdate`, `timing`, `email`, `address`, `dob` FROM `tbl_doctor` WHERE 1 "
            mycursor.execute(query)
            records = mycursor.fetchall()
            return render(request, 'vvirtualapp/adminpannel/doctlist.html', {'records': records})

def updatedoctor(request):
        if request.method == "POST":
            id=request.POST["did"]
            name = request.POST["docname"]
            qualification = request.POST["quali"]
            phone = request.POST["phoneno"]
            joiningdate = request.POST["join"]
            timing = request.POST["time1"]
            email = request.POST["email"]
            address = request.POST["address"]
            dob = request.POST["dob"]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            q = "UPDATE `tbl_doctor` SET `name`='"+name+"',`qualification`='"+qualification+"',`phone`='"+phone+"',`joiningdate`='"+joiningdate+"',`timing`='"+timing+"',`email`='"+email+"',`address`='"+address+"',`dob`='"+dob+"' WHERE id="+id+" "
            mycursor.execute(q)
            conn.commit()
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "SELECT `id`, `name`, `gender`, `qualification`, `phone`, `joiningdate`, `timing`, `email`, `address`, `dob` FROM `tbl_doctor` WHERE 1 "
            mycursor.execute(query)
            if mycursor.rowcount == 0:
                return render(request, 'virtualapp/admin/doctor1.html', {'mess': 'No doctors found'})
            else:
                records = mycursor.fetchall()
                return render(request, 'virtualapp/adminpannel/doctlist.html', {'records': records})
        return render(request,'virtualapp/adminpannel/doctlist.html',{'mes':'Doctor added Succesfully'})


def editdis(request):
    if request.method == 'POST':
        if request.POST.get('edit'):
            disid = request.POST["disid"]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "SELECT `diseasename`, `symptom1`, `symptom2`, `symptom3` FROM `adddisease` WHERE  diseaseid = '+disid+' "
            mycursor.execute(query)
            if mycursor.rowcount == 0:
                return render(request, 'virtualapp/admin/dislist.html', {'mess': 'No disease found'})
            else:
                records = mycursor.fetchall()
                return render(request, 'virtualapp/edit/editdisease.html', {'records': records})
        elif request.POST.get('delete'):
            disid = request.POST["disid"]
            print(id)
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "DELETE FROM `adddisease` WHERE diseaseid ="+disid+" "
            mycursor.execute(query)
            conn.commit()
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "SELECT `diseasename`, `symptom1`, `symptom2`, `symptom3`, `diseaseid`FROM `adddisease` WHERE 1"
            mycursor.execute(query)
            records = mycursor.fetchall()
            return render(request, 'virtualapp/adminpannel/dislist.html', {'records': records})
def editpatient(request):
    if request.method == 'POST':
        if request.POST.get('edit'):
            phone = request.POST["pno"]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "SELECT `name`, `emailid`, `phone`, `dob` FROM `addpaitent` WHERE  phone = '+phone+' "
            mycursor.execute(query)
            if mycursor.rowcount == 0:
                return render(request, 'virtualapp/admin/patientlist.html', {'mess': 'No users  found'})
            else:
                records = mycursor.fetchall()
                return render(request, 'virtualapp/edit/editpatient.html', {'records': records})
        elif request.POST.get('delete'):
            phone = request.POST["pno"]
            print(id)
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "DELETE FROM `addpaitent` WHERE phone = '+phone+' "
            mycursor.execute(query)
            conn.commit()
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
            mycursor = conn.cursor()
            query = "SELECT `name`, `emailid`, `phone`, `dob` FROM `addpaitent` WHERE 1"
            mycursor.execute(query)
            records = mycursor.fetchall()
            return render(request, 'virtualapp/adminpannel/patientlist.html', {'records': records})


def  reg_patient(request):
    if request.method == "POST":
        name = request.POST["name"]
        emailid = request.POST["email"]
        phone = request.POST["phone"]
        dob = request.POST["date"]
        password = request.POST["password"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "INSERT INTO `addpaitent`(`name`, `emailid`, `phone`, `dob`, `password`) VALUES ('"+name+"','"+emailid+"','"+phone+"','"+dob+"','"+password+"')"
        mycursor.execute(q)
        conn.commit()
    return render(request, 'virtualapp/patient_register.html', {'mes': 'Patient added Succesfully'})
def reg_lab(request):
    if request.method == "POST":
        name = request.POST["firstname"]
        email = request.POST["email"]
        password = request.POST["password"]
        img = request.POST["img"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "insert into 'addlab' values('" + name + "', '" + email + "', '" + password + "', '" + img + "')"
        mycursor.execute(q)
        conn.commit()
    return render(request, 'virtualapp/add_lab.html', {'mes': 'Doctor added Succesfully'})


def reg_disease(request):
    if request.method == "POST":
        diseasename = request.POST["first_name"]
        diseaseid = request.POST["iddis"]
        symptom1 = request.POST["sym1"]
        symptom2 = request.POST["sym2"]
        symptom3 = request.POST["sym3"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "INSERT INTO `adddisease`(`diseasename`, `symptom1`, `symptom2`, `symptom3`, `diseaseid`)VALUES('"+diseasename+"','"+symptom1+"','"+symptom2+"','"+symptom3+"','"+diseaseid+"')"
        mycursor.execute(q)
        conn.commit()
    return render(request, 'virtualapp/adddisease.html', {'mes': 'Disease added Succesfully'})
def reg_chemist(request):
    if request.method == "POST":
        name = request.POST["firstname"]
        emailid = request.POST["email"]
        password = request.POST["password"]
        img = request.POST["img"]
        phone= request.POST["phone"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "insert into `addchemist` (`name`, `emailid`,`password`, `img`,`phone`) values ('" + name + "','" + emailid + "','" + password + "','"+img+"','"+phone+"')"
        mycursor.execute(q)
        conn.commit()
    return render(request, 'virtualapp/add chemist.html', {'mes': 'chemist added Succesfully'})

def patientlistdoc(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT `name`, `emailid`, `phone`, `dob`, `password` FROM `addpaitent` WHERE 1"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        return render(request, 'virtualapp/padd.html', {'mess': 'No doctors found'})
    else:
        records = mycursor.fetchall()
        return render(request, 'virtualapp/padd.html', {'records': records})



       #####
     #####
    ######
    ######################
    #######  manasm  #################        ##
    ######################                    ##
   #####                                   ##
      #####
def sendmed(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT medname,medno,medex  from medstock"
    mycursor.execute(query)
    records = mycursor.fetchall()
        # query1 = "SELECT name,medicine,dosage  FROM addprescription"
        # mycursor.execute(query1)
        # records1 = mycursor.fetchall()
        # query2 = "SELECT name,medcinename,date  FROM sendmed "
        # mycursor.execute(query2)
        # records3 = mycursor.fetchall()
    return render(request, 'virtualapp/home/sendmed.html', {'records': records})

def dispatch(request):
    if request.method == 'POST':

        s = request.POST["name"]
        p = request.POST["subject"]
        t = request.POST["message"]
        r = request.POST["message1"]
        v = datetime.now()
        b = str(v)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "insert into sendmed values('" + s + "','" + p + "','" + t + "','" + r + "','" + b + "')"
        mycursor.execute(q)
        conn.commit()
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        query = "SELECT name,medcinename,date  FROM sendmed"
        mycursor.execute(query)
        records = mycursor.fetchall()
        return render(request, 'virtualapp/home/SENDMED1.html', {'records': records})

    else:
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        query = "SELECT name,medcinename,date  FROM sendmed"
        mycursor.execute(query)
        records = mycursor.fetchall()
        return render(request, 'virtualapp/home/SENDMED1.html', {'records': records})
def labreport(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT name,type  FROM docreport"
    mycursor.execute(query)
    records = mycursor.fetchall()
    return render(request, 'virtualapp/home/labmakereport.html', {'records': records})

def addreports(request):
    t = request.POST["name"]
    r = request.POST["testtype"]
    s = request.POST["report"]
    v = datetime.now()
    b = str(v)
    print(b)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    q = "insert into report values('" + t + "','" + r + "','" + s + "','" + b + "')"
    mycursor.execute(q)
    conn.commit()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT name,type  FROM docreport"
    mycursor.execute(query)
    records = mycursor.fetchall()
    return render(request, 'virtualapp/home/labmakereport.html', {'records': records})

def addreport(request):
    return render(request, 'virtualapp/home/addreport.html')

def sendmed1(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT medname,medno,medex  from medstock"
    mycursor.execute(query)
    records = mycursor.fetchall()
    return render(request, 'virtualapp/home/senmed01.html', {'records': records})

def sendmed2(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT name,medicine,dosage  FROM addprescription"
    mycursor.execute(query)
    records = mycursor.fetchall()
    return render(request, 'virtualapp/home/pres.html', {'records': records})

def sendmed3(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT name,medcinename,date  FROM sendmed"
    mycursor.execute(query)
    records = mycursor.fetchall()
    return render(request, 'virtualapp/home/SENDMED1.html',{'records': records})
def drp(request):
    return render(request, 'virtualapp/chemist/docreportadd.html')


def drp2(request):
    if request.method == "POST":
        n = request.POST["p"]
        d = request.POST["m"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
        mycursor = conn.cursor()
        q = "insert into docreport values('"+p+"','"+m+"')"
        mycursor.execute(q)
        conn.commit()
    return render(request, 'virtualapp/padd.html')

def reportdoc(request):

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='vclinic1')
    mycursor = conn.cursor()
    query = "SELECT name,testtype,report,date  FROM report"
    mycursor.execute(query)
    records = mycursor.fetchall()
    return render(request, 'virtualapp/reportview.html', {'records': records})


def add_prescription(request):
    if request.method == "POST":
        name = request.POST["medname"]
        dosage = request.POST["dosname"]
        time = request.POST["medtime"]


