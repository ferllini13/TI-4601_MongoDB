#!/usr/bin/python
# -*- coding: latin-1 -*-

import pymongo
from pymongo import MongoClient
client = MongoClient('localhost',27017)

DB = client["Taller"]
Movies = DB["Movies"]
Companies=DB["Companies"]



#elimnar
#def mDel():
#def cDel():


#agregar
def mAdd(title,genre,director_name,franchise,country,year,duration,company,actors):
    data={
	    "title":title,
		"genre":genre,
		"director_name":director_name,
		"franchise":franchise,
		"country":country,
		"year":int(year), 
		"duration":int(duration), 
		"company":company, 
		"actors":actors
    }

    Movies.insert_one(data)


def cAdd(name,year,web_address):
    data={
		"name":name,
		"year":year,
		"web_address":web_address  
    }

    Companies.insert_one(data)




#editar 
#def mEdit():
#def cEdit():



#Consultar toda la información de la película con un título en particular.
def movieByTittle(title):
    movie = Movies.find_one({"title":title})
    return movie

#Consultar  toda  la  información  de  las  películas  de  una  franquicia  en particular.
def movieByFranchise(franchise):
    movie = Movies.find({"franchise":franchise})
    return list(movie)


#Consultar toda la información de las películas estrenadas en un rango de años específico.
def movieByRange(year1,year2):
    movie = Movies.find_one({ "$and": [{"year":{"$gte":year1}}, {"year":{"$lte":year2}}]})
    return movie


#Consultar el nombre de película, género, año de estreno de todas las películas producidas por una compañía productora en particular.
def movieByCompany(Company):
    movie = Movies.aggregate ([{"$match" : { "company" : Company }},{"$project" : {"title":1, "genre":1, "year":1 }}]) 
    return list(movie)


#Consultar la cantidad de películas de compañia e  las películas producidas por una compañía productora en particular
def cantMovies(Company):
    cant = Movies.find({"company":Company}).count()
    return cant

#Consultar la película con la menor duración e  las películas producidas por una compañía productora en particular
def lessDuration(Company):
    movie = Movies.find({"company":Company}).sort("duration", 1).limit(0)
    return movie[0]

#Consultar la  película  con  la  mayor  duracióne  las películas producidas por una compañía productora en particular
def moreDuration(Company):
    movie = Movies.find({"company":Company}).sort("duration", -1).limit(0)
    return movie[0]

#Consultar la  duración  promedio  de  las películas producidas por una compañía productora en particular
def averageDuration():
    cant = Movies.aggregate([{"$group":{"_id": "$company","average": { "$avg": "$duration" }}}]) 
    return list(cant)


