#!/usr/bin/python
# -*- coding: latin-1 -*-

from Tkinter import *
import ttk
import tkMessageBox
import os
import api
from api import *




window = Tk()
window.title("Robotic Finger")
window.geometry("700x430")


def printmovie(data):
	newwin = Toplevel(window)    
	Lb1 = Listbox(newwin)
	Lb1.insert(1,data["title"])
	Lb1.insert(2,data["genre"])
	Lb1.insert(3,data["director_name"])
	Lb1.insert(4,data["franchise"])
	Lb1.insert(5,data["country"])
	Lb1.insert(6,data["year"])
	Lb1.insert(7,data["duration"])
	Lb1.insert(8,data["company"])
	Lb1.insert(9,data["actors"])
	Lb1.pack()


def printComp(data):
	newwin = Toplevel(window)    
	Lb1 = Listbox(newwin)
	Lb1.insert(1,data["title"])
	Lb1.insert(2,data["genre"])
	Lb1.insert(3,data["year"])
	Lb1.pack()

#if press touch
def bytittle():
	value = title.get()#get the seconds to press
	data= movieByTittle(str(value))
	print ("################### Movie By Title ########################")
	print(data)
	print ("###########################################################")
	printmovie(data)





#if press press
def byfranchise():
	value = fran.get()#get the seconds to pres
	data= movieByFranchise(str(value))
	print ("################### Movie By Franchise ########################")
	print(data)
	print ("###############################################################")
	for x in data:
		printmovie(x)




#if press move to
def byrange():
	y1 = year1.get()# get the key to move to
	y2 = year2.get()# get the key to move to
	data=movieByRange(int(y1),int(y2))
	print ("################### Movies in Range ########################")
	print(data)
	print ("############################################################")
	for x in data:
		printmovie(x)


def bycompany():
	company = comp.get()
	data=movieByCompany(str(company))
	companyDAta()
	print ("################### Movies by Company ########################")
	print(data)
	print ("##############################################################")
	for x in data:
		printComp(x)

# write the configuration file
def companyDAta():
	company = comp.get()
	val0=averageDuration()
	val1=moreDuration(str(company))
	val2=lessDuration(str(company))
	val3=cantMovies(str(company))

	print ("################### More duration ########################")
	print(val1)
	print ("################### less duration ########################")
	print(val2)
	print ("###################  Cant Movies  ########################")
	print(val3)
	print ("################### Average time  ########################")
	for x in val0:
		if x["_id"]==company:
			print(x["average"])
			var4.set(x["average"])
	
	var1.set(val3)
	var2.set(val1["duration"])
	var3.set(val2["duration"])
	


def addmov():
	data= addM.get()
	mAdd2(data)
def addcom():
	data= addC.get()
	cAdd2(data)



var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()

result=StringVar()

Label(window,text="movies",fg="black",font="none 12 bold").place(x=10,y=250)
mov=Label(window,textvariable=var1,fg="black",font="none 12 bold").place(x=200,y=250)

Label(window,text="more duration",fg="black",font="none 12 bold").place(x=10,y=280)
more=Label(window,textvariable=var2,fg="black",font="none 12 bold").place(x=200,y=280)

Label(window,text="less duration",fg="black",font="none 12 bold").place(x=10,y=310)
less=Label(window,textvariable=var3,fg="black",font="none 12 bold").place(x=200,y=310)

Label(window,text="average duration",fg="black",font="none 12 bold").place(x=10,y=340)
av=Label(window,textvariable=var4,fg="black",font="none 12 bold").place(x=200,y=340)




#entry for seconds to press
title=Entry(window,width=10, bg="black",font="none 12 bold")
title.place(x=250,y=50)
#Label(window,text="SECONDS",fg="black",font="none 12 bold").place(x=300,y=50)

fran=Entry(window,width=10, bg="black",font="none 12 bold")
fran.place(x=250,y=100)


year1=Entry(window,width=4, bg="black",font="none 12 bold")
year1.place(x=250,y=150)
year2=Entry(window,width=4, bg="black",font="none 12 bold")
year2.place(x=320,y=150)

comp=Entry(window,width=10, bg="black",font="none 12 bold")
comp.place(x=250,y=200)


Label(window,text="Add Movie",fg="black",font="none 12 bold").place(x=400,y=10)
addM=Entry(window,width=25, bg="black",font="none 12 bold")
addM.place(x=400,y=40)
Button(window, text ="ADD",command = addmov, height = 2, width = 20).place(x=400,y=70)


Label(window,text="Add Company",fg="black",font="none 12 bold").place(x=400,y=210)
addC=Entry(window,width=25, bg="black",font="none 12 bold")
addC.place(x=400,y=250)
Button(window, text ="ADD",command = addcom, height = 2, width = 20).place(x=400,y=280)


# deifne the buttons
Button(window, text ="movie by tittle",command = bytittle, height = 2, width = 20).place(x=10,y=50)
Button(window, text ="movies by franchise",command = byfranchise, height = 2, width = 20).place(x=10,y=100)
Button(window, text ="movies in range",command = byrange, height = 2, width = 20).place(x=10,y=150)
Button(window, text ="company data",command = bycompany, height = 2, width = 20).place(x=10,y=200)
     
window.mainloop()
