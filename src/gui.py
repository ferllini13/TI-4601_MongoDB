#!/usr/bin/python
# -*- coding: latin-1 -*-

from Tkinter import *
import ttk
import os
import api
from api import *



window = Tk()
window.title("Robotic Finger")
window.geometry("500x430")

#if press touch
def bytittle():
	value = title.get()#get the seconds to press
	data= movieByTittle(str(value))
	print(data)


#if press press
def byfranchise():
	value = fran.get()#get the seconds to pres
	data= movieByTittle(str(value))
	print(data)



#if press move to
def byrange():
	y1 = year1.get()# get the key to move to
	y2 = year2.get()# get the key to move to
	data=movieByRange(int(y1),int(y2))
	print(data)

def bycompany():
	company = comp.get()
	data=movieByCompany(str(company))
	companyDAta()
	print(data)

# write the configuration file
def companyDAta():
	company = comp.get()
	averageDuration()
	moreDuration(str(company))
	lessDuration(str(company))
	cantMovies(str(company))

	




Label(window,text="movies",fg="black",font="none 12 bold").place(x=10,y=250)
Label(window,text="more duration",fg="black",font="none 12 bold").place(x=10,y=280)
Label(window,text="less duration",fg="black",font="none 12 bold").place(x=10,y=310)
Label(window,text="average duration",fg="black",font="none 12 bold").place(x=10,y=340)

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

# deifne the buttons
Button(window, text ="movie by tittle",command = bytittle, height = 2, width = 20).place(x=10,y=50)
Button(window, text ="movies by franchise",command = byfranchise, height = 2, width = 20).place(x=10,y=100)
Button(window, text ="movies in range",command = byrange, height = 2, width = 20).place(x=10,y=150)
Button(window, text ="company data",command = bycompany, height = 2, width = 20).place(x=10,y=200)
     
window.mainloop()




#Consultar toda la información de la película con un título en particular.
#Consultar  toda  la  información  de  las  películas  de  una  franquicia  en particular.
#Consultar toda la información de las películas estrenadas en un rango de años específico.
#Consultar el nombre de película, género, año de estreno de todas las películas producidas por una compañía productora en particular.
#Consultar la cantidad de películas de compañia e  las películas producidas por una compañía productora en particular
#Consultar la película con la menor duración e  las películas producidas por una compañía productora en particular
#Consultar la  película  con  la  mayor  duracióne  las películas producidas por una compañía productora en particular
#Consultar la  duración  promedio  de  las películas producidas por una compañía productora en particular
