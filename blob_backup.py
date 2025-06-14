from azure.storage.blob import BlobServiceClient
import os

# Replace with your connection string from Azure
connection_string = "YOUR_AZURE_CONNECTION_STRING"
container_name = "backups"
local_file_path = "test_upload.txt"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Create container if it doesn't exist
try:
    blob_service_client.create_container(container_name)
    print("🪣 Container created.")
except:
    print("🪣 Container already exists.")

# Upload the file
with open(local_file_path, "rb") as data:
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.path.basename(local_file_path))
    blob_client.upload_blob(data, overwrite=True)
    print(f"✅ Uploaded {local_file_path}")
