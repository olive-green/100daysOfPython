data={1:"pankaj",3:"ankit",4:"anjali"}

print(data[4])

print(data.get(1))

# //merge two list into a dictionary

keys=["Pankaj","ankit","anjali"]
values=["coder","basketballer","athelete"]

skills= dict(zip(keys,values)) # zip function is used to merge two lists and dict converted them into dictionary

# dictionaries are mutable
skills["ankit"]="medico"

print(skills)