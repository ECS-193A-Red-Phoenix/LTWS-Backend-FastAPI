import requests, os
from pathlib import Path
from pprint import pprint
from typing import List


BASE_URL = "http://localhost:8000"
BINARIES_FOLDER = str(Path.cwd()) + "/binaries/temperature"


def single_file_upload(file_to_upload_path : str):
    local_file = Path(file_to_upload_path)
    print(local_file)
    file_data = { 
        "file" : local_file.open(mode = "rb")
    }

    print()
    print("ABOUT TO TRANSMIT")
    print()

    response = requests.post(f"{BASE_URL}/input_to_disk/", files = file_data)
    pprint(response.json())


def multiple_file_transfer():
    # get all files in the directory
    files_in_directory : List[str] = os.listdir(path = BINARIES_FOLDER)
    for i, n in enumerate(files_in_directory):
        print(i, n)

    print("=================================================")

    for i, file_name in enumerate(files_in_directory):  # transfer each ile to the server
        print(i, file_name)
        file_path = f"{BINARIES_FOLDER}/{file_name}"
        single_file_upload(file_to_upload_path = file_path)


multiple_file_transfer()  # transfer all the files in temperature subdirectory to the server