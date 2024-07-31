import os
import shutil

def remove_pycache(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name == '_pycache_':
                pycache_path = os.path.join(root, dir_name)
                print(f"Removing {pycache_path}")
                shutil.rmtree(pycache_path)

if __name__ == "_main_":
    project_root = os.path.dirname(os.path.abspath(__file__))
    remove_pycache(project_root)