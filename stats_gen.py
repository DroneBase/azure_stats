import math
import os
import datetime

from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError
from azure.storage.blob import BlobServiceClient
from tabulate import tabulate


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


class BlobStats(object):

    connection_string = "DefaultEndpointsProtocol=https;AccountName=statsecureacl;AccountKey=qeib+Ov04t8c38c+PuAyPvfLQQDaSXLowIPcvchc3h3pLyGwMlpK06AQILEuuxIKZiXVrTE9lUaOETnA7w5GpQ==;EndpointSuffix=core.windows.net"
    print("Folder Name Example - Jaison/Adani/Adani_10mwp_vijayanagaram/RAW/Mapping/RGB")
    folder_name = input("Enter folder name from internal-pilots-upload bucket: ")
    print(folder_name)
    if not folder_name:
        print("Pilot name not mentioned")
        exit(0)

    date_entry = input("Enter a date in YYYY-MM-DD format: ")
    year, month, day = map(int, date_entry.split("-"))
    input_data = datetime.date(year, month, day)
    print(input_data)
    if not input_data:
        print("Date not mentioned")
        exit(0)

    def get_blob_information(self):
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        container_client = blob_service_client.get_container_client("internal-pilots-upload")
        try:
            headers = ["File Name", "File Size", "File Size in Units", "Created Date", "Modified Date"]
            data = []
            list_blobs = container_client.list_blobs(self.folder_name)
            _size = 0
            for blob in list_blobs:
                if blob.size > 0 and blob.last_modified.date() == self.input_data:
                    _size += blob.size
                    data.append([blob.name, blob.size, convert_size(blob.size), blob.creation_time, blob.last_modified])
            print(tabulate(data, headers=headers))
            print("Total Size = {0}, Total Size in Units = {1}".format(str(_size), convert_size(_size)))
        except ResourceNotFoundError:
            print("Container not found.")


if __name__ == "__main__":
    blog_object = BlobStats()
    blog_object.get_blob_information()
