import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(source, destination):
    try:
        shutil.move(source, destination)
    except FileNotFoundError:
        print(f"File not found: {source}")
    except Exception as e:
        print(f"Error moving file: {e}")
        
def list_files(directory):
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
