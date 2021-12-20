try:
    f=open("text_file.txt",'r')
except FileNotFoundError:
    print("No such file found ")
    
    f=open("text_file.txt",'w')
    print("Created file successfully")
    a=f.write("Enter the message u wanna save")
    print("Data entered successfully")
