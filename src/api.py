#!/usr/bin/python
# -*- coding: latin-1 -*-

import pymongo
from pymongo import MongoClient
client = MongoClient('localhost',27017)

DB = client["Taller"]
Movies = DB["Movies"]
Companies=DB["Companies"]


#Consultar toda la información de la película con un título en particular.
def movieByTittle(title):
    movie = Movies.find_one({"title":title})
    print(movie)
    return movie

#Consultar  toda  la  información  de  las  películas  de  una  franquicia  en particular.
def movieByFranchise(franchise):
    movie = Movies.find({"franchise":franchise})
    print(movie)
    return movie


#Consultar toda la información de las películas estrenadas en un rango de años específico.
#def movieByRange(yearRange):

#Consultar el nombre de película, género, año de estreno de todas las películas producidas por una compañía productora en particular.
#def movieByCompany(Company):

#Consultar la cantidad de películas
#def cantMovies():

#Consultar la película con la menor duración 
def lessDuration():
    movie = Movies.find().sort("duration", 1).limit(0)
    print(movie[0])
    return movie[0]

#Consultar la  película  con  la  mayor  duración
def moreDuration():
    movie = Movies.find().sort("duration", -1).limit(0)
    #print(movie[0])
    return movie[0]

#Consultar la  duración  promedio  de  las películas producidas por una compañía productora en particular
#def averageDuration(Company)


def main():
    movie = lessDuration()
    print(movie)

main()