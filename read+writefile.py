with open("fruits.txt", "a+") as myfile:
    myfile.write("\n Brinjal")  
    myfile.seek(0)
    content = myfile.read()

print(content)  
