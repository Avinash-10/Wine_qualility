##it will create templates for the project

import os

dirs = [                                          #creating folder for project
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebook",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore"
]

for file_ in files:
    with open(file_,"w") as f:
        pass