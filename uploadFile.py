import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:

    
    script_path = os.path.realpath(__file__)
    folder = os.path.join(script_path, 'fol_near_script')
    if not os.path.exists(folder):
        os.mkdir(folder)

    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BF3UJgOrCQrcyeK4RqtLNSTqmxhW3KN2cR4-GYfoO1tCzseN3tASXlofxtot_LG-uMnbKag7OYbMY8S_PYbpf_iIH2iBN7-4jucDTDgK3cdeUOcUX8nIqLqQiQ8q9ECJuXwGtCuY3mjj'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()