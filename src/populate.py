import pymongo
from pymongo import MongoClient
client = MongoClient('localhost',27017)

DB = client["Taller"]
Movies = DB["Movies"]
Companies=DB["Companies"]


movies = [
    {
							"title":"Ant-Man",
							"genre":"Action",
							"director_name":"Peyton Reed",
							"franchise":"",
							"country":"USA",
							"year":int(2015), 
							"duration":117, 
							"company":"Marvel Studios", 
							"actors":[{"name":"Paul Rudd"},{"name":"Michael Douglas"},{"name":"Corey Stoll"}]
    },
    {
							"title":"A Clockwork Orange",
							"genre":"Crime",
							"director_name":"Stanley Kubrick",
							"franchise":"",
							"country":"England",
							"year":int(1971), 
							"duration":136, 
							"company":"UK Films", 
							"actors":[{"name":"Malcolm McDowell"},{"name":"Patrick Magee"},{"name":"Michael Bates"}]
    },
    {
							"title":"Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb",
							"genre":"Comedy",
							"director_name":"Stanley Kubrick",
							"franchise":"",
							"country":"England",
							"year":int(1964), 
							"duration":95, 
							"company":"UK Films", 
							"actors":[{"name":"Peter Sellers"},{"name":"George C. Scott"},{"name":"Sterling Hayden"}]
    },
    {
							"title":"X-Men: First Class",
							"genre":"Action & Sci-Fi",
							"director_name":"Matthew Vaughn",
							"franchise":"X-Men Franchise",
							"country":"USA",
							"year":int(2011), 
							"duration":131, 
							"company":"Marvel Studios", 
							"actors":[{"name":"James McAvoy"},{"name":"Michael Fassbender"},{"name":"Jennifer Lawrence"}]
    },
    {
							"title":"X-Men: Days of Future Past",
							"genre":"Action & Sci-Fi",
							"director_name":"Bryan Singer",
							"franchise":"X-Men Franchise",
							"country":"USA",
							"year":int(2014), 
							"duration":132, 
							"company":"Marvel Studios", 
							"actors":[{"name":"Patrick Stewart"},{"name":"Hugh Jackman"},{"name":"Ian McKellen"}]
    }
]

companies=[
    {
		"name":"Marvel Studios",
		"year":"1993",
		"web_address":"www.marvel.com"	  
    },
    {
		"name":"UK Films",
		"year":"1978",
		"web_address":"www.ukfilms.com"	  
    }
]


Movies.insert_many(movies)
Companies.insert_many(companies)