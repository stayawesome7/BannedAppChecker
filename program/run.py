import tkinter as tk
from PIL import ImageTk, Image
import subprocess
from fpdf import FPDF
import os
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
#print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
only_date_string = now.strftime("%d/%m/%Y")
#print("date and time =", dt_string)

window = tk.Tk()

width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))

#window.attributes('-fullscreen', True)
window.title("BANNED APP CHECKER")
window.iconbitmap("dagger.ico")

headLabel = tk.Label(window,text="BANNED APP CHECKER")
headLabel.config(font=("calibre", 44),width=200,bg="yellow")
headLabel.pack()

leftimage = tk.PhotoImage(file="daggerlogo.png")
leftimagelabel = tk.Label(image=leftimage).place(x=2,y=2)
rightimage = tk.PhotoImage(file="jimmylogo.png")
rightimagelabel = tk.Label(image=rightimage).place(x=1210,y=2)
# rightimagelabel.pack()
# image1 = Image.open("dagger.png")
# image1 = image1.resize((150, 150), Image.ANTIALIAS)


#listBannedApps = ["com.instagram.android","com.facebook.katana","com.facebook.lite","com.facebook.orca","com.zhiliaoapp.musically","com.tencent.mm","com.tinder","com.UCMobile.intl",
# 					"jp.naver.line.android","us.zoom.videomeetings","free.video.downloader.freevideodownloader"]
#listBannedApps = []

listMeet = open("bannedlist.txt").read().split("\n")
listBannedAppsNames = []
listBannedApps = []
for i in listMeet:
	listBannedAppsNames.append(i.split(":")[0])
	listBannedApps.append(i.split(":")[-1])





listUsersChecked = []
foundBannedAPPList = []
foundBannedAppFlag = False

def addBannedApp():
	if e1.get():
		listBannedApps.append(e1.get())
		listBannedAppsNames.append(e1.get())
	e1.delete(0, 'end')
	#print(e1.get())

def viewBannedApp():
	y1=0
	for app in listBannedAppsNames[:12]:
			tk.Label(frame1,text=app,font=('calibre',11, 'bold')).place(x=85,y=223+y1)
			y1=y1+29
		#print(app)
	y1=0
	for app in listBannedAppsNames[12:24]:
			tk.Label(frame1,text=app,font=('calibre',11, 'bold')).place(x=275,y=223+y1)
			y1=y1+29

frame1 = tk.Frame(master=window, width=425, height=100, bg="#48b4e0",relief=tk.GROOVE, borderwidth=7)
frame1.pack(fill=tk.Y,side=tk.LEFT)

frame1headLabel = tk.Label(frame1,text="1. Add Banned APP",fg="white")
frame1headLabel.config(font=("Arial-bold", 15,'bold'),width=23,bg="red")
frame1headLabel.place(x=80,y=7)


e1 = tk.Entry(master=frame1,width=35,bg="yellow",borderwidth=3,font=('calibre',11, 'bold'))
e1.place(x=65, y=69)
e1.insert(0,"Example : com.instagram.android")
#activebackground='#345',activeforeground='white', padx=5, pady=5 ).pack(pady=10)
#borderwidth=3, relief="groove",padx=5, pady=10
b1 = tk.Button(frame1,text="Add Package",bg='#F1C40F', font=('calibre',13, 'bold'),borderwidth=4, relief="ridge",
	activebackground='#345',activeforeground='white', padx=3, pady=3,command=addBannedApp)

b1.place(x=159,y=109)
b1 = tk.Button(frame1,height=2,width=11,text="List All Apps",bg='#F1C40F', font=('calibre',13, 'bold'),borderwidth=4, relief="ridge",
	activebackground='#345',activeforeground='white', padx=3, pady=3,command=viewBannedApp)
b1.place(x=157,y=161)

