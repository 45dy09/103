import os
import shutil

from_dir="C:/Users/sopha/Downloads"
to_dir="C:/Users/sopha/Downloads"

listOfFiles=os.listdir(from_dir)
#print(listOfFiles)

for file in listOfFiles:
    name,extension=os.path.splitext(file)
    #print(name)
    #print(extension)
    if extension=="":
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:
        path1=from_dir+"/"+file
        path2=to_dir+"/"+"images"
        path3=to_dir+"/"+"images"+"/"+file

        if os.path.exists(path2):
            print("moviendo "+file)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moviendo "+file)
            shutil.move(path1,path3)
