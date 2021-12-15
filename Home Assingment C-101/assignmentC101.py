import dropbox
import os
from dropbox.files import WriteMode

class Transferdata:
    def __init__ (self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,fle_to):
        dbx=dropbox.Dropbox(self.access_token)
        for route,dir,files in os.walk(file_from):
            for filename in files:
                localPath=os.path.join(route,filename)
                relativePath=os.path.relpath(localPath,file_from)
                dbxPath=os.path.join(fle_to,relativePath)
                with open(localPath,'rb') as f:
                    dbx.files_upload(f.read(),dbxPath,mode=WriteMode('overwrite'))

def main():
    access_token="sl.A-O0llAF89TBUogR1s2HrLR6noUWHI6Q3UxPv2YNPtE7WkWnthcviBXTCSx_BznhEsKg6Z3WYpBss6-gplKvgGL5xdOlj4JyAbt8GNOyjNLVjgBBIS_NohkeDqs_ImJWLLgdPB-Ywt-Q"
    transferData=Transferdata(access_token)
    file_from=input("Enter your file path to transfer:")
    fle_to=input("Enter the path to upload to dropbox:")

    transferData.upload_file(file_from,fle_to)

    print("File has been moved successfully")

if __name__=="__main__":
    main()

                
