def newFile():
    execFiles = []
    # open the contents of the file
    with open("file.txt") as f:
        x = f.readlines()
        
        for i in range(1,len(x)):
            el = x[i].split(",")
            if len(el) !=0:
                execFiles.append({"name": el[0],"age": el[1], "address": el[2], "phone": el[3], "email": el[4] })        
        
        with open("CustomerSupport", "w") as f1:
            for i in range(0,len(execFiles)):
                file = execFiles[i]
                if int(execFiles[i]["age"]) >= 40 and int(execFiles[i]["age"]) <= 59:
                    f1.write(file["name"] + ', ' + file['phone'] + ', ' + file['email'])
            f1.close()
        f.close()


newFile()
