import os
import boto3
def clear_files_in_folders(directory):
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct the full path to the file
            file_path = os.path.join(root, file)
            # Remove the file
            os.remove(file_path)
            print(f"Deleted: {file_path}")
clear_files_in_folders("/home/ubuntu/CTIC/GOESimages/noaa-goes16")

# Crea un recurso de S3

s3 = boto3.resource('s3')
bucket = s3.Bucket('eata-smartmachines')

# Lista y elimina todos los objetos
for obj in bucket.objects.all():
    obj.delete()