smartphoneDetailsDict = {}
def viewSmartphoneDetails():
	y1=0
	vectors = ["net.bt.name","ro.product.vendor.marketname","ro.product.vendor.model","ro.serialno","ro.ril.miui.imei0"]
	for vector in vectors:
		result = subprocess.run(["adb", "shell", "getprop", vector], capture_output=True, text=True)
		#print(vector.split(".")[-1] + " : " + result.stdout)
		tk.Label(frame2, font=('calibre',10, 'bold'),text=vector.split(".")[-1] + " : " + result.stdout).place(x=131,y=105+y1)
		smartphoneDetailsDict[str(vector.split(".")[-1])] = result.stdout
		y1=y1+27
	#print(smartphoneDetailsDict)

pers_armyno = tk.StringVar()
pers_rank = tk.StringVar()
pers_name = tk.StringVar()
pers_unit = tk.StringVar()

class Pers:
  def __init__(self, pers_armyno,pers_rank,pers_name,pers_unit):
    self.armyno = pers_armyno
    self.rank = pers_rank
    self.name = pers_name
    self.unit = pers_unit

#p1 = Pers("ic82408h","capt","AJ Dixit","18 RAJ RIF")
#print(p1.armyno + p1.rank + p1.name + p1.unit)  

frame2 = tk.Frame(master=window, width=425, bg="#2B36D5",relief=tk.GROOVE, borderwidth=7)
frame2.pack(fill=tk.Y,side=tk.LEFT)


frame2headLabel = tk.Label(frame2,text="2. Smartphone & Pers Details",fg="white")
frame2headLabel.config(font=("Arial-bold", 15,'bold'),width=27,bg="red")
frame2headLabel.place(x=63,y=7)


b2 = tk.Button(frame2,text="Click for Smartphone Details", bg='#F1C40F',font=('calibre',13, 'bold'),borderwidth=4, relief="ridge",
	activebackground='#345',activeforeground='white', padx=3, pady=3,command=viewSmartphoneDetails)
b2.place(x=93,y=59)

section_label = tk.Label(frame2, text = 'Enter Pers Details', font=('calibre',13, 'bold'))
section_label.place(x=139,y=297)

name_label = tk.Label(frame2, text = 'Army No', font=('calibre',10, 'bold'))
name_label.place(x=49,y=331)
armyno_entry = tk.Entry(frame2,width=27,textvariable = pers_armyno, font=('calibre',10,'normal'))
armyno_entry.place(x=139,y=331)

name_label = tk.Label(frame2, text = 'Rank', font=('calibre',10, 'bold'))
name_label.place(x=49,y=359)
rank_entry = tk.Entry(frame2,width=27,textvariable = pers_rank, font=('calibre',10,'normal'))
rank_entry.place(x=139,y=359)

name_label = tk.Label(frame2, text = 'Name', font=('calibre',10, 'bold'))
name_label.place(x=49,y=387)
name_entry = tk.Entry(frame2,width=27,textvariable = pers_name, font=('calibre',10,'normal'))
name_entry.place(x=139,y=387)

name_label = tk.Label(frame2, text = 'Unit', font=('calibre',10, 'bold'))
name_label.place(x=49,y=417)
unit_entry = tk.Entry(frame2,width=27,textvariable = pers_unit, font=('calibre',10,'normal'))
unit_entry.place(x=139,y=417)
name_label = tk.Label(frame2, text = 'Created By : Capt Ajay Dixit  19 IDSR', font=('calibre',11, 'bold'))
name_label.place(x=75,y=539)
def addPersDetails():
	# print(pers_armyno.get())
	# print(pers_rank.get())
	# print(pers_name.get())
	# print(pers_unit.get())

	pers = Pers(pers_armyno.get(),pers_rank.get(),pers_name.get(),pers_unit.get())
	listUsersChecked.append(pers)
	#print(pers.armyno+pers.rank+pers.name+pers.unit)

def clearDetails():
	armyno_entry.delete(0, 'end')
	rank_entry.delete(0, 'end')
	unit_entry.delete(0, 'end')
	name_entry.delete(0, 'end')

