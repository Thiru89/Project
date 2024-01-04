from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

storage_account_key = os.environ.get("storage_account_key")
storage_account_name ="strgforadb"
connection_string = os.environ.get("connection_string")
container_name = "tgt"

def uploadToBlobStorage(filepath, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    with open(filepath, "rb") as data:
        blob_client.upload_blob(data)
    print(f"uploaded {file_name}.")

uploadToBlobStorage("C://Users//Vighnahartha//Downloads//circuits_test_1.csv","circuits_test_2")

