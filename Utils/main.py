import os
from azure.storage.filedatalake import (
    DataLakeServiceClient,
    DataLakeDirectoryClient,
    FileSystemClient
)
from azure.identity import DefaultAzureCredential
from sas import sas_key

sas_token = sas_key()

# creating the service client
def get_service_client_sas(account_name: str, sas_token: str) -> DataLakeServiceClient:
    account_url = f"https://{account_name}.dfs.core.windows.net"
    service_client = DataLakeServiceClient(account_url, credential=sas_token)
    return service_client

try:
    print("about to connect to the storage account")
    service_client = get_service_client_sas("musilistorageaccount", sas_token=sas_token)
except Exception as e:
    print(f"Error connecting to the storage account: {e}")
    raise

# creating the file system client
def create_file_system(service_client: DataLakeServiceClient, file_system_name: str) -> FileSystemClient:
    file_system_client = service_client.create_file_system(file_system=file_system_name)
    return file_system_client

try:
    print("about to create the container")
    file_system_client = create_file_system(service_client=service_client, file_system_name="musilicontainer")
    print("done creating the container")
except Exception as e:
    print(f"Container already exists or error occurred: {e}")

# creating the directory client
def create_directory(file_system_client: FileSystemClient, directory_name: str) -> DataLakeDirectoryClient:
    directory_client = file_system_client.create_directory(directory_name)
    return directory_client

try:
    print("about to create the directory")
    directory_client = create_directory(file_system_client=file_system_client, directory_name="rawfile")
    print("done creating the directory")
except Exception as e:
    print(f"Directory already exists or error occurred: {e}")

# uploading file to the storage account
def upload_file_to_directory(directory_client: DataLakeDirectoryClient, local_path: str, file_name: str):
    file_client = directory_client.get_file_client(file_name)
    # accessing my local directory to hget the dataset
    with open(file=os.path.join(local_path, file_name), mode="rb") as data:
        file_client.upload_data(data, overwrite=True)
    print(f"Uploaded {file_name} to directory {directory_client.path_name}")

try:
    local_path = os.getcwd()  # or specify your file path
    file_name = "Superstore_Sample_Dataset.xlsx"  
    upload_file_to_directory(directory_client, local_path, file_name)
except Exception as e:
    print(f"Error uploading file: {e}")