#Maureen Mbugua
#19/02/2026
#programme to perform file operations

#create new file
new_file = open("sleeping.txt","r+")


#write to new file
new_file.write("student name : Jace Norman, ID : 23458976 ,email : jacenorman12@gmail.com")



#read to new file
new_file = open("sleeping.txt","r+")

data = new_file.read()

print(data)

new_file.close()


#delete file
#os module
import os
os.remove("remove.txt")


#delete folder
os.remove("folder")




