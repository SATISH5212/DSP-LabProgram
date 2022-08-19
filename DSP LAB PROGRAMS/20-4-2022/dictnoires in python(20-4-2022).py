#PYTHON DICTNOIRES AND OPERATIONS
d={"name":"satish","id":116,"class":"2E","branch":"CSE"}
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d["id"])
print(d.get("class"))
if 116 in d:   #this will  indentify keys only not values 
    print("roll no exists in dictnory")
else:
    print("rollno doesn't exists")
# changing the elements in dictnories
d["name"]="satheesh"
print(d)
d.update({"name":"satish"})
print(d)
#ADDING ELEMENTS IN DICTNORIES
d["batch"]=2018
print(d)#DELETING ELEMTS IN DICTONORIES
d.pop("batch")
print(d)
d.popitem()  #deletes last element
print(d)
del d["name"]
print(d)
d["name"]="satish"
print(d)
   
