import json

def group_of_decades(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod=int(index)%10
        decade=int(index)-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            a=int(x)
            if a>=i and a<=dec10:
                for v in movies[x]:
                    moviedec[i].append(v)
    with open("groups_of_decades.json","w") as file:
        json.dump(moviedec,file,indent=4)
    return(moviedec)
file = open("movie_by_year.json","r")
read = file.read()
data = json.loads(read)
print(group_of_decades(data))


# nestedlist = [ [1, 2, 3, 4], ["Ten", ["Twenty",["tywentyone","twentytwo","twentythree"]], "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]
# flatlist=[element for sublist in nestedlist for element in sublist]
# print(flatlist)
original_list = [[1,2], [3], [4,5,[6,[7,8,[9,10]]]]]                                                                                                                         
# def flatten(potential_list): 
#    new_list = [] 
#    for e in potential_list:
#        if isinstance(e, list):
#            new_list.extend(flatten(e))
#        else:
#            new_list.append(e)
#    return new_list
# print(flatten(original_list))

flat_list=sum(original_list,[])
print(flat_list)