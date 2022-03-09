
from os import path, remove

def remove_file_from_disk(file_name : str = None) -> int:
    """
    Remove file with name {file_name} from the disk.
    Return Type: int
        1 : successful removal
        0 : no file name
        -1 : file does not exist
    """
    if file_name == None:
        return 0

    file_path = f"./disk_file_storage/{file_name}"
    if path.exists(file_path) == False:
        return -1
    
    # remove file from "../disk_file_storage/" directory
    remove(file_path)  # os.remove(file_location)
   
    return 1
