def main():
    print("Hello user")
    print("welcome")

# __name__ prints the __main__ if we write it in the file iteself
# else prints module name in the exporting file if we import the module

##like if we import this file into work.py then the __name__ of this file become module name in work.py
#but __name__ of work.py remains __main__


if __name__=="__main__":
    main()
    