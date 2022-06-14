import requests
from bs4 import BeautifulSoup
import json , os.path
# import pprint
f = open("top_movie.json","r")
read = f.read()
data = json.loads(read)
# get_all_movie_details = []
i  = 0
movie_cast={}
cast=[]
while i < len(data):
    print(str(i+1)+".",data[i]["movie_name"])
    user =data[i]["movie URL"]
    name=data[i]["movie_name"]
    # n = 0
    actor_list = []
    # dict1={"actor_name":"","id":""}
    page = requests.get(user)
    soup = BeautifulSoup(page.text,'html.parser')
    actor = soup.find('div',class_ = "col mob col-center-right col-full-xs mop-main-column")
    castsection = actor.find('section',id ="movie-cast")
    crew = castsection.find_all('div',class_="media-body")
    for J in crew :
        dict1 = {"id":"","actor_name":""}
        character = J.find('span',class_ = "characters subtle smaller").get_text().strip()
        print(character)
        if character == "Director":
            break
        else:
            if J.find('a') != None :
                    dict1["actor_name"]= J.span.get_text().strip()
                    dict1["id"]= J.a["href"].strip()
                    actor_list.append(dict1)
        movie_cast[name]=actor_list
        cast.append(movie_cast)
    i=i+1
with open("movie_castdetails.json","w") as f:
    json.dump(cast,f,indent=4)
user1=input("enter the movie name")
# n=0
for n in data:
        if n["movie_name"] == user1:
            if os.path.exists((n["movie_name"].strip())+"cast.json"):
                with open(str(n["movie_name"].strip())+"cast.json","r") as f:
                    data = json.load(f)
                    print(data)
            else:
                def analyse_actors (movie_cast):
                    for j in movie_cast:
                        s=j[user1]
                    with open(str(n["movie_name"].strip())+"cast.json","w") as f:
                        json.dump(s,f,indent=4)
                    
                #   page   = requests.get(movie_url)
                #     soup = BeautifulSoup(page.text,'html.parser')
                #     actor = soup.find('div',class_ = "col mob col-center-right col-full-xs mop-main-column")
                #     castsection = actor.find('section',id ="movie-cast")
                #     crew = castsection.find_all('div',class_="media-body")
                #     for i in crew :
                #         dict1 = {"id":"","actor_name":""}
                #         character = i.find('span',class_ = "characters subtle smaller").get_text().strip()
                #         print(character)
                #         if character == "Director":
                #             break
                #         else:
                #             if i.find('a') != None :
                #                 dict1["actor_name"]= i.span.get_text().strip()
                #                 dict1["id"]= i.a["href"].strip()
                #                 actor_list.append(dict1)
                #                 movie_cast[user]=dict1
                #                 cast.append(movie_cast)
                analyse_actors(cast)
        #         with open(str(n["movie_name"].strip())+"cast.json","w") as f:
        #             json.dump(actor_list,f,indent=4)
        # # n+=1
# with open("movie_castdetails.json","w") as f:
#     json.dump(cast,f,ident=4)