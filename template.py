import os
from pathlib import Path

package_name="QA_System"

list_of_files=[
    f"{package_name}/__init__.py",
    f"{package_name}/data_ingestion.py",
    f"{package_name}/embedding.py",
    f"{package_name}/model_api.py",
    "logger.py",
    "exception.py",
    "Experiments/Experiments.ipynb",
    "requirements.txt",
    "setup.py",
    "StreamlitApp.py",
]


# here will create a directory

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")