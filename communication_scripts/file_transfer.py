import requests
from pathlib import Path
from pprint import pprint

BASE_URL = "http://localhost:8000"
BINARIES_FOLDER = Path.cwd() / "communication_scripts" / "binaries"
print(Path.cwd())
print(BINARIES_FOLDER)
def single_file_upload():
    binary_file = BINARIES_FOLDER / "plane_2"
    file_data = { 
        "file" : binary_file.open(mode = "rb")
    }
    response = requests.post(f"{BASE_URL}/input_to_db/", files = file_data)
    pprint(response.json())

single_file_upload()