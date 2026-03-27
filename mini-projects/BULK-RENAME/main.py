import os 

def arrange_files(files, ext):
    files_with_ext=[file for file in files if file.endswith(ext)]
    print("orignal name of files was\n",files_with_ext)     
    print("**************************************************")   
        # for file in files_with_ext :

        #     os.rename(file,f"photo-{i}{ext}")
        #     i+=1
    if not(os.path.exists("images")):
            os.mkdir("images")
    for i, file in enumerate(files_with_ext ): #enumarate will create i with initial value 0 
            os.rename(file,f"images/photo-{i+1}{ext}")
            i+=1
if __name__=="__main__":
    files=os.listdir() #will give list of files in a folder
    arrange_files(files,".jpg")