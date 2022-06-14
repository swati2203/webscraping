import json
from bs4 import BeautifulSoup
import requests
from task1 import data
def movie_details(movies,m):
        j=0
        # a={}
        while j<len(movies):
            if m==movies[j]["movie_name"]:
                newurl=movies[j]["movie URL"]
                x=requests.get(newurl)
                soup=BeautifulSoup(x.text,"html.parser")
                movie_find_1=soup.find("ul",class_="content-meta info")
                movie_find_2=movie_find_1.find_all("li",class_="meta-row clearfix")
                my_dict={}
                for i in movie_find_2:
                    alldata=i.find("div",class_="meta-label subtle").get_text().strip()
                    allvalue=i.find("div",class_="meta-value").get_text().strip().replace("\n","")
                    my_dict.update({alldata:allvalue})
                # a.update({m:my_dict})
            j=j+1
        return my_dict
i=1
a=[]
while i<=10:
    mn=input("enter the movie name")
    b=movie_details(data,mn)
    a.append(b)
    print(a)
    i=i+1
with open("movie_details.json","w") as file:
    json.dump(a,file,indent=4)




