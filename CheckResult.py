import re ,sys
import mechanize
import datetime , time
from win10toast import ToastNotifier
from BeautifulSoup import BeautifulSoup

toaster = ToastNotifier()

def getExam(res ,year1 ,month1):
    if month1 >=1 and month1 <=5:
        year1 = year1 - 1
    html = BeautifulSoup(res)
    select_node = html.findAll('select', attrs={'title': 'Select Exam'})
    for optio in select_node[0].findAll('option'):
        for opvalue in optio:
            checkResult = optio.text

            if opvalue[0:3] == "NOV" and month1 == 12:
                if opvalue[10:14] == str(year1) and opvalue[17:24] == "REGULAR":
                    exam1 = str(optio['value'])
                    toaster.show_toast("Doom", "Result has arrived")
                    sys.exit(1)
                else:
                    print "Result Not Arrived Yet"
            elif opvalue[0:5] == "APRIL" and month1 <=11:
                if opvalue[13:17] == str(year1) and opvalue[20:27] == "REGULAR":
                    exam1 = str(optio['value'])
                    toaster.show_toast("Doom", "Result has arrived")
                    sys.exit(1)
                else:
                    print "Result Not There"
    
    
while (1):       
    enrollment =   #ENTER YOUR ENROLLMENT NUMBER HERE (NOT IN STRING FORMAT)
    branch1 = ""  #ENTER your branch in inverted comma. For Computer = "1", for IT = "2", Mechanical = "3", Mecha = "5", Biomed = "149", EC = "3", Civil = "7"
    sem1 = "" #Enter your SEM 1/2/3/4/5/6/7/8 in inverted comma
    now1 = datetime.datetime.now()
    month1 = now1.month
    year1 = now1.year
    url = "http://result.ganpatuniversity.ac.in"
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open(url)
    br.select_form(id="form1")
    br["ddlInst"] = ["1",]
    response = br.submit()
    br.reload()
    br.select_form(id="form1")
    br["ddlDegree"] = [branch1,]
    br.submit()
    br.reload()
    br.select_form(id="form1")
    br["ddlSem"] = [sem1,]
    res = br.submit()
    getExam(res ,year1 ,month1)
    time.sleep(600)