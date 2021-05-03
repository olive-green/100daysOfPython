#in python u can also give variables name in parameter and u have to use double star to indicate that you are using keyword also .

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)


person("Pankaj", age=20,mobile=9837839099)