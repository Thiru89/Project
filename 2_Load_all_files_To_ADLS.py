from azure.storage.blob import BlobServiceClient 
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

storage_account_key = os.environ.get("storage_account_key")
storage_account_name ="strgforadb"
connection_string = os.environ.get("connection_string")
container_name = "tgt"
directory_path = 'C://Users//Vighnahartha//Downloads//SRC_FILES'

# Below function takes filepath and filename as inputs  and uploads the files into the ADLS
def uploadToBlobStorage(filepath, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    with open(filepath, "rb") as data:
            blob_client.upload_blob(data)
            
# Loads all the filenames from the directories
files = os.listdir(directory_path)
for file_name in files:
    file_path = os.path.join(directory_path, file_name)
    if os.path.isfile(file_path):
         uploadToBlobStorage(file_path,file_name)
         print(f"uploaded {file_name}.")