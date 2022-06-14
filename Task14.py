from csv import DictReader
import json


with open("all_movie1_details.json","r") as f:
    data=json.load(f)
dict1={}
i=0
sum=0
while i<len(data):
    for j in data[i]["cast"]:
        dict1[j["id"]]={}
    i=i+1
dict2={}
for k in dict1:
    l=0
    c=0
    sum=""
    list1=[]
    while l<len(data):
        for m in data[l]["cast"]:
            if k==m["id"]:
                c+=1
                sum=m["movie_name"]
                list1.append(data[l]["name"])
        l=l+1
    if c>=2:
        dict2[k]={}
        dict2[k]["name"]=sum
        dict2[k]["movies"]=list1
        dict2[k]
print(dict2)