b3 = tk.Button(frame2,text="Add Details",font=('calibre',11, 'bold'),bg='#F1C40F',borderwidth=4, relief="ridge",
	activebackground='#345',activeforeground='white', padx=3, pady=3,command=addPersDetails)
b3.place(x=147,y=457)
b4 = tk.Button(frame2,text="Clear",font=('calibre',11, 'bold'),bg='#F1C40F',borderwidth=4, relief="ridge",
	activebackground='#345',activeforeground='white', padx=3, pady=3,command=clearDetails)
b4.place(x=287,y=457)




frame3 = tk.Frame(master=window, width=425, bg="#017D11",relief=tk.GROOVE, borderwidth=7)
frame3.pack(fill=tk.Y,side=tk.LEFT)

frame3headLabel = tk.Label(frame3,text="3. Scan & Generate Wizard",fg='white')
frame3headLabel.config(font=("Arial-bold", 15,'bold'),width=23,bg="red")
frame3headLabel.place(x=80,y=7)
runOnceFlag = 0
def checkBannedApps():
	outputSet = set()
	global runOnceFlag
	runOnceFlag = runOnceFlag + 1

	if runOnceFlag == 1:
		global foundBannedAPPList
		global foundBannedAppFlag
		y1 = 0
		appList = []
		result = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True)
		for i in range(len(result.stdout.split("\n"))):
			appList.append(result.stdout.split("\n")[i].split(":")[-1])
		
		outputSet = set(listBannedApps) & set(appList)

		if len(outputSet) == 0:
			tk.Label(frame3,text="NO BANNED APP FOUND !",font=('calibre',11, 'bold'),fg="green").place(x=131,y=127)

		else:
			for e in outputSet:
				foundBannedAPPList.append(e)
				tk.Label(frame3,text=e,font=('calibre',11, 'bold'),fg="red").place(x=141,y=101+y1)
				y1 = y1+27
			foundBannedAppFlag = True
		# print(foundBannedAppFlag)
	else:
		return



class PDF(FPDF):
    def header(self):
        # Logo
        self.image('dagger.png', 7, 5, 19)
        self.image('jimmy.jpg', 180, 5, 19)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(55, 10, 'Report : Banned App ', 1, 0, 'L')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def generateReport(listUsersChecked,foundBannedAPPList,foundBannedAppFlag):
	#print("report generation under progress")
	#print(foundBannedAppFlag)
	# print(listUsersChecked[-1].armyno)
	# print(listUsersChecked[-1].name)

	pdf = PDF()
	pdf.alias_nb_pages()
	pdf.add_page()
	pdf.set_font('Times', '', 12)
	pdf.cell(10, 10, ' ' , 0, 1)
	#pdf.cell(10, 10, ' ' , 0, 1)
	#pdf.cell(10, 10, dt_string , 0, 1)
	#pdf.cell(10, 10, ' ' , 0, 1)
	pdf.cell(10, 10, '1.	Personal Details ' , 0, 1)
	pdf.cell(10, 10, 'Army No :   '+listUsersChecked[-1].armyno, 5, 5)
	pdf.cell(0, 10, 'Rank :   '+listUsersChecked[-1].rank , 0, 1)
	pdf.cell(0, 10, 'Name :   '+listUsersChecked[-1].name, 0, 1)
	pdf.cell(0, 10, 'Unit :   '+listUsersChecked[-1].unit, 0, 1)
	pdf.cell(10, 10, ' ' , 0, 1)

	pdf.cell(20, 10, '2.	Smartphone Details ' , 0, 1)
	pdf.cell(10, 10, 'Name : '+ smartphoneDetailsDict['name'] , 0, 1)
	pdf.cell(10, 10, 'Market Name : '+ smartphoneDetailsDict['marketname'] , 0, 1)
	pdf.cell(10, 10, 'Model : '+ smartphoneDetailsDict['model'] , 0, 1)
	pdf.cell(10, 10, 'Serial Number : '+ smartphoneDetailsDict['serialno'] , 0, 1)
	pdf.cell(10, 10, 'IMEI Number : '+ smartphoneDetailsDict['imei0'] , 0, 1)
	pdf.cell(10, 10, ' ' , 0, 1)

	pdf.cell(10, 10, '3.	Banned Apps Section ' , 0, 1)

	if foundBannedAppFlag:
		pdf.set_font('Times','',15.0)
		pdf.set_text_color(255,0,0)
		pdf.cell(10, 10, 'Banned App Found :  '+'Yes !', 0, 1)
		for i in range(len(foundBannedAPPList)):
			pdf.cell(10, 10, str(i+1) + " : " + str(foundBannedAPPList[i]) , 0, 1)
	else:
		pdf.set_font('Times','',15.0)
		pdf.set_text_color(0,255,0)
		pdf.cell(10, 10, 'Banned App Found :  '+'No !', 0, 1)
	pdf.cell(10, 10, ' ' , 0, 1)
	#pdf.cell(10, 10, ' ' , 0, 1)
	pdf.set_font('Times','',11.0)
	pdf.set_text_color(0,0,0)
	pdf.cell(10, 10, 'Checked By : '+ checked_by.get() , 0, 1)
	#pdf.cell(10, 10, ' ' , 0, 1)
	pdf.cell(10, 10, dt_string , 0, 1)
	pdf.cell(10, 10, ' ' , 0, 1)
	pdf.cell(10, 10, "Checker Sign  -   _________________                                                         Indl Sign  -  _________________" , 0, 1)

	pdf.output(listUsersChecked[-1].armyno + '_report.pdf', 'F')
	


