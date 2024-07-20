d= {"name": "shubham",
    "add": "titwala",
     "marks": 90, 
     0:"zero" }
# print(d[0])
# print(d["add"])
# print(d["name"])
# print(d.items()) #dict_items([('name', 'shubham'), ('add', 'titwala'), ('marks', 90), (0, 'zero')])
# print(d.keys()) #dict_keys(['name', 'add', 'marks', 0])
# print(d.values())  #dict_values(['shubham', 'titwala', 90, 'zero'])
d.update({"marks":99})
d.update({"add": "murbad", "dept":"devops"}) #existing change & new added

print(d.get("dept")) #get value of key
print(d.get("add1")) # give none
print(d["add1"]) #give error








