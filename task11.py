import json
file = open("movie_details.json","r")
a = file.read()
data = json.loads(a)
i = 0
genre = {}
while i < len(data):
        for j,y in data[i].items():
                if j=="Genre:":
                    genre[y]=0
        i+=1
k = 0
while k < len(data):
    for d in genre:
        if d in data[k]["Genre:"]:
            genre[d]+=1
    k+=1
print(genre)
with open("analyse_movies_genre .json","w") as f:
        json.dump(genre,f,indent=4)