def uninstallApp():
	y1 = 0
	if len(foundBannedAPPList) == 0:
		tk.Label(frame3,text="No Banned App for Uninstallation !",font=('calibre',11, 'bold'),fg="green").place(x=87,y=480)
	else:
		for app in foundBannedAPPList:
			result = subprocess.run(["adb", "uninstall", app ], capture_output=True, text=True)
			#print(result)
			if result.returncode == 0:
				tk.Label(frame3,text=str(app.split(".")[1]) + ' Uninstalled Suceessfully ',fg="green").place(x=137,y=479+y1)
				y1= y1 + 27

			else:
				tk.Label(frame3,text=str(app.split(".")[1]) + 'Uninstall Failed',fg="red").place(x=161,y=490+y1)



	#result = subprocess.run(["adb", "uninstall", ], capture_output=True, text=True)
	#foundBannedAPPList


b5 = tk.Button(frame3,text="Check For Banned APPS",font=('calibre',11, 'bold'),bg='#F1C40F',borderwidth=4, relief="ridge",
	activebackground='#345',activeforeground='white', padx=3, pady=3,command=checkBannedApps)
b5.place(x=129,y=59)

checked_by = tk.StringVar()
name_label = tk.Label(frame3, text = 'Checked By', font=('calibre',12, 'bold'))
name_label.place(x=59,y=301)
checkedby_name = tk.Entry(frame3,width=19,textvariable = checked_by, font=('calibre',12,'normal'))
checkedby_name.place(x=171,y=301)



b6 = tk.Button(frame3,height=2,width=15,font=('calibre',11, 'bold'),text="Generate Report",bg='#F1C40F',borderwidth=4, relief="ridge",
	activebackground='#345',activeforeground='white', padx=3, pady=3,command=lambda:generateReport(listUsersChecked,foundBannedAPPList,foundBannedAppFlag))
b6.place(x=137,y=353)

b7 = tk.Button(frame3,height=2,width=17,font=('calibre',11, 'bold'),text="Uninstall Banned App",bg='#F1C40F',borderwidth=4, relief="ridge",
	activebackground='#345',activeforeground='white', padx=3, pady=3,command=uninstallApp)
b7.place(x=129,y=417)

tk.Label(frame3,text=only_date_string).place(x=343,y=547)
# for j in listUsersChecked:
# 	print(j)
window.mainloop()