import re ,sys, os
import mechanize
import datetime , time
from BeautifulSoup import BeautifulSoup

def getinfo(enrollment):
    now = datetime.datetime.now()
    currentyear = now.year
    currentmonth = now.month
    st = enrollment[0:2]
    studentyear = "20" + st
    branch = enrollment[6]
    dip = enrollment[7]
    diff = currentyear - int(studentyear)
    if currentmonth >= 7 and diff == 0:
        sem = 1
    elif currentmonth >= 7 and diff == 1:
        if dip == "2":
            sem = 5
        else:
            sem = 3
    elif currentmonth >= 7 and diff == 2:
        if dip == "2":
            sem = 7
        else:
            sem = 5
    elif currentmonth >= 7 and diff == 3:
        sem = 7
    elif currentmonth < 7 and diff == 1:
        if dip == "2":
            sem = 4
        else:
            sem = 2
    elif currentmonth < 7 and diff == 2:
        if dip == "2":
            sem = 6
        else:
            sem = 4
    elif currentmonth < 7 and diff == 3:
        if dip == "2":
            sem = 8
        else:
            sem = 6
    elif diff == 4:
        sem = 8
    
    if branch == "1":
        br = "1" #computer
    elif branch == "2":
        br = "2" #IT
    elif branch == "3":
        br = "6" #mechanical
    elif branch == "4":
        br = "5" #mecha
    elif branch == "5":
        br = "149" #biomedical
    elif branch == "6":
        br = "3" #EC
    elif branch == "7":
        br = "7" #civil
    return sem, br

def getExam(res ,year1 ,month1):
    if month1 >=1 and month1 <=5:
        year1 = year1 - 1
    # resp = open("C:/Users/Darsh/Desktop/response1.txt" , "r")
    # line = resp.readline()
    #print prevResponse
    html = BeautifulSoup(res)
    select_node = html.findAll('select', attrs={'title': 'Select Exam'})
    for optio in select_node[0].findAll('option'):
        for opvalue in optio:
            checkResult = optio.text

            if opvalue[0:3] == "NOV" and month1 == 12:
                if opvalue[10:14] == str(year1) and opvalue[17:24] == "REGULAR":
                    exam1 = str(optio['value'])
                else:
                    print "Result Not Arrived Yet"
            elif opvalue[0:5] == "APRIL" and month1 <=11:
                if opvalue[13:17] == str(year1) and opvalue[20:27] == "REGULAR":
                    exam1 = str(optio['value'])
                else:
                    print "Result Not There"
    #resp.close()
    return exam1
        

enrollment = sys.argv[1]
sem1, br1 = getinfo(enrollment)
now1 = datetime.datetime.now()
month1 = now1.month
year1 = now1.year
if month1 >= 7 and month1 <=11:
    sem2 = sem1 - 1
elif month1 >=1 and month1 <=5:
    sem2 = sem1 - 1
elif month1 == 12 or month1 == 6:
    sem2 = sem1 - 1
print sem2
url = "http://result.ganpatuniversity.ac.in"
br = mechanize.Browser()
br.set_handle_robots(False)
br.open(url)
br.select_form(id="form1")
br["ddlInst"] = ["1",]
response = br.submit()
br.reload()
br.select_form(id="form1")
br["ddlDegree"] = [br1,]
br.submit()
br.reload()
br.select_form(id="form1")
br["ddlSem"] = [str(sem2),]
res = br.submit()
exam = getExam(res ,year1 ,month1)
br.reload()
br.select_form(id="form1")
br["ddlScheduleExam"] = [exam,]
br["txtEnrNo"] = str(enrollment)
resp2 = br.submit()
content = resp2.read()
with open("*path to result html file*", "w") as f: #give location for where to put result once fetched.. usually keep it to your desktop.
    f.write(content)